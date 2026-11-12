# BURROW ZERO — UI/UX Navigation v0.1

**Status:** Product navigation baseline  
**Languages:** Vietnamese + English  
**Art:** simple AI-first low-poly.

---

# 1. UX Principle

The player should be at most **2 taps/clicks** away from:

- Silo;
- Squad/Survivors;
- World Map;
- current mission;
- inventory;
- research.

Avoid nested mobile-4X menu trees.

---

# 2. Primary Navigation

Persistent top/side navigation:

1. **Silo**
2. **Survivors**
3. **World**
4. **Missions**
5. **Research**
6. **Inventory**

Secondary:
- Alliance;
- Faction;
- Season;
- Settings.

Secondary features appear only after unlock.

---

# 3. Home — Silo

Main screen:

- cutaway Silo;
- Power/Water/Food/Scrap top bar;
- rooms clickable;
- survivor visible;
- Build;
- Staff;
- Upgrade;
- Explore/World shortcut.

No separate "base management spreadsheet" required for basic use.

---

# 4. Room Interaction

Click room opens compact panel:

- room name/level;
- output/load;
- assigned workers;
- upgrade;
- priority/on-off;
- damage/status.

Advanced details under expandable section.

---

# 5. Survivors

Roster screen:

- card/portrait list;
- filter role/job/status;
- selected survivor 3D preview;
- stats;
- role;
- profession;
- trait;
- history;
- gear slots.

Tabs:
- Overview;
- Gear;
- Traits;
- History.

No rarity star rating for survivors.

---

# 6. Squad Builder

Shows:

- 3–5 formation slots;
- role;
- HP/condition;
- weapon;
- consumables;
- readiness warning.

Warnings:

- no healer;
- heavy Supply;
- Bio risk;
- injured survivor.

Warnings are advice, not hard block.

---

# 7. World Map

Map screen contains:

- current Silo;
- known nodes;
- unknown signals;
- Resource Sites;
- faction ownership;
- temporary event timers.

Select node → target card.

Target card:
- distance;
- size;
- threat;
- Intel confidence;
- likely loot;
- Scout;
- Prepare.

---

# 8. Mission Preparation

Layout:

Left:
target card.

Center:
squad.

Right:
consumables/loadout.

Bottom:
Supply cost;
survival estimate;
Deploy.

No hidden submenus needed to change one weapon.

---

# 9. Expedition HUD

Minimal:

- survivor portraits + HP;
- cargo;
- room/route;
- Alarm when relevant;
- consumable quick actions;
- Map;
- Extract.

Do not display full RPG stat sheet during combat.

---

# 10. Combat HUD

Core actions only:

- focus target;
- consumable;
- ability if enabled;
- reposition limited;
- retreat/extract.

Damage types communicated with VFX/icons.

---

# 11. Post-Run

Sequence:

1. outcome;
2. survivor injuries/death;
3. recovered loot;
4. cache reveal;
5. XP/Bestiary/Blueprint/Contract progress;
6. Return to Silo.

"Skip reveal animation" option.

---

# 12. Inventory

Categories:

- Weapon;
- Armor;
- Utility;
- Consumable;
- Materials;
- Key/Research.

Filters:
- tier;
- damage type;
- equipped;
- craftable.

No giant unsorted item grid.

---

# 13. Research

Tree grouped by:

- Survival;
- Combat;
- Expedition;
- Security;
- Alien;
- Faction.

Show:
- requirement;
- effect;
- source hint.

No fake branching where one path is always objectively best.

---

# 14. Notification System

Only high-value alerts:

- water critical;
- squad returned;
- temporary target expiring soon;
- site attacked;
- research complete;
- survivor critical.

No red-dot spam.

Notification inbox can collect low-priority events.

---

# 15. Localization UX

VI/EN first-class.

Rules:

- flexible button width;
- no text baked in art;
- 30% expansion room;
- full Vietnamese diacritics;
- avoid abbreviations dependent on English.

---

# 16. Accessibility Baseline

- UI scale;
- text scale;
- colorblind-safe icon redundancy;
- reduced camera motion;
- reduced flash;
- subtitles;
- master/music/SFX sliders;
- hold/tap options;
- animation skip for cache opening.

---

# 17. Controller / Mouse / Touch

UI should be navigable by:

- mouse;
- touch;
- controller focus.

Large primary hit targets.

No tiny drag interactions required for core systems.

---

# 18. Back Behavior

Every screen:
- one predictable Back action;
- never exits mission accidentally.

Destructive actions require confirmation:
- abandon mission;
- salvage rare item;
- dismiss survivor if ever supported.

---

# 19. UX Success Criteria

Player should:

- know where to go next;
- understand resource warnings;
- equip squad quickly;
- enter mission with few steps;
- return home without menu fatigue.
