# BURROW ZERO — Design & Production Plan v0.4

> **Deep Below. Far Beyond.**

**Status:** Pre-production design  
**Initial languages:** Vietnamese + English  
**Art:** AI-first simple low-poly 3D, panda survivor mascot  
**Combat Simulation:** NOT STARTED intentionally

Canonical conflict resolution:

[CANONICAL_RULES_V0.1.md](./CANONICAL_RULES_V0.1.md)

---

# 1. Product Core — LOCKED

BURROW ZERO is:

- underground Silo management;
- named panda survivors;
- room-by-room PvE expedition;
- imperfect intel;
- preparation-focused combat;
- extraction/retreat tension;
- loot/crafting/research;
- Silo excavation;
- bosses;
- persistent World Map;
- Resource Site economy;
- optional asynchronous PvP;
- factions;
- alliance/coalition;
- seasonal/endgame PvE and PvP.

PvE must remain a complete game path.

PvP adds:
- rivalry;
- prestige;
- alternate progression;
- contested economy.

---

# 2. Canonical Progression

CCL:

```
1  Survival
2  Surface Gate + Squad 3
3  Radio/Scout + Workshop
4  Clinic/Training
5  Research + Squad 4
6  Security/Armory + Resource Sites
7  NPC Silo / Network
8  Player PvP + Squad 5
9  Prototype Tech
10 Alien Tech
11 Coalition
12 Endgame / Surface Return
```

Standard squad cap:

```
3 → 4 → 5
```

Standard max:

**5**

---

# 3. Core Design Specs — COMPLETE BASELINE

## Foundation

- [GAME_DESIGN_V0.1.md](./GAME_DESIGN_V0.1.md)
- [CANONICAL_RULES_V0.1.md](./CANONICAL_RULES_V0.1.md)
- [BRAND_LOCALIZATION_V0.1.md](./BRAND_LOCALIZATION_V0.1.md)

## Silo / Economy

- [ECONOMY_RESOURCES_V0.1.md](./ECONOMY_RESOURCES_V0.1.md)
- [SILO_BUILDINGS_V0.1.md](./SILO_BUILDINGS_V0.1.md)
- [SILO_EXPANSION_V0.1.md](./SILO_EXPANSION_V0.1.md)
- [SILO_DEFENSE_SECURITY_V0.1.md](./SILO_DEFENSE_SECURITY_V0.1.md)
- [RESEARCH_TECH_TREE_V0.1.md](./RESEARCH_TECH_TREE_V0.1.md)

## Survivors / Combat

- [UNITS_ITEMS_V0.1.md](./UNITS_ITEMS_V0.1.md)
- [POPULATION_TRAITS_V0.1.md](./POPULATION_TRAITS_V0.1.md)
- [ENEMIES_RESISTANCES_V0.1.md](./ENEMIES_RESISTANCES_V0.1.md)

## Exploration / Loot

- [WORLD_TARGETS_V0.1.md](./WORLD_TARGETS_V0.1.md)
- [SCOUT_TRAVEL_CONTRACTS_V0.1.md](./SCOUT_TRAVEL_CONTRACTS_V0.1.md)
- [LOOT_CRAFTING_V0.1.md](./LOOT_CRAFTING_V0.1.md)
- [REWARD_REVEAL_CACHE_V0.1.md](./REWARD_REVEAL_CACHE_V0.1.md)

## World / Strategy

- [WORLD_MAP_REGIONS_V0.1.md](./WORLD_MAP_REGIONS_V0.1.md)
- [RESOURCE_SITES_V0.1.md](./RESOURCE_SITES_V0.1.md)
- [FACTIONS_V0.1.md](./FACTIONS_V0.1.md)
- [ALLIANCE_COALITION_V0.1.md](./ALLIANCE_COALITION_V0.1.md)
- [MIMIC_INFILTRATION_V0.1.md](./MIMIC_INFILTRATION_V0.1.md)

## Raids / PvP

- [NPC_SILO_RAID_V0.1.md](./NPC_SILO_RAID_V0.1.md)
- [PLAYER_PVP_RAID_V0.1.md](./PLAYER_PVP_RAID_V0.1.md)
- [PVP_MATCHMAKING_PROTECTION_V0.1.md](./PVP_MATCHMAKING_PROTECTION_V0.1.md)

