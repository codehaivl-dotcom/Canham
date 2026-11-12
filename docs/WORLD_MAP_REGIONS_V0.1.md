# BURROW ZERO — World Map, Regions & Refresh v0.1

**Status:** Prototype design baseline

---

# 1. Purpose

World Map is the persistent context connecting:

- Silo;
- PvE targets;
- resource sites;
- factions;
- NPC Silos;
- player Silos;
- bosses;
- temporary events.

It must feel like a place, not a random mission menu.

---

# 2. Region Structure

Prototype world is divided into Regions.

Each Region contains:

- 1–3 major landmarks;
- 6–12 persistent nodes;
- temporary nodes;
- routes;
- hazards;
- faction influence;
- player/NPC Silo signatures.

Player starts in one local Region.

---

# 3. Region Scale

Prototype:

- local region radius: ~30 km;
- extended scan: up to 60 km;
- inter-region travel unlocks later.

Map is abstracted, not real GPS.

Distance affects:

- travel time;
- Supply;
- event chance;
- scouting quality.

---

# 4. Node Types

### Persistent
- named Hospital;
- Military Depot;
- Research Lab;
- NPC Silo;
- major Resource Site;
- landmark;
- faction hub.

### Semi-persistent
- Warehouse;
- House cluster;
- local tunnel;
- minor resource site.

### Temporary
- distress signal;
- crash;
- convoy;
- anomaly;
- rare cache;
- world event.

---

# 5. Fog of War

Map starts obscured.

Discovery sources:

- Radio Scan;
- expedition adjacency;
- story;
- faction intel;
- Scout trait;
- alliance intel later.

Fog reveals nodes, not complete contents.

---

# 6. Spawn Budget

Each Region maintains target budget by category.

Example local region:

- 2–4 Civilian;
- 2–3 Industrial;
- 1–2 Medical;
- 1–2 Military/Research;
- 1 Resource Site;
- 0–2 temporary events;
- 0–1 rare/alien event.

Generator prevents all targets from being same type.

---

# 7. Refresh Rules

Persistent nodes:
- do not vanish;
- can change state; mandatory boss/key contracts repeat6h with guaranteed progression token, first access immediate; see PROTOTYPE_PROGRESSION_V0.1.md. Partial extraction does not reroll an uncleared instance; remaining rooms/loot persist. Completed room loot cannot be farmed twice in same version.

Semi-persistent:
- refresh after successful objective+extract in6h for prototype House/Warehouse; private instance contents immutable until settlement; Perimeter comeback node refresh immediate;
- may return with new threat package.

Temporary:
- expire after 2–8h;
- never expire while squad is traveling/inside.

---

# 8. Cleared Node Evolution

A cleared location can become:

- scavenged;
- reoccupied;
- contaminated;
- faction-controlled;
- resource opportunity;
- story node.

This avoids exact “reset dungeon” feeling.

---

# 9. Region Threat Level

Each Region has:

```
REGION THREAT
1–5
```

Affected by:

- story progress;
- alien activity;
- player/faction control;
- world event.

Threat modifies node packages, not all enemy stats blindly.

---

# 10. Faction Influence

Region displays approximate influence:

- Continuity;
- Free Settlements;
- Earthborn;
- Ascendants;
- Archivists;
- hostile/unknown.

Influence changes:

- contracts;
- stores;
- patrols;
- target control;
- event probabilities.

---

# 11. Player Silo Discovery

Player Silos are not visible globally.

They become discoverable by:

- PvP matchmaking;
- signal scan;
- high Noise;
- resource contest;
- revenge;
- alliance intel.

Map icon reveals approximate area, not exact private metadata.

---

# 12. NPC Silo Discovery

NPC Silos can be:

- story-locked;
- persistent;
- rare signal;
- faction-controlled.

They teach raid systems and provide regional lore.

---

# 13. World Boss

World boss nodes:

- temporary or seasonal;
- region-wide signal;
- high preparation;
- solo/squad-instance PvE initially;
- alliance cooperative layer later.

No real-time massive raid required for MVP.

---

# 14. Routes

Travel follows abstract route graph.

Route modifiers:

- safe;
- exposed;
- contaminated;
- blocked;
- faction-controlled.

Player may choose:

- shorter risky route;
- longer safer route.

Keep choice simple: max 2–3 route options.

---

# 15. Region Unlock

New Region requires one or more:

- Radio range;
- story milestone;
- route restoration;
- faction access;
- boss clear;
- CCL.

Opening a region is a major progression moment.

---

# 16. World Events

Examples:

- signal storm;
- alien migration;
- military convoy;
- plague;
- blackout;
- faction conflict;
- resource bloom;
- crashed object.

Events modify node state for hours/days.

---

# 17. Map Readability

At a glance player sees:

- known vs unknown;
- threat band;
- distance;
- location family;
- temporary timer;
- faction ownership;
- contested status.

Do not show exact loot/enemy.

---

# 18. Anti-Chore

No requirement to clear whole map.

Map always has:

- a few relevant targets;
- not dozens of flashing timers.

Temporary event count capped.

No “red notification everywhere”.

---

# 19. Success Criteria

World Map succeeds if:

1. player remembers locations;
2. target choice reflects need;
3. world state changes;
4. PvP/resource conflict feels geographically grounded;
5. map is readable without becoming 4X clutter.
