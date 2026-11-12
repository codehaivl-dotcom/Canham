# Combat Simulation Results

Mode: quick; 1,800 battles; seed 20261112; 5 seeds/primary cell.

**Headless model results, not runtime gameplay QA or final balance approval.**

Health: **CONCERNS**. 51 target/diagnostic deviations. Unmodified design baselines; no auto-tuning to force a pass.

## Balanced squad, level10, medium

| Encounter | Squad | Win% | 95% CI | Win TTK p50 | Win HP loss | Downs/run | Medkits/run |
|---|---:|---:|---|---:|---:|---:|---:|
| swarm | 3 | 100.0 | [0.565509, 1.0] | 5.2 | 0.10949 | 0 | 0 |
| swarm | 4 | 100.0 | [0.565509, 1.0] | 3.9 | 0.06889 | 0 | 0 |
| swarm | 5 | 100.0 | [0.565509, 1.0] | 2.7 | 0.04747 | 0 | 0 |
| brute_swarm | 3 | 100.0 | [0.565509, 1.0] | 9.6 | 0.13232 | 0 | 0.4 |
| brute_swarm | 4 | 100.0 | [0.565509, 1.0] | 6.8 | 0.10523 | 0 | 0 |
| brute_swarm | 5 | 100.0 | [0.565509, 1.0] | 5.6 | 0.06636 | 0 | 0 |
| carrier_swarm | 3 | 100.0 | [0.565509, 1.0] | 11.7 | 0.12913 | 0 | 0.4 |
| carrier_swarm | 4 | 100.0 | [0.565509, 1.0] | 9.0 | 0.11106 | 0 | 0 |
| carrier_swarm | 5 | 100.0 | [0.565509, 1.0] | 7.2 | 0.0582 | 0 | 0 |
| raider_basic | 3 | 100.0 | [0.565509, 1.0] | 8.4 | 0.07697 | 0 | 0.8 |
| raider_basic | 4 | 100.0 | [0.565509, 1.0] | 6.5 | 0.12608 | 0 | 0 |
| raider_basic | 5 | 100.0 | [0.565509, 1.0] | 5.0 | 0.08218 | 0 | 0 |
| marksman_room | 3 | 100.0 | [0.565509, 1.0] | 6.5 | 0.11903 | 0 | 0.2 |
| marksman_room | 4 | 100.0 | [0.565509, 1.0] | 5.2 | 0.08737 | 0 | 0 |
| marksman_room | 5 | 100.0 | [0.565509, 1.0] | 3.9 | 0.04467 | 0 | 0 |
| tech_raider_room | 3 | 100.0 | [0.565509, 1.0] | 11.7 | 0.13525 | 0 | 1 |
| tech_raider_room | 4 | 100.0 | [0.565509, 1.0] | 8.4 | 0.05201 | 0 | 1 |
| tech_raider_room | 5 | 100.0 | [0.565509, 1.0] | 7.2 | 0.08309 | 0 | 0.4 |
| security_pair | 3 | 100.0 | [0.565509, 1.0] | 10.4 | 0.17544 | 0 | 0 |
| security_pair | 4 | 100.0 | [0.565509, 1.0] | 8.4 | 0.12166 | 0 | 0 |
| security_pair | 5 | 100.0 | [0.565509, 1.0] | 6.4 | 0.07121 | 0 | 0 |
| repair_room | 3 | 100.0 | [0.565509, 1.0] | 13.2 | 0.06214 | 0 | 1 |
| repair_room | 4 | 100.0 | [0.565509, 1.0] | 9.6 | 0.13825 | 0 | 0 |
| repair_room | 5 | 100.0 | [0.565509, 1.0] | 7.5 | 0.09635 | 0 | 0 |
| crystal_stalker | 3 | 100.0 | [0.565509, 1.0] | 8.4 | 0.18927 | 0 | 0 |
| crystal_stalker | 4 | 100.0 | [0.565509, 1.0] | 7.2 | 0.12147 | 0 | 0 |
| crystal_stalker | 5 | 100.0 | [0.565509, 1.0] | 5.4 | 0.07986 | 0 | 0 |
| spore_hounds | 3 | 100.0 | [0.565509, 1.0] | 10.8 | 0.25073 | 0 | 1 |
| spore_hounds | 4 | 100.0 | [0.565509, 1.0] | 8.4 | 0.12625 | 0 | 1 |
| spore_hounds | 5 | 100.0 | [0.565509, 1.0] | 7.5 | 0.07439 | 0 | 1 |
| void_stalkers | 3 | 100.0 | [0.565509, 1.0] | 10.2 | 0.14089 | 0 | 1 |
| void_stalkers | 4 | 100.0 | [0.565509, 1.0] | 7.2 | 0.12952 | 0 | 0.4 |
| void_stalkers | 5 | 100.0 | [0.565509, 1.0] | 6.3 | 0.1072 | 0 | 0.2 |
| solo_alpha_brute | 3 | 100.0 | [0.565509, 1.0] | 17.9 | 0.22216 | 0 | 1.4 |
| solo_alpha_brute | 4 | 100.0 | [0.565509, 1.0] | 12.8 | 0.15675 | 0 | 1 |
| solo_alpha_brute | 5 | 100.0 | [0.565509, 1.0] | 10.4 | 0.13425 | 0 | 0.6 |
| solo_warden_mech | 3 | 100.0 | [0.565509, 1.0] | 41.4 | 0.3991 | 1 | 2 |
| solo_warden_mech | 4 | 100.0 | [0.565509, 1.0] | 28.6 | 0.18847 | 0 | 2 |
| solo_warden_mech | 5 | 100.0 | [0.565509, 1.0] | 22.1 | 0.07974 | 0 | 1.8 |
| solo_phase_hunter | 3 | 100.0 | [0.565509, 1.0] | 12.4 | 0.23702 | 0.2 | 1 |
| solo_phase_hunter | 4 | 100.0 | [0.565509, 1.0] | 8.1 | 0.08931 | 0 | 1 |
| solo_phase_hunter | 5 | 100.0 | [0.565509, 1.0] | 6.5 | 0.08147 | 0 | 0.6 |
| solo_hive_mother | 3 | 0.0 | [-0.0, 0.434491] | None | None | 3 | 2 |
| solo_hive_mother | 4 | 100.0 | [0.565509, 1.0] | 45.0 | 0.77861 | 1.2 | 2 |
| solo_hive_mother | 5 | 100.0 | [0.565509, 1.0] | 34.8 | 0.39466 | 0.4 | 2 |
| solo_war_machine_a_17 | 3 | 0.0 | [-0.0, 0.434491] | None | None | 3 | 2 |
| solo_war_machine_a_17 | 4 | 0.0 | [-0.0, 0.434491] | None | None | 4 | 2 |
| solo_war_machine_a_17 | 5 | 0.0 | [-0.0, 0.434491] | None | None | 5 | 2 |
| solo_fallen_visitor | 3 | 0.0 | [-0.0, 0.434491] | None | None | 3 | 2 |
| solo_fallen_visitor | 4 | 0.0 | [-0.0, 0.434491] | None | None | 4 | 2 |
| solo_fallen_visitor | 5 | 60.0 | [0.23072, 0.882382] | 77.5 | 0.83641 | 3.6 | 2 |

Win TTK/HP metrics are conditional on victories; all-duration/win rate include failures in CSV/JSON. Small samples have wide confidence intervals.

## Authored room chains (no reset between rooms)

| Mission | Win% | Win duration p50 | HP loss mean |
|---|---:|---:|---:|
| house | 100.0 | 2.3 | 0.014 |
| warehouse | 100.0 | 4.4 | 0.043 |
| hospital | 100.0 | 10.2 | 0.131 |

## Model limitations

- all trait/perk/relationship effects
- all Alien/Artifact item mechanics
- visual telegraph reactions/navigation
- player learning/manual focus timings
- whole-campaign time-to-complete
- actual client/backend crash/network behavior

See combat_summary.json for source hashes, complete findings and coverage; combat_matrix.csv for every cell; combat_traces.json for17 replayable event logs.