## Narrative / Onboarding / Live

- [STORY_CAMPAIGN_V0.1.md](./STORY_CAMPAIGN_V0.1.md)
- [TUTORIAL_FIRST_2H_V0.1.md](./TUTORIAL_FIRST_2H_V0.1.md)
- [SEASONS_ENDGAME_V0.1.md](./SEASONS_ENDGAME_V0.1.md)

## Product / Presentation

- [UI_UX_NAVIGATION_V0.1.md](./UI_UX_NAVIGATION_V0.1.md)
- [ART_PRODUCTION_V0.1.md](./ART_PRODUCTION_V0.1.md)
- [VISUAL_SCREEN_TARGETS_V0.1.md](./VISUAL_SCREEN_TARGETS_V0.1.md)
- [SOUND_MUSIC_V0.1.md](./SOUND_MUSIC_V0.1.md)
- [SOCIAL_PLAYER_SAFETY_V0.1.md](./SOCIAL_PLAYER_SAFETY_V0.1.md)

---

# 4. Research / Reference Docs

These are supporting references, not higher-priority gameplay rules:

- [MARKET_RESEARCH_V0.1.md](./MARKET_RESEARCH_V0.1.md)
- [LESSONS_APPLIED_V0.1.md](./LESSONS_APPLIED_V0.1.md)

---

# 5. Current Production Sequence

Recommended:

```
LOCK CANONICAL DOCS ✓
      ↓
ART BLOCKOUT / CORE SCREENS
      ↓
SILO HOME PROTOTYPE
      ↓
EXPEDITION ROOM PROTOTYPE
      ↓
COMBAT IMPLEMENTATION
      ↓
COMBAT SIMULATION / TUNING
      ↓
LOOT + RETURN LOOP
      ↓
FIRST 2H VERTICAL SLICE
      ↓
NPC SILO RAID
      ↓
WORLD MAP / RESOURCE SITE
      ↓
PLAYER PVP
      ↓
FACTION / ALLIANCE / SEASON
```

Do not build full persistent MMO backend before the base + expedition + extraction loop is proven.

---

# 6. Vertical Slice Target

Vertical slice should demonstrate:

1. panda Silo home;
2. Power/Water/Food;
3. 6+ room types;
4. survivor jobs;
5. squad 3 → 4 progression;
6. House/Warehouse/Hospital or Research target;
7. Scout;
8. mission preparation;
9. room exploration;
10. readable combat;
11. injury/death/revive pressure;
12. extraction;
13. cache/card reward;
14. crafting/research;
15. Silo sector clear/restore;
16. NPC Silo signal hook.

Player PvP does not need to be in first vertical slice.

---

# 7. Art Production Priorities

First assets/screens:

1. Panda base rig/body;
2. Vanguard/Medic/Engineer role modules;
3. Silo room kit;
4. Main Silo screen;
5. Expedition room kit;
6. Dungeon Exploration screen;
7. Combat screen;
8. Mission Prep;
9. World Map;
10. Cache Return.

Use [ART_PRODUCTION_V0.1.md](./ART_PRODUCTION_V0.1.md) as production ceiling.

---

# 8. Intentionally Open Decisions

Do not let implementation agents silently decide these:

- exact active combat control density;
- exact CCL upgrade costs;
- final combat/economy tuning;
- final drop probabilities;
- monetization/pricing;
- launch platform order;
- technical backend/save topology.

When one is decided, update CANONICAL_RULES first.

---

# 9. Explicitly Not Done Yet

## Combat Simulation

Not started.

Future output should test:

- TTK;
- HP loss;
- squad 3/4/5;
- AOE;
- healing;
- resistance;
- wrong-loadout penalty;
- bosses.

Current numeric combat values remain prototype baselines.

---

# 10. Change-Control Rule

For future design work:

1. edit dedicated system spec;
2. if it changes a cross-system rule, update CANONICAL_RULES;
3. update this plan only if roadmap/status changes;
4. run audit after major milestone;
5. do not append contradictory rules to the bottom of old files.

This rule exists specifically to prevent multi-turn design drift.
