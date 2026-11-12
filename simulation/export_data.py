"""Export documented prototype tables; stdlib only, deterministic, fail on drift.

Free-form ability/effect prose is retained beside explicit structured adapters.
Adapters are interpretations of cited sections, never claims of runtime support.
Run: python simulation/export_data.py [--combat-only] [--check]
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "simulation" / "data"
TYPES = ("ballistic", "energy", "explosive", "fire", "electric", "bio")
STATS = ("COM", "END", "AGI", "PER", "INT", "TEC", "MED", "RES")
SOURCES: dict[str, dict] = {}


def read(name):
    path = ROOT / "docs" / name
    raw = path.read_bytes()
    SOURCES[name] = {"path": f"docs/{name}", "sha256": hashlib.sha256(raw).hexdigest()}
    return raw.decode("utf-8-sig")


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "_", s).strip("_")


def number(s):
    m = re.search(r"[-+]?\d+(?:\.\d+)?", s.replace(",", ""))
    if not m:
        raise ValueError(f"Missing numeric value: {s!r}")
    n = float(m.group())
    return int(n) if n.is_integer() else n


def minutes(s):
    n = number(s)
    return n * 60 if re.search(r"\d\s*h", s) else n / 60 if re.search(r"\d\s*s(?:ec)?\b", s) else n


def table_rows(text):
    return [[x.strip() for x in line.strip().strip("|").split("|")]
            for line in text.splitlines() if line.strip().startswith("|")
            and not re.match(r"\|\s*[-:]", line.strip())]


def section(text, pattern):
    m = re.search(pattern, text, re.M)
    if not m:
        raise ValueError(f"Missing section: {pattern}")
    end = re.search(r"^#{1,2} ", text[m.end():], re.M)
    return text[m.end():m.end() + end.start()] if end else text[m.end():]


def provenance(path, heading):
    return {"path": f"docs/{path}", "section": heading}


def ability(aid, **kwargs):
    return {"id": aid, "adapter_status": "documented_parameters_interpreted", **kwargs}


def combat():
    unit = read("UNITS_ITEMS_V0.1.md")
    enemy = read("ENEMIES_RESISTANCES_V0.1.md")
    content = read("PROTOTYPE_CONTENT_PACK_V0.1.md")
    implementation = read("IMPLEMENTATION_BASELINE_V0.1.md")
    read("SURVIVOR_RECOVERY_V0.1.md")
    weapons = {}
    effects = {
        "pistol": {}, "smg": {"front_mid_damage_multiplier": 1.10, "far_accuracy_delta": -.15},
        "assault_rifle": {}, "shotgun": {"aoe_falloff": [1, .45, .25], "front_damage_multiplier": 1.10},
        "laser_rifle": {"focus_per_second": .04, "focus_cap": .20},
        "sniper_rifle": {"elite_boss_damage_multiplier": 1.20, "back_accuracy_delta": .05, "back_bonus_apply_once": True},
        "rocket_launcher": {"aoe_falloff": [1, .60, .45, .30], "stagger_seconds": .5},
        "flamethrower": {"aoe_falloff": [1, .60, .60], "burn_dps": 3, "burn_seconds": 4},
        "emp_rifle": {"buildup_per_hit": 1, "mechanical_threshold": 3, "shielded_organic_threshold": 4, "disable_seconds": 2.5},
    }
    damage_types = dict(zip(effects, ["ballistic"] * 4 + ["energy", "ballistic", "explosive", "fire", "electric"]))
    for row in table_rows(section(unit, r"^# 11\. Weapon Baseline")):
        if len(row) != 7 or row[0] == "Weapon":
            continue
        key = slug(row[0])
        weapons[key] = {"id": key, "name": row[0], "damage": number(row[1]), "interval": number(row[2]),
                        "base_dps_display": number(row[3]), "accuracy": number(row[4]) / 100,
                        "crit": number(row[5]) / 100, "damage_type": damage_types[key],
                        "effects": effects[key], "identity": row[6],
                        "source": provenance("UNITS_ITEMS_V0.1.md", "11–12 Weapon baseline/effects")}
    armor = {}
    for row in table_rows(section(unit, r"^# 16\. Armor Archetypes")):
        if len(row) != 4 or row[0] == "Armor":
            continue
        key = slug(row[0]); res = dict.fromkeys(TYPES, 0)
        if key == "combat_armor": res["ballistic"] = .10
        if key == "hazmat_suit": res["bio"] = .45
        if key == "insulated_suit": res.update(electric=.35, energy=.35)
        armor[key] = {"id": key, "name": row[0], "armor": number(row[1]), "resistances": res,
                      "attack_speed_multiplier": .97 if key == "combat_armor" else .92 if key == "heavy_armor" else 1,
                      "special_text": row[2], "penalty_text": row[3],
                      "effects": {"radiation_resistance": .45} if key == "hazmat_suit" else {},
                      "source": provenance("UNITS_ITEMS_V0.1.md", "16 Armor Archetypes")}
    # Natural-language Hazmat '-5% Armor vs ballistic' is interpreted literally as armor ×.95.
    armor["hazmat_suit"]["effects"]["ballistic_armor_multiplier"] = .95
    roles = {
        "vanguard": {"hp_multiplier": 1.20, "aggro_multiplier": 1.25, "stagger_resistance": .15},
        "assault": {"damage_multiplier": 1.08, "attack_speed_multiplier": 1.05},
        "scout": {"crit_delta": .05, "first_target_accuracy_delta": .10, "intel_contribution_multiplier": 1.15},
        "engineer": {"tech_multiplier": 1.20, "emp_duration_multiplier": 1.20},
        "medic": {"healing_multiplier": 1.25, "revive_time_multiplier": .75, "revive_hp_fraction": .40},
        "heavy": {"aoe_multiplier": 1.15, "stagger_multiplier": 1.15, "heavy_penalty_multiplier": .50},
    }
    for key, value in roles.items():
        value.update(id=key, source=provenance("UNITS_ITEMS_V0.1.md", "5 Roles"))
    adapters = {
        "spitter": [ability("acid_spit", corrode_chance=.20, armor_delta=-10, duration=6)],
        "bloated": [ability("rupture", trigger="death", damage=22, damage_type="bio", targets="nearby")],
        "mutated_brute": [ability("heavy_slam", cooldown=8, damage=26, damage_type="ballistic", targets="front", stagger_seconds=.5)],
        "hive_carrier": [ability("brood_release", hp_thresholds=[.65, .30], spawn="crawler", counts=[1, [1, 2]], once_per_threshold=True)],
        "breacher": [ability("breach_rush", first_hit_multiplier=1.25)],
        "marksman": [ability("marked_shot", every_n_attacks=3, targets="back_mid", crit_delta=.15)],
        "tech_raider": [ability("jammer", cooldown=10, duration=5, accuracy_delta=-.10), ability("deploy_shield_drone", shield=50, once=True, target="lowest_hp_ally")],
        "sentry_drone": [ability("emp_vulnerable", grenade_disable_seconds=4)],
        "security_bot": [ability("guard_protocol", aggro_multiplier=1.20)],
        "repair_drone": [ability("repair_beam", heal_per_second=18, duration=3, cooldown=8, target="mechanical_ally")],
        "stalker": [ability("shadow_leap", targets="back", first_hit_multiplier=1.20, once=True)],
        "spore_weaver": [ability("spore_cloud", cooldown=9, duration=6, damage_per_second=4, damage_type="bio", targets="room_zone")],
        "rift_hound": [ability("phase_dash", dodge_chance=.20, cooldown=4)],
        "void_caster": [ability("distortion_field", while_shielded=True, ally_energy_resistance=.10), ability("shield_break", emp_buildup_multiplier=1.40, stagger_seconds=2)],
        "alpha_brute": [ability("roar", cooldown=14, duration=5, attack_speed_delta=-.15, resolve_check=True), ability("ground_slam", cooldown=9, damage=35, damage_type="ballistic", targets="front_mid")],
        "warden_mech": [ability("shield_cycle", no_hit_seconds=5, shield=80), ability("suppression_burst", accuracy_delta=-.12, duration=4)],
        "phase_hunter": [ability("phase", cooldown=10, untargetable_seconds=1.2, targets="mid_back"), ability("marked_prey", target="lowest_hp", damage_multiplier=1.15, duration=6)],
        "hive_mother": [ability("hive_phases", thresholds=[.70, .35], spawn_interval=18, phase1_spawn={"crawler": 2}, phase2_spawn={"spitter": 1, "crawler": 1}, phase2_zone_dps=4, phase2_zone_duration=6, phase2_zone_interval=12, phase3_interval_multiplier=.85, phase3_slam_damage=35, phase3_slam_interval=8, max_spawn_waves=3)],
        "war_machine_a_17": [ability("war_machine_phases", repair_drone_threshold=.75, shield_break_armor_multiplier=.65, exposure_seconds=12, emp_exposure_bonus=3, overheat_threshold=.35, overheat_fire_resistance=.40, overheat_attack_speed_multiplier=1.20, hazard_damage=6, hazard_interval=10, hazard_type="fire")],
        "fallen_visitor": [ability("adaptive_shell", interval=20, resistance_gain=.20, other_resistance_delta=-.15, resistance_cap=.80), ability("phase_shift", hp_threshold=.50, spawn={"stalker": 2}, shield=250, once=True)],
    }
    enemies = {}
    names = {"Scavenger Rifleman": "rifleman", "Auto Turret Mk II": "auto_turret"}
    for m in re.finditer(r"^## ((?:INF|HUM|MEC|ALN|ELT|BOSS)-\d+) — (.+)$", enemy, re.M):
        following = enemy[m.end():]
        end = re.search(r"^#{1,2} ", following, re.M)
        body = following[:end.start()] if end else following
        name = m[2].strip(); key = names.get(name, slug(name))
        stats = {r[0]: number(r[1]) for r in table_rows(body) if len(r) == 2 and r[0] in {"HP", "Shield", "Damage", "Attack Interval", "Armor", "Threat Cost"}}
        res = dict.fromkeys(TYPES, 0)
        resist_rows = [r for r in table_rows(body) if len(r) == 6 and "%" in r[0]]
        if resist_rows:
            res = dict(zip(TYPES, [number(v) / 100 for v in resist_rows[0]]))
        family = {"INF": "infected", "HUM": "raider", "MEC": "mechanical", "ALN": "alien"}.get(m[1].split("-")[0])
        if family is None:
            family = "mechanical" if key in {"warden_mech", "war_machine_a_17"} else "infected" if key in {"alpha_brute", "hive_mother"} else "alien"
        role_m = re.search(r"\*\*Role:\*\* (.+)", body)
        dtype = "bio" if key in {"spitter", "spore_weaver"} else "energy" if key == "void_caster" else "ballistic"
        enemies[key] = {"id": key, "document_id": m[1], "name": name, "hp": stats["HP"], "shield": stats.get("Shield", 0),
                        "damage": stats["Damage"], "interval": stats["Attack Interval"], "armor": stats["Armor"],
                        "threat_cost": stats.get("Threat Cost"), "damage_type": dtype, "family": family,
                        "role": role_m[1].strip() if role_m else "boss", "category": "boss" if m[1].startswith("BOSS") else "elite" if m[1].startswith("ELT") else "regular",
                        "resistances": res, "abilities": adapters.get(key, []), "source_text": body.strip(),
                        "source": provenance("ENEMIES_RESISTANCES_V0.1.md", f"{m[1]} — {name}"),
                        "damage_type_assumption": "Direct attack type not explicitly tabulated; adapter maps Bio-pressure to bio, Void Caster to energy, physical/gun/melee to ballistic; ability types override."}
    # Check the full resistance matrix agrees, including deliberately edited historical discrepancies.
    matrix = section(enemy, r"^# 14\. Full Resistance Matrix")
    aliases = {"Rifleman": "rifleman", "Auto Turret": "auto_turret"}
    for row in table_rows(matrix):
        if len(row) != 7 or row[0] == "Enemy": continue
        key = aliases.get(row[0], slug(row[0]))
        assert [number(v) / 100 for v in row[1:]] == list(enemies[key]["resistances"].values()), ("Resistance drift", key)
    roster = []
    initial_roles = ["vanguard", "assault", "medic", None, None, None]
    for row in table_rows(content):
        if row[0].startswith("SUR-"):
            vals = [int(v.strip()) for v in row[2].split("/")]
            assert len(vals) == 8 and sum(vals) == int(row[3]) and 32 <= sum(vals) <= 44
            i = len(roster)
            roster.append({"id": row[0], "name": row[1], "stats": dict(zip(STATS, vals)), "role": initial_roles[i],
                           "weapon": ["shotgun", "assault_rifle", "pistol", "pistol", "pistol", "pistol"][i], "armor": "civilian_jacket",
                           "formation": ["front", "mid", "back", None, None, None][i], "assignment_text": row[5], "profession_trait_text": row[4], "level": 1})
    for m in re.finditer(r"(SUR-00[78]) \*\*(.+?)\*\*: ([\d /]+) = \*\*(\d+)\*\*", content):
        vals = [int(v.strip()) for v in m[3].split("/")]
        assert len(vals) == 8 and sum(vals) == int(m[4]) and 32 <= sum(vals) <= 44
        roster.append({"id": m[1], "name": m[2], "stats": dict(zip(STATS, vals)), "role": None, "weapon": None, "armor": None, "formation": None, "level": 1, "rescue": True})
    consumables = {}
    for row in table_rows(section(unit, r"^# 20\. Consumables")):
        if len(row) != 3 or row[0] == "Item": continue
        key = slug(row[0]); consumables[key] = {"id": key, "name": row[0], "effect_text": row[1], "stack": int(row[2]), "source": provenance("UNITS_ITEMS_V0.1.md", "20 Consumables")}
    encounters = []
    packages = [("swarm", ["crawler"] * 4), ("brute_swarm", ["mutated_brute", "crawler", "crawler"]),
                ("carrier_swarm", ["hive_carrier", "crawler", "crawler", "spitter"]), ("raider_basic", ["rifleman", "rifleman", "breacher"]),
                ("marksman_room", ["marksman", "rifleman", "rifleman"]), ("tech_raider_room", ["tech_raider", "breacher", "rifleman", "rifleman"]),
                ("security_pair", ["security_bot", "sentry_drone"]), ("repair_room", ["security_bot", "repair_drone", "sentry_drone"]),
                ("crystal_stalker", ["crystal_beast", "stalker"]), ("spore_hounds", ["spore_weaver", "rift_hound", "rift_hound"]),
                ("void_stalkers", ["void_caster", "stalker", "stalker"])]
    for key, ids in packages:
        encounters.append({"id": key, "difficulty": "medium", "enemies": ids, "category": "regular", "source": provenance("ENEMIES_RESISTANCES_V0.1.md", "29 Prototype Encounter Set")})
    for key, value in enemies.items():
        if value["category"] in {"elite", "boss"}: encounters.append({"id": f"solo_{key}", "difficulty": "medium", "enemies": [key], "category": value["category"]})
    assert len(weapons) == 9 and len(armor) == 6 and len(enemies) == 24 and len(roster) == 8 and len(consumables) == 10, (len(weapons),len(armor),len(enemies),len(roster),len(consumables))
    extras = expanded_items(unit, read("POPULATION_TRAITS_V0.1.md"), implementation, weapons, armor, consumables)
    return {"schema_version": 1, "weapons": weapons, "armor": armor, "roles": roles, "enemies": enemies, **extras,
            "roster": roster, "consumables": consumables, "encounters": encounters,
            "difficulty": {"easy": {"hp": .90, "damage": .90}, "medium": {"hp": 1, "damage": 1}, "hard": {"hp": 1.10, "damage": 1.10}, "extreme": {"hp": 1.18, "damage": 1.18}},
            "assumptions": ["Enemy direct damage types are explicit adapter assumptions; enemy attack accuracy is absent from stat tables and must be labeled by the engine, not fabricated as parsed data.", "Boss Threat Cost is null because Boss Budget is Fixed, never zero-cost generated content.", "Ability parameters exported does not imply engine implements every ability; runner must report unsupported IDs.", "Hazmat ballistic armor penalty interpreted as armor ×0.95, not resistance -5 percentage points.", "Engineer tech and EMP bonuses describe overlapping effect fields; engine must document whether it applies role multiplier once or stacks two distinct bonuses."]}


RESOURCE_NAMES = {"RD": "research_data", "Research Data": "research_data", "Scrap": "scrap", "Components": "components", "Chemicals": "chemicals", "Food": "food", "Water": "water", "Supply": "supply", "Credits": "credits", "Military Data": "military_data", "Prototype Core": "prototype_core", "Alien Material": "alien_material", "Reactor Material": "reactor_material", "Energy Cells": "energy_cells", "Population": "population"}


def subheads(text, depth=2):
    pattern = rf"^{'#' * depth} (.+)$"
    matches = list(re.finditer(pattern, text, re.M))
    for i, m in enumerate(matches):
        body = text[m.end():matches[i+1].start() if i+1 < len(matches) else len(text)]
        yield m[1].strip(), re.sub(r"^---\s*$", "", body, flags=re.M).strip()


def declared_numbers(text):
    return re.findall(r"[-+]?\d+(?:\.\d+)?\s*%?", text)


def expanded_items(unit, population, implementation, weapons, armor, consumables):
    """Keep complete catalog coverage distinct from runner effect support."""
    named = {}
    base_map = {"C-9 Civilian Pistol": "pistol", "M-4 Service Rifle": "assault_rifle", "LX-3 Laser Carbine": "laser_rifle",
                "HSR-12 Marksman Rifle": "sniper_rifle", "R-7 Breach Launcher": "rocket_launcher", "PYR-2 Incinerator": "flamethrower"}
    for name, body in subheads(numbered(unit, 15)):
        key = slug(name); base = base_map[name]; overrides = {}
        for field, pattern in {"damage": r"- Damage\s+(\d+)", "interval": r"- (?:Interval\s+|)(\d+(?:\.\d+)?)\s*sec", "accuracy": r"- Accuracy\s+(\d+)%"}.items():
            m = re.search(pattern, body)
            if m: overrides[field] = float(m[1]) / 100 if field == "accuracy" else number(m[1])
        if "interval" not in overrides:
            m = re.search(r"- Interval\s+([\d.]+)", body)
            if m: overrides["interval"] = number(m[1])
        named[key] = {"id": key, "name": name, "kind": "named_weapon", "base_weapon": base,
                      "overrides": overrides, "absolute_stats": {f: overrides.get(f, weapons[base][f]) for f in ["damage", "interval", "accuracy", "crit", "damage_type"]},
                      "inherited_fields": [f for f in ["damage", "interval", "accuracy", "crit"] if f not in overrides],
                      "apply_tier_multiplier": False, "effect_text": body, "numeric_declarations": declared_numbers(body),
                      "implementation_status": "catalog_complete_base_effects_available_variant_not_automatically_simulated",
                      "source": provenance("UNITS_ITEMS_V0.1.md", f"15 {name}")}
    assert len(named) == 6
    utilities = {}
    utility_parameters = {"tactical_scanner": {"scout_confidence_delta": .10, "next_room_hint_charges": 1},
                          "portable_shield": {"shield_hp_fraction": .25, "duration": 10},
                          "breaching_tool": {}, "drone": {"adjacent_room_reveals": 1},
                          "bio_scanner": {"bio_detection_delta": .15}, "shield_module": {"energy_resistance_delta": .10, "shield_hp_fraction": .05}}
    for name, body in subheads(numbered(unit, 18)):
        key = slug(name)
        entry = {"id": key, "name": name, "kind": "utility", "parameters": utility_parameters[key], "effect_text": body,
                 "numeric_declarations": declared_numbers(body), "implementation_status": "catalog_only_unmodeled_utility_actions",
                 "unresolved": ["Cooldown/charges or interaction availability not fully quantified in source; no invented value."],
                 "source": provenance("UNITS_ITEMS_V0.1.md", f"18 {name}")}
        utilities[key] = entry; named[f"utility_{key}"] = entry
    assert len(utilities) == 6
    for name, body in subheads(numbered(unit, 25)):
        key = slug(name)
        named[key] = {"id": key, "name": name, "kind": "alien_item", "effect_text": body,
                      "parameters": {"single_target_damage_multiplier": 1.25, "damage_type": "energy"} if key == "neural_beam" else {"regen_hp_fraction": .01, "regen_interval": 5},
                      "numeric_declarations": declared_numbers(body), "implementation_status": "catalog_only_missing_full_base_stat_definition",
                      "unresolved": ["Neural Beam base damage/interval and room Exposure amount not specified; Living Armor Armor value/Bio resistance/risk coefficient not specified. Do not invent complete balance stats."],
                      "source": provenance("UNITS_ITEMS_V0.1.md", f"25 {name}")}
    for key, value in armor.items(): named[f"armor_{key}"] = {**value, "kind": "armor", "implementation_status": "base_armor_catalog_engine_support_separate"}
    for key, value in consumables.items(): named[f"consumable_{key}"] = {**value, "kind": "consumable", "implementation_status": "catalog_complete_runner_must_report_supported_effect_ids"}
    traits = []
    trait_parameters = {"field_medic": {"medkit_multiplier": 1.20}, "calm": {"fear_resistance_delta": .15}, "mechanic": {"room_efficiency_delta": .08},
                        "keen_eye": {"detection_delta": .08, "scout_contribution_delta": .08}, "tough": {"hp_multiplier": 1.08}, "fast_learner": {"xp_multiplier": 1.10},
                        "scavenger": {"extra_common_roll_chance_delta": .10}, "steady_hands": {"accuracy_delta": .05}, "team_player": {"extraction_morale": 3},
                        "night_owl": {"night_efficiency_delta": .08}, "claustrophobic": {"long_silo_morale": -8, "extraction_morale": 3},
                        "reckless": {"damage_multiplier": 1.05, "damage_taken_multiplier": 1.10}, "fragile": {"hp_multiplier": .92}, "slow_recovery": {"clinic_duration_multiplier": 1.20},
                        "nervous": {"fear_psychic_resistance_delta": -.15}, "hoarder": {"cargo_delta": 1, "storage_efficiency_delta": -.05}, "short_temper": {},
                        "tech_illiterate": {"tech_interaction_multiplier": .85}, "paranoid": {"mimic_detection_delta": .15, "overcrowded_morale": -5},
                        "alien_touched": {"alien_efficiency_multiplier": 1.10, "exposure_multiplier": 1.20}, "veteran": {"damage_multiplier": 1.05, "accuracy_delta": .05, "death_morale_multiplier": 1.50},
                        "survivor": {"hp_threshold": .30, "low_hp_damage_taken_multiplier": .90, "clinic_duration_multiplier": 1.15},
                        "adrenaline_junkie": {"hard_extreme_attack_speed_multiplier": 1.08, "easy_morale_reward_delta": -5}, "pacifist": {"raider_damage_multiplier": .90}}
    for n, category in [(13, "positive"), (14, "negative"), (15, "mixed")]:
        for name, body in subheads(numbered(population, n)):
            key = slug(name); assert key in trait_parameters
            traits.append({"id": key, "name": name, "category": category, "parameters": trait_parameters[key], "effect_text": body,
                           "numeric_declarations": declared_numbers(body), "implementation_status": "catalog_adapter_parameters_runner_support_separate",
                           "source": provenance("POPULATION_TRAITS_V0.1.md", f"{n} {name}")})
    assert len(traits) == 24 and len({t["id"] for t in traits}) == 24
    perks = []
    for role, body in subheads(numbered(population, 17)):
        for m in re.finditer(r"^- ([^:\n]+): (.+)$", body, re.M):
            key = slug(m[1]); perks.append({"id": f"perk_{key}", "name": m[1], "role": "heavy" if role == "Heavy/Specialist" else slug(role),
                "effect_text": m[2], "numeric_declarations": declared_numbers(m[2]), "implementation_status": "catalog_only_perk_effect_support_not_implied",
                "source": provenance("POPULATION_TRAITS_V0.1.md", f"17 {role}")})
    assert len(perks) == 18
    perks.append({"id": "perk_steady_resolve", "name": "Steady Resolve", "role": "all", "parameters": {"resolve_check_delta": .05, "resolve_check_cap": .95}, "level": 40,
                  "implementation_status": "catalog_only_perk_effect_support_not_implied", "source": provenance("IMPLEMENTATION_BASELINE_V0.1.md", "4 XP và Training")})
    affixes = []
    for name, body in subheads(numbered(unit, 24), 3):
        affixes.append({"id": slug(name), "name": name, "effect_text": body, "numeric_declarations": declared_numbers(body),
                        "implementation_status": "catalog_only_corrosive_and_lightweight_effects_incomplete_in_source" if name in {"Corrosive", "Lightweight"} else "catalog_adapter_effect_support_separate",
                        "source": provenance("UNITS_ITEMS_V0.1.md", f"24 {name}")})
    assert len(affixes) == 5
    tiers = []
    for row in table_rows(numbered(unit, 14)):
        if row[0] == "Tier": continue
        vals = re.findall(r"\d+\.\d+", row[1])
        tiers.append({"id": slug(row[0]), "name": row[0], "budget_min": float(vals[0]) if vals else None,
                      "budget_max": float(vals[-1]) if vals else None, "effect_text": row[1]})
    assert len(tiers) == 7
    return {"named_items": named, "utilities": utilities, "traits": traits, "perks": perks, "affixes": affixes, "tiers": tiers,
            "catalog_coverage": {"named_weapon_variants": 6, "alien_item_examples": 2, "utilities": 6, "traits": 24, "perks_including_shared_level40": 19, "affixes": 5, "tiers": 7,
                                 "warning": "Catalog exported does not mean effects simulated. Incomplete source values remain null/text with unresolved notes; runner reports support separately."}}


def costs(text):
    result = {}
    for name, key in sorted(RESOURCE_NAMES.items(), key=lambda x: -len(x[0])):
        # Accept both human table conventions: '20 RD' and 'Components5'.
        m = re.search(rf"(?<!\w){re.escape(name)}\s*(\d+)(?!\d)|(?<!\d)(\d+)\s*{re.escape(name)}\b", text)
        if m:
            result[key] = int(m[1] or m[2])
    return result


def numbered(text, n):
    m = re.search(rf"^# {n}\. .*?$", text, re.M)
    if not m: raise ValueError(f"Missing numbered section {n}")
    end = re.search(r"^# \d+\. ", text[m.end():], re.M)
    return text[m.end():m.end()+end.start()] if end else text[m.end():]


def systems():
    buildings = read("SILO_BUILDINGS_V0.1.md")
    economy = read("ECONOMY_RESOURCES_V0.1.md")
    loot = read("LOOT_CRAFTING_V0.1.md")
    research_text = read("PROTOTYPE_RESEARCH_CATALOG_V0.1.md")
    progression_text = read("PROTOTYPE_PROGRESSION_V0.1.md")
    recovery = read("SURVIVOR_RECOVERY_V0.1.md")
    pvp_text = read("PVP_MATCHMAKING_PROTECTION_V0.1.md")
    implementation = read("IMPLEMENTATION_BASELINE_V0.1.md")
    sites_text = read("RESOURCE_SITES_V0.1.md")
    content = read("PROTOTYPE_CONTENT_PACK_V0.1.md")
    read("CAMPAIGN_CONTRACTS_V0.1.md")
    read("SILO_DEFENSE_SECURITY_V0.1.md")
    start = {slug(r[0]): number(r[1]) for r in table_rows(numbered(economy, 4)) if len(r) == 2 and r[0] != "Resource"}
    room_defs = {5: ("generator", ["power_output"]), 6: ("battery", ["reserve_puh"]),
                 7: ("water", ["water_per_hour", "power"]), 8: ("hydroponics", ["food_per_hour", "power"]),
                 9: ("living", ["beds", "power"]), 10: ("storage", ["capacity", "power"]),
                 11: ("workshop", ["craft_speed", "queue", "power"]), 12: ("clinic", ["beds", "heal_speed", "power"]),
                 13: ("training", ["slots", "training_speed", "power"]), 14: ("research_lab", ["research_speed", "queue", "power"]),
                 15: ("radio", ["radius_km", "intel_bonus_percent", "power"]), 16: ("security", ["capacity", "power"]),
                 17: ("armory", ["gear_capacity", "prep_bonus_percent", "power"]), 18: ("recycler", ["scrap_per_hour", "power"])}
    rooms = {}
    for n, (key, fields) in room_defs.items():
        block = numbered(buildings, n)
        levels = []
        for row in table_rows(block):
            if not re.fullmatch(r"L[1-5]", row[0]): continue
            levels.append({"level": int(row[0][1:]), **{f: number(v) for f, v in zip(fields, row[1:])}})
        build_time = re.search(r"Build\s+(\d+)\s*min", block)
        rooms[key] = {"id": key, "levels": levels, "build_cost": costs("; ".join(re.findall(r"^- (?:Scrap|Components|Chemicals).*", block, re.M))),
                      "build_minutes": int(build_time[1]) if build_time else None,
                      "source": provenance("SILO_BUILDINGS_V0.1.md", f"{n} Room table")}
        assert len(levels) == 5, (key, levels)
    recipes = []
    recipe_names = {"5 Supply": "supply", "C-9 Civilian Pistol": "pistol", "M-4 Service Rifle": "service_rifle"}
    recipe_block = numbered(loot, 13)
    for m in re.finditer(r"^## (.+)$", recipe_block, re.M):
        rest = recipe_block[m.end():]; end = re.search(r"^## ", rest, re.M)
        block = rest[:end.start()] if end else rest
        name = m[1].strip(); key = recipe_names.get(name, slug(name)); tm = re.search(r"^- (\d+) min", block, re.M)
        recipes.append({"id": key, "name": name, "inputs": costs(block), "outputs": {key: 5 if key == "supply" else 1},
                        "minutes": int(tm[1]), "unlock_text": " ".join(re.findall(r"^Requires.*", block, re.M)),
                        "source": provenance("LOOT_CRAFTING_V0.1.md", f"13 {name}")})
    research = []
    for row in table_rows(research_text):
        if not re.match(r"(?:SUR|EXP|COM|SEC|ENG|XEN|FAC)-\d{2} ", row[0]): continue
        aid, name = row[0].split(" ", 1); parts = [v.strip() for v in row[1].split(";")]
        ccl = int(parts[-2]); lab = int(re.search(r"L(\d+)", parts[-1])[1])
        research.append({"id": aid, "name": name, "tier": parts[0] if len(parts) == 3 else "special", "ccl": ccl, "lab_level": lab,
                         "prerequisites": [] if row[2] == "None" else re.findall(r"[A-Z]{3}-\d{2}", row[2]), "cost": costs(row[3]),
                         "minutes": minutes(row[4]), "effect_text": row[5], "source_text": row[6],
                         "source": provenance("PROTOTYPE_RESEARCH_CATALOG_V0.1.md", aid)})
    assert len(research) == 34 and len({r["id"] for r in research}) == 34
    ccl = []
    for row in table_rows(section(progression_text, r"^## 1\. CCL requirements")):
        if len(row) != 6 or not row[0].isdigit(): continue
        ccl.append({"level": int(row[0]), "cost": {"scrap": int(row[1]), "components": int(row[2]), "research_data": int(row[3])},
                    "minutes": minutes(row[4]), "prerequisite_text": row[5], "source": provenance("PROTOTYPE_PROGRESSION_V0.1.md", "1 CCL requirements")})
    assert [r["level"] for r in ccl] == list(range(2, 13))
    weights = {}
    for row in table_rows(section(implementation, r"^## 6\. Normal loot authoring")):
        if len(row) == 8 and row[0] != "Archetype":
            vals = [int(v) for v in row[1:]]; assert sum(vals) == 100
            weights[slug(row[0])] = dict(zip(["scrap", "components", "chemicals", "food_water", "data", "gear_consumable", "fragment"], vals))
    sites = {}
    for row in table_rows(numbered(economy, 20)):
        if len(row) != 2 or row[0] == "Site": continue
        m = re.match(r"(\d+)\s+(.+?)/h", row[1]); assert m, row
        resource = RESOURCE_NAMES.get(m[2], slug(m[2])); key = slug(row[0])
        sites[key] = {"id": key, "base_output": {resource: int(m[1])}, "source_text": row[1], "source": provenance("ECONOMY_RESOURCES_V0.1.md", "20 Resource Site Baseline Output")}
    treatment = []
    for row in table_rows(section(recovery, r"^## 3\. Base recovery và injury service")):
        if len(row) != 4 or row[0] == "Case": continue
        treatment.append({"id": slug(row[0]), "name": row[0], "minutes": number(row[1]), "chemicals": int(row[2]), "result_text": row[3]})
    caps = {}
    for row in table_rows(numbered(pvp_text, 11)):
        if len(row) == 4 and row[0].isdigit():
            caps[row[0]] = dict(zip(["scrap", "components", "chemicals"], [int(v) for v in row[1:]]))
    assert len(caps) == 5
    ledger = []
    for row in table_rows(content):
        if len(row) != 3: continue
        delta = row[1].replace("**", "").split("/"); balance = row[2].replace("**", "").split("/")
        if len(delta) == len(balance) == 3 and all(re.fullmatch(r"\s*[-+]?\d+\s*", v) for v in delta + balance):
            ledger.append({"id": slug(row[0]), "label": row[0], "delta": dict(zip(["scrap", "components", "chemicals"], map(int, delta))), "balance": dict(zip(["scrap", "components", "chemicals"], map(int, balance)))})
    return {"schema_version": 1, "economy": {"start": start, "consumption": {"food": 1, "water": 1.2}, "production": {"food": 10, "water": 12}, "offline_cap_hours": 8},
            "rooms": rooms, "recipes": recipes, "research": research, "ccl": ccl, "loot_weights": weights, "sites": sites,
            "treatment": treatment, "tutorial_ledger": ledger,
            "pvp": {"raid_charges": 3, "regen_hours": 4, "charge_cap": 3, "loss_caps": caps, "exposure_fraction": .10, "site_output_hours_cap": 2, "rolling_loss_hours": 24, "same_target_cooldown_hours": 24, "revenge_hours": 24, "max_incoming": 1},
            "assumptions": ["Text prerequisites/effects are exported as source text rather than falsely presented as fully machine-executable semantics.", "Loot weights are parsed from Implementation table; quantity bands Easy8–15/Medium12–20/Hard18–28/Extreme24–36 are documented uniform integers. Food/Water split50/50; one choice per roll.", "Tutorial balances include stored plus Return Inbox entitlement; not all entitlement is immediately spendable.", "Resource-site base_output excludes tier, staffing, integrity, ownership and control multipliers; systems engine must apply documented factors explicitly."]}


def emit(filename, data, check):
    data["sources"] = [SOURCES[k] for k in sorted(SOURCES)]
    encoded = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    path = OUT / filename
    if check:
        assert path.read_text(encoding="utf-8") == encoded, f"Stale export {path}"
    else:
        OUT.mkdir(parents=True, exist_ok=True)
        path.write_text(encoded, encoding="utf-8", newline="\n")


def validate_catalogs(combat_data, systems_data=None):
    for collection in [combat_data["weapons"], combat_data["armor"], combat_data["roles"], combat_data["enemies"]]:
        assert len({v["id"] for v in collection.values()}) == len(collection), "Duplicate stable IDs"
    for row in combat_data["weapons"].values():
        assert row["damage"] > 0 and row["interval"] > 0 and 0 <= row["accuracy"] <= 1 and 0 <= row["crit"] <= 1
        assert abs(row["damage"] / row["interval"] - row["base_dps_display"]) < .11, row["id"]
    for row in combat_data["enemies"].values():
        assert row["hp"] > 0 and row["damage"] > 0 and row["interval"] > 0 and row["armor"] >= 0
        assert set(row["resistances"]) == set(TYPES)
        assert all(-.25 <= n <= .80 for n in row["resistances"].values()), row["id"]
    for enc in combat_data["encounters"]:
        assert all(key in combat_data["enemies"] for key in enc["enemies"])
    for row in combat_data["roster"]:
        assert set(row["stats"]) == set(STATS) and all(1 <= n <= 10 for n in row["stats"].values())
        assert 32 <= sum(row["stats"].values()) <= 44
    if systems_data is not None:
        nodes = {r["id"]: r for r in systems_data["research"]}
        def depth(key, visited):
            assert key not in visited, ("Research cycle", key)
            return 1 + max([depth(p, visited | {key}) for p in nodes[key]["prerequisites"]], default=0)
        assert max(depth(key, set()) for key in nodes) <= 3
        for row in systems_data["recipes"]:
            assert row["minutes"] > 0 and all(v >= 0 for v in row["inputs"].values())
        assert systems_data["economy"]["start"]["scrap"] == 300


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--combat-only", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    combat_data = combat()
    validate_catalogs(combat_data)
    emit("combat.json", combat_data, args.check)
    if not args.combat_only:
        systems_data = systems()
        validate_catalogs(combat_data, systems_data)
        emit("systems.json", systems_data, args.check)
    print("Validated and " + ("checked" if args.check else "exported") + " documented catalogs")


if __name__ == "__main__":
    main()
