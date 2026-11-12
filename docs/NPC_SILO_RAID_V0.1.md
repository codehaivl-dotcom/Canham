# BURROW ZERO — NPC Silo Raid v0.1

**Status:** Prototype baseline  
**Purpose:** teach Silo infiltration before real PvP.

---

# 1. Role

NPC Silo Raid is the bridge between dungeon PvE and Player Silo PvP.

It teaches:

- scout hidden layout;
- route choice;
- alarm;
- disabling infrastructure;
- stealing limited loot;
- extracting under pressure.

---

# 2. Unlock

Prototype:

- first NPC Silo signal at CCL7;
- tutorial raid is curated;
- later NPC Silos are procedural within archetype.

---

# 3. Structure

Typical NPC Silo:

```
SURFACE ENTRY
→ SECURITY
→ RESIDENTIAL
├→ POWER
├→ CLINIC
├→ STORAGE
├→ ARMORY
└→ COMMAND
   ↓
DEEP SECTOR / VAULT
```

10–20 rooms.

Not all rooms are required.

---

# 4. Scout

Scout can reveal:

- known entrance;
- likely power wing;
- security density;
- population estimate;
- possible vault;
- alarm system type.

Never reveal full map.

---

# 5. Raid Objectives

Player chooses primary objective before deployment:

### Supply Raid
Steal common resources.

### Intelligence Raid
Reach data terminal.

### Armory Raid
Reach weapon storage.

### Rescue
Recover captive survivor.

### Command Breach
Reach Command Core.

### Deep Vault
High-risk optional objective.

Objective changes route and reward.

---

# 6. Alarm Meter

Alarm:

```
0 → 100
```

Sources:

- loud combat;
- failed hack;
- destroyed door;
- camera/sensor;
- alarm room;
- time spent after detection.

Thresholds:

| Alarm | Effect |
|---|---|
| 0–24 | unaware |
| 25–49 | guards reposition |
| 50–74 | reinforced rooms / doors lock |
| 75–99 | response squad activates |
| 100 | lockdown + extraction pressure |

---

# 7. Silent vs Loud

Some actions reduce Alarm:

- Engineer hack;
- Scout bypass;
- disable camera;
- power cut;
- alternate tunnel.

Loud options:

- explosive breach;
- Rocket;
- destroy turret;
- force door.

No stealth micro-game required.

This is strategic stealth, not crouch gameplay.

---

# 8. Infrastructure Actions

### Disable Power
Pros:
- turrets/cameras weaken;
- some doors fail open.

Cons:
- some security doors fail locked;
- dark hazard;
- enemy may use backup generator.

### Disable Alarm
Hard technical objective.

### Cut Ventilation
Can block Bio hazard or create alternate effect.

### Open Security Gate
Shortens extraction path.

---

# 9. Reinforcement

At Alarm 75+:

- one response wave can spawn;
- no infinite reinforcements.

At Alarm 100:

- elite defender or Warden may activate;
- extraction timer/pressure starts.

---

# 10. Extraction

Normal:

return to entry.

Alternate:

- emergency shaft;
- service tunnel;
- breached side exit.

Some exits require:
- power;
- Engineer;
- key;
- Breach Charge.

---

# 11. Loot

NPC Silo reward:

- Credits;
- Scrap/Components;
- Military Data;
- Combat Data small amount;
- gear;
- blueprint fragments;
- survivor/story item.

Best rewards usually deeper.

Player can extract after primary objective without full clear.

---

# 12. Failure

Failure can mean:

- squad wiped;
- objective failed;
- loot lost;
- captured/lost unit chance in special missions.

No permanent world punishment beyond expedition consequence.

---

# 13. Defender AI

NPC Silo defense uses:

- static guards;
- patrol room assignment abstractly;
- turrets;
- response squad;
- doors;
- sensors.

AI priorities follow enemy combat spec.

---

# 14. Procedural Packages

NPC Silo archetypes:

### Civilian Continuity
More population, fewer heavy defenses.

### Military Remnant
Armor/turret/armory.

### Research Silo
Robots, labs, alien samples.

### Raider Silo
Traps, irregular routes, aggressive response.

### Abandoned Silo
Environmental hazard + unknown occupants.

---

# 15. Tutorial NPC Raid

Curated sequence:

1. scout partial layout;
2. choose Security or Maintenance route;
3. hack camera;
4. fight guard room;
5. disable power;
6. loot Armory;
7. optional push to Command;
8. Alarm rises;
9. response squad appears;
10. extract.

Goal:

teach PvP language without risking another player.

---

# 16. Success Criteria

NPC Silo Raid works if:

- player understands Silo as dungeon;
- route/infrastructure choices matter;
- Alarm changes behavior;
- full clear is not mandatory;
- same systems can later drive async PvP.
