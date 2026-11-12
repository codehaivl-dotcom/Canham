"""Independent analytical/adversarial QA; no balance baselines are tuned here.

Private helpers are used only to isolate state transitions from RNG/AI decisions.
Public run() cases additionally verify integration, determinism and input isolation.
"""
from copy import deepcopy
import math
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from combat import CombatSimulator, expected_weapon_dps, load_catalog, make_squad, mitigate


STATS = {key: 5 for key in ('COM', 'END', 'AGI', 'PER', 'INT', 'TEC', 'MED', 'RES')}


class IndependentCombatQA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog()

    def setup_room(self, enemy='crawler', squad=None, seed=1):
        """Initialize durable room state without advancing an attack interval."""
        simulator = CombatSimulator(deepcopy(self.catalog), seed=seed)
        simulator.run(squad or make_squad(self.catalog, size=3), [enemy],
                      max_seconds=0, enable_consumables=False)
        players = [e for e in simulator.entities if e.side == 'player']
        enemies = [e for e in simulator.entities if e.side == 'enemy']
        return simulator, players, enemies

    def test_mitigation_independent_numeric_oracle(self):
        # Direct arithmetic from Implementation Baseline, not calls to engine internals.
        fixtures = [
            (100, 120, .2, 'ballistic', 40.0),
            (100, 120, .2, 'explosive', 53.33),
            (100, 999, -.25, 'energy', 125.0),
            (100, 999, .8, 'fire', 20.0),
            (100, -50, 0, 'ballistic', 100.0),
            (100, 0, .99, 'electric', 20.0),
            (100, 0, -.99, 'bio', 125.0),
        ]
        for raw, armor, resist, dtype, expected in fixtures:
            with self.subTest(dtype=dtype, armor=armor, resist=resist):
                self.assertEqual(expected, mitigate(raw, armor, resist, dtype))

    def test_valid_hit_floor_and_zero_damage(self):
        self.assertEqual(1, mitigate(.01, 9999, .8, 'ballistic'))
        self.assertEqual(0, mitigate(0, 100, .8, 'ballistic'))
        self.assertEqual(0, mitigate(-10, 0, 0, 'energy'))

    def test_pistol_expected_dps_from_probability(self):
        expected = (17 / .90) * .86 * ((1 - .05) + .05 * 1.5)
        self.assertAlmostEqual(expected, expected_weapon_dps(
            self.catalog['weapons']['pistol'], STATS), places=9)

    def test_assault_damage_and_cycle_bonus_apply_once(self):
        # Round mitigated ordinary/critical hits, as the direct-hit spec requires.
        ordinary, critical = round(16 * 1.08, 2), round(16 * 1.08 * 1.5, 2)
        expected = (.95 * ordinary + .05 * critical) * .82 * 1.05 / .62
        actual = expected_weapon_dps(self.catalog['weapons']['assault_rifle'],
                                     STATS, role='assault')
        self.assertAlmostEqual(expected, actual, places=9)

    def test_sniper_back_accuracy_bonus_not_doubled(self):
        expected = (52 / 1.90) * .97 * (1 + .12 * .5)
        actual = expected_weapon_dps(self.catalog['weapons']['sniper_rifle'],
                                     STATS, formation='back')
        self.assertAlmostEqual(expected, actual, places=9)

    def test_sniper_elite_damage_bonus(self):
        weapon = self.catalog['weapons']['sniper_rifle']
        normal = expected_weapon_dps(weapon, STATS, formation='mid')
        elite = expected_weapon_dps(weapon, STATS, formation='mid',
                                    enemy={'category': 'elite'})
        self.assertAlmostEqual(normal * 1.2, elite, delta=.01)

    def test_seed_replay_and_no_input_mutation(self):
        squad = make_squad(self.catalog, size=4)
        catalog_copy, squad_copy = deepcopy(self.catalog), deepcopy(squad)
        simulator = CombatSimulator(self.catalog, seed=1703)
        first = simulator.run(squad, ['crawler', 'spitter', 'rifleman'])
        second = simulator.run(squad, ['crawler', 'spitter', 'rifleman'])
        self.assertEqual(first, second)
        self.assertEqual(catalog_copy, self.catalog)
        self.assertEqual(squad_copy, squad)

    def test_first_attack_respects_interval(self):
        result = CombatSimulator(self.catalog, seed=4).run(
            make_squad(self.catalog, size=1, loadout='ballistic'), ['crawler'],
            max_seconds=.5, enable_consumables=False)
        self.assertFalse(any(e['kind'] in ('damage', 'miss') for e in result['events']))

    def test_fractional_interval_does_not_accumulate_tick_rounding_drift(self):
        catalog = deepcopy(self.catalog)
        catalog['enemies']['target_dummy'] = {'hp': 1e9, 'damage': 0, 'interval': 1e6}
        squad = [{'id': 'rate_probe', 'stats': STATS, 'formation': 'front',
                  'weapon': 'assault_rifle', 'armor': {}, 'max_hp': 1e6}]
        result = CombatSimulator(catalog, seed=8).run(
            squad, ['target_dummy'], max_seconds=62, enable_consumables=False)
        shots = [e for e in result['events'] if e.get('actor') == 'rate_probe'
                 and e['kind'] in ('damage', 'miss')]
        # 62 / .62 = 100 scheduled attacks; fixed step may delay an impact <= .1s,
        # but rounding each entire interval upward must not erase twelve shots.
        self.assertEqual(100, len(shots))

    def test_ordinary_shield_break_does_not_invent_disable(self):
        sim, players, enemies = self.setup_room()
        target = enemies[0]
        target.shield = 1
        sim._damage(players[0], target, 10, 'energy')
        self.assertEqual(0, target.controlled_until)
        self.assertFalse(any(e['kind'] == 'control' for e in sim.events))

    def test_scout_accuracy_bonus_lasts_for_first_target_not_first_shot(self):
        class ProbabilityProbe:
            def random(self):
                return .9  # Pistol .86 misses; Scout first-target .96 hits.
        squad = [{'id': 'scout_probe', 'stats': STATS, 'role': 'scout',
                  'formation': 'front', 'weapon': 'pistol'}]
        sim, players, enemies = self.setup_room(squad=squad)
        sim.rng = ProbabilityProbe()
        enemies[0].hp = enemies[0].max_hp = 1e6
        sim._attack(players[0], enemies[0])
        sim.t = 1
        sim._attack(players[0], enemies[0])
        hits = [e for e in sim.events if e['kind'] == 'damage']
        self.assertEqual(2, len(hits))

    def test_shield_overflow_mitigates_exactly_once(self):
        sim, players, enemies = self.setup_room()
        target = enemies[0]
        target.armor, target.resistances, target.hp, target.shield = 120, {'ballistic': .2}, 100, 10
        sim._damage(players[0], target, 100, 'ballistic')
        self.assertEqual(0, target.shield)
        self.assertEqual(70, target.hp)  # 40 post-mitigation: 10 shield + 30 HP.
        self.assertEqual(1, sum(e['kind'] == 'shield_break' for e in sim.events))
        sim._damage(players[0], target, 10, 'energy')
        self.assertEqual(1, sum(e['kind'] == 'shield_break' for e in sim.events))

    def test_dot_has_no_one_damage_floor(self):
        sim, players, enemies = self.setup_room()
        target = enemies[0]
        target.resistances['fire'] = .8
        before = target.hp
        sim._damage(players[0], target, 3, 'fire', direct=False)
        self.assertAlmostEqual(.6, before - target.hp)

    def test_heal_never_revives_down_or_overfills(self):
        sim, players, _ = self.setup_room()
        medic, target = players[2], players[0]
        target.hp = target.max_hp - 2
        sim._heal(medic, target, 10000)
        self.assertEqual(target.max_hp, target.hp)
        target.state, target.hp = 'DOWN', 0
        sim._heal(medic, target, 10000)
        self.assertEqual(('DOWN', 0), (target.state, target.hp))

    def test_critical_event_applies_one_and_half_once(self):
        class GuaranteedHitAndCrit:
            def random(self):
                return 0
        squad = [{'id': 'crit_probe', 'stats': STATS, 'formation': 'mid',
                  'weapon': 'pistol'}]
        sim, players, enemies = self.setup_room(squad=squad)
        sim.rng = GuaranteedHitAndCrit()
        enemies[0].armor = 0
        enemies[0].resistances = {}
        sim._attack(players[0], enemies[0])
        hit = next(e for e in sim.events if e['kind'] == 'damage')
        self.assertTrue(hit['critical'])
        self.assertEqual(25.5, hit['amount'])

    def test_character_hp_formula_and_role_trait_order(self):
        for level in (1, 20, 50):
            for endurance in (1, 5, 10):
                for role in ('none', 'vanguard'):
                    with self.subTest(level=level, endurance=endurance, role=role):
                        stats = {**STATS, 'END': endurance}
                        squad = [{'id': 'hp_probe', 'stats': stats, 'level': level,
                                  'role': role, 'traits': ['Tough'],
                                  'formation': 'front', 'weapon': 'pistol'}]
                        sim, players, _ = self.setup_room(squad=squad)
                        expected = (100 + 12 * endurance + 5 * (level - 1))
                        expected *= 1.2 if role == 'vanguard' else 1
                        expected *= 1.08
                        self.assertAlmostEqual(expected, players[0].max_hp)

    def test_dead_enemy_does_not_receive_new_damage(self):
        sim, players, enemies = self.setup_room()
        enemy = enemies[0]
        sim._damage(players[0], enemy, 1e6)
        logged = len(sim.events)
        sim._damage(players[0], enemy, 1e6)
        self.assertEqual(logged, len(sim.events))
        self.assertEqual(0, enemy.hp)

    def test_first_lethal_second_lethal_and_body_untargetable(self):
        sim, players, enemies = self.setup_room()
        target = players[0]
        sim._damage(enemies[0], target, 1e6)
        self.assertEqual('DOWN', target.state)
        self.assertEqual(60, target.bleedout)
        sim._damage(enemies[0], target, 1e6)
        self.assertEqual('DOWN', target.state)
        target.state, target.hp, target.revive_count = 'ACTIVE', 10, 1
        sim._damage(enemies[0], target, 1e6)
        self.assertEqual('DEAD_RECOVERABLE', target.state)
        self.assertFalse(target.active)

    def test_completed_revive_consumes_once_and_sets_trauma(self):
        sim, players, enemies = self.setup_room()
        actor, target = players[2], players[0]
        sim._damage(enemies[0], target, 1e6)
        sim._items(actor)
        self.assertEqual('revival_injector', actor.action['kind'])
        sim.t = 2.2
        sim._complete_item(actor)
        self.assertEqual('DOWN', target.state)
        sim.t = 2.3  # 3 sec base * .75 Medic, on the next .1 tick.
        sim._complete_item(actor)
        self.assertEqual('ACTIVE', target.state)
        self.assertEqual(1, target.revive_count)
        self.assertAlmostEqual(target.max_hp * .4, target.hp)
        self.assertIn('trauma', target.flags)
        self.assertEqual(0, actor.consumables['revival_injector'])
        sim._complete_item(actor)
        self.assertEqual(1, sim.items_used['revival_injector'])

    def test_incapacitated_reviver_cancels_without_consumption(self):
        sim, players, enemies = self.setup_room()
        actor, target = players[2], players[0]
        sim._damage(enemies[0], target, 1e6)
        sim._items(actor)
        sim._damage(enemies[0], actor, 1e6)
        sim.t = 3
        sim._complete_item(actor)
        self.assertEqual(1, actor.consumables['revival_injector'])
        self.assertIsNone(actor.action)
        self.assertEqual('DOWN', target.state)

    def test_second_field_revive_is_rejected(self):
        sim, players, enemies = self.setup_room()
        target, medic = players[0], players[2]
        target.revive_count = 1
        sim._damage(enemies[0], target, 1e6)
        sim._items(medic)
        self.assertNotEqual('revival_injector', (medic.action or {}).get('kind'))

    def test_tutorial_lethal_is_safe_down(self):
        squad = make_squad(self.catalog, size=1)
        squad[0]['hp'] = 1
        result = CombatSimulator(self.catalog, seed=1).run(
            squad, ['crawler'], max_seconds=10, enable_consumables=False,
            overrides={'tutorial_protected': True, 'enemy_damage_multiplier': 100})
        self.assertEqual('protected_return', result['outcome'])
        self.assertEqual('SAFE_DOWN', result['survivors'][0]['state'])

    def test_simultaneous_last_kill_and_lethal_is_wipe(self):
        catalog = deepcopy(self.catalog)
        catalog['enemies']['duelist'] = {'hp': 1, 'damage': 1000, 'interval': .1,
                                        'accuracy': .98, 'crit': 0, 'armor': 0}
        squad = [{'id': 'duelist_player', 'stats': STATS, 'max_hp': 1,
                  'formation': 'front', 'weapon': {'id': 'qa', 'damage': 1000,
                  'interval': .1, 'accuracy': .98, 'crit': 0}}]
        result = CombatSimulator(catalog, seed=1).run(
            squad, ['duelist'], max_seconds=1, enable_consumables=False)
        self.assertEqual('wipe', result['outcome'])
        self.assertEqual('DEAD', result['enemies'][0]['state'])
        self.assertEqual('DOWN', result['survivors'][0]['state'])

    def test_aoe_falloff_has_no_duplicate_targets(self):
        sim, players, enemies = self.setup_room()
        primary = enemies[0]
        for i in range(4):
            sim._spawn('crawler', primary)
        targets = sim._aoe(primary, [1, .6, .45, .3], 'rocket')
        self.assertEqual([1, .6, .45, .3], [factor for _, factor in targets])
        self.assertEqual(4, len({entity.id for entity, _ in targets}))
        cone = sim._aoe(primary, [1, .45, .25], 'cone')
        self.assertEqual(3, len(cone))

    def test_emp_boss_reduction_and_repeat_diminishing(self):
        sim, _, enemies = self.setup_room('war_machine_a_17')
        target = enemies[0]
        sim._cc(target, 'emp', 2.5)
        self.assertAlmostEqual(1, target.controlled_until)
        sim.t = 2
        sim._cc(target, 'emp', 2.5)
        self.assertAlmostEqual(2.5, target.controlled_until)

    def test_continuous_cc_cap_and_immunity(self):
        sim, _, enemies = self.setup_room()
        target = enemies[0]
        sim._cc(target, 'emp', 10)
        self.assertEqual(4, target.controlled_until)
        self.assertEqual(6, target.immune_until)
        sim.t = 3
        sim._cc(target, 'stagger', 10)
        self.assertEqual(4, target.controlled_until)
        sim.t = 6
        sim._cc(target, 'stagger', 1)
        self.assertEqual(7, target.controlled_until)

    def test_hive_spawn_waves_are_finite(self):
        sim, players, enemies = self.setup_room('hive_mother')
        boss = enemies[0]
        sim.active_cap = 8
        for t in (18, 36, 54, 72, 90, 108):
            sim.t = t
            sim._ability(boss)
            # Kill adds between waves to distinguish finite-wave limit from cap.
            for add in sim.entities:
                if add.side == 'enemy' and add is not boss:
                    add.state, add.hp = 'DEAD', 0
        spawns = [event for event in sim.events if event['kind'] == 'spawn']
        self.assertEqual(6, len(spawns))  # 3 waves * 2 Crawlers.
        self.assertLessEqual(sim.max_active_enemies, 8)

    def test_fallen_phase_trigger_is_one_shot(self):
        sim, _, enemies = self.setup_room('fallen_visitor')
        boss = enemies[0]
        boss.hp = boss.max_hp * .5
        shield_before = boss.shield
        sim._ability(boss)
        sim._ability(boss)
        self.assertEqual(2, sum(e['kind'] == 'spawn' for e in sim.events))
        self.assertEqual(shield_before + 250, boss.shield)
        self.assertEqual(1, sum(e['kind'] == 'boss_phase' for e in sim.events))

    def test_war_machine_repair_add_only_once(self):
        sim, _, enemies = self.setup_room('war_machine_a_17')
        boss = enemies[0]
        boss.hp = boss.max_hp * .75
        sim._ability(boss)
        boss.hp = boss.max_hp * .9
        sim._ability(boss)
        boss.hp = boss.max_hp * .7
        sim._ability(boss)
        self.assertEqual(1, sum(e['kind'] == 'spawn' for e in sim.events))

    def test_adaptive_resistance_stays_within_contract(self):
        sim, _, enemies = self.setup_room('fallen_visitor')
        boss = enemies[0]
        for t in range(20, 401, 20):
            sim.t = t
            boss.recent_damage.append((t, 'energy', 100))
            sim._ability(boss)
        self.assertTrue(all(-.25 <= value <= .8 for value in boss.resistances.values()))
        self.assertEqual(.8, boss.resistances['energy'])

    def test_integration_results_finite_and_bounded(self):
        for seed in range(10):
            with self.subTest(seed=seed):
                result = CombatSimulator(self.catalog, seed=seed).run(
                    make_squad(self.catalog, size=5), ['security_bot', 'repair_drone'])
                self.assertTrue(math.isfinite(result['duration']))
                self.assertTrue(0 <= result['hp_loss_fraction'] <= 1)
                for entity in result['survivors']:
                    self.assertTrue(0 <= entity['hp'] <= entity['max_hp'] + .01)
                    self.assertLessEqual(entity['revive_count'], 1)
                    self.assertTrue(all(v >= 0 for v in entity['consumables'].values()))


if __name__ == '__main__':
    unittest.main()
