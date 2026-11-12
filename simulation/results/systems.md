# Noncombat systems simulation

Seed: 20261112
Summary: {'seed': 20261112, 'scenario_count': 104, 'passed': 104, 'failed': 0}
Data: exported_data

| Scenario | Category | Result |
|---|---|---|
| offline_partition_8h | economy | PASS |
| full_storage_consumption | economy | PASS |
| offline16h_reconnect | sites | PASS |
| blackout_manual_restart | power | PASS |
| normal_generator_repair | power | PASS |
| battery_to_emergency | power | PASS |
| bound_relief_no_repeat_mint | recovery | PASS |
| clinic_pause_resume | recovery | PASS |
| fatigue81_boundary | recovery | PASS |
| tutorial_restore | progression | PASS |
| tutorial_convert | progression | PASS |
| extended_slice_ccl5_research | progression | PASS |
| pve_gate_reachability | progression | PASS |
| ccl_affordability_2 | progression | PASS |
| ccl_affordability_3 | progression | PASS |
| ccl_affordability_4 | progression | PASS |
| ccl_affordability_5 | progression | PASS |
| ccl_affordability_6 | progression | PASS |
| ccl_affordability_7 | progression | PASS |
| ccl_affordability_8 | progression | PASS |
| ccl_affordability_9 | progression | PASS |
| ccl_affordability_10 | progression | PASS |
| ccl_affordability_11 | progression | PASS |
| ccl_affordability_12 | progression | PASS |
| research_dependency_dag | research | PASS |
| research_SUR-01 | research | PASS |
| research_SUR-02 | research | PASS |
| research_SUR-03 | research | PASS |
| research_SUR-04 | research | PASS |
| research_SUR-05 | research | PASS |
| research_EXP-01 | research | PASS |
| research_EXP-02 | research | PASS |
| research_EXP-03 | research | PASS |
| research_EXP-04 | research | PASS |
| research_EXP-05 | research | PASS |
| research_COM-01 | research | PASS |
| research_COM-02 | research | PASS |
| research_COM-03 | research | PASS |
| research_COM-04 | research | PASS |
| research_COM-05 | research | PASS |
| research_SEC-01 | research | PASS |
| research_SEC-02 | research | PASS |
| research_SEC-03 | research | PASS |
| research_SEC-04 | research | PASS |
| research_SEC-05 | research | PASS |
| research_ENG-01 | research | PASS |
| research_ENG-02 | research | PASS |
| research_ENG-03 | research | PASS |
| research_ENG-04 | research | PASS |
| research_ENG-05 | research | PASS |
| research_XEN-01 | research | PASS |
| research_XEN-02 | research | PASS |
| research_XEN-03 | research | PASS |
| research_XEN-04 | research | PASS |
| research_XEN-05 | research | PASS |
| research_FAC-01 | research | PASS |
| research_FAC-02 | research | PASS |
| research_FAC-03 | research | PASS |
| research_FAC-04 | research | PASS |
| noncombat_character_traits | characters | PASS |
| craft_salvage_material_conservation | economy | PASS |
| recipe_source_sink_supply | crafting | PASS |
| recipe_source_sink_medkit | crafting | PASS |
| recipe_source_sink_frag_grenade | crafting | PASS |
| recipe_source_sink_emp_grenade | crafting | PASS |
| recipe_source_sink_pistol | crafting | PASS |
| recipe_source_sink_service_rifle | crafting | PASS |
| recipe_source_sink_combat_armor | crafting | PASS |
| recipe_source_sink_revival_injector | crafting | PASS |
| npc_market_craft_sell_buy_salvage | economy | PASS |
| site_tier_worker_integrity_ownership_hide | sites | PASS |
| site_output_sweep_alien_crater | sites | PASS |
| site_output_sweep_chemical_plant | sites | PASS |
| site_output_sweep_data_center | sites | PASS |
| site_output_sweep_military_salvage | sites | PASS |
| site_output_sweep_scrapyard | sites | PASS |
| site_output_sweep_solar_farm | sites | PASS |
| site_output_sweep_uranium_mine | sites | PASS |
| site_output_sweep_water_facility | sites | PASS |
| defense_capacity_enumeration | defense | PASS |
| seeded_weighted_loot_and_pity | loot | PASS |
| loot_distribution_depot | loot | PASS |
| loot_distribution_hospital | loot | PASS |
| loot_distribution_house | loot | PASS |
| loot_distribution_lab | loot | PASS |
| loot_distribution_metro | loot | PASS |
| loot_distribution_npc_silo | loot | PASS |
| loot_distribution_warehouse | loot | PASS |
| treatment_routine_hp_recovery | recovery | PASS |
| treatment_tutorial_bruising | recovery | PASS |
| treatment_fracture | recovery | PASS |
| treatment_concussion | recovery | PASS |
| treatment_burn | recovery | PASS |
| treatment_infection | recovery | PASS |
| treatment_trauma | recovery | PASS |
| treatment_recovered_body | recovery | PASS |
| normal_five_card_cache_contract | loot | PASS |
| house_authored_cargo | loot | PASS |
| reward_failed_retry_replay_cache_claim | persistence | PASS |
| cross_asset_concurrent_reservation_replay | pvp | PASS |
| rolling24h_exact_boundary | pvp | PASS |
| reservation_expiry_failed_extraction | pvp | PASS |
| pvp_eligibility_matrix | pvp | PASS |
| beacon_claim_interruption_refund | sites | PASS |

## Limits

- Noncombat reference model; not the game runtime, network/server, engine or manual playtest.
- Tutorial ledger computes authored entitlement and affordability, not a timed optimal-policy playthrough or UI inbox interaction.
- Loot uses exported category weights,Easy1–2 rolls/clear,Easy8–15 quantities and documented3successful-clear pity; eligible gear pool is a four-item baseline, not all research/CCL loot filters.
- Craft/salvage tests use documented50% maximum material recovery; NPC craft/sell and buy/salvage/sell cycles run for priced recipes; arbitrary full multi-recipe conversion cycles are not proven absent.
- PvP model covers consent, locks, exposure, rolling theft, charges, shields and expiry; not ranking/match quality, capture combat or collusion enforcement.
- Power model runs life-support priority and battery/emergency/restart, not a full arbitrary room-grid topology solver.
- Economy assumes staffed life support at efficiency1 and full-integrity rooms unless overridden; detailed hunger-derived nonessential penalties and relief pending-mission eligibility are not modeled.
- Recovery models rest and one powered treatment with pause/resume; parallel clinic queue, full roster/body/capture state machine belong to combat/runtime validation.
