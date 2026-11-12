# BURROW ZERO — Player PvP Silo Raid v0.1

**Status:** Direction baseline  
**Model:** Asynchronous PvP

---

# 1. Core Principle

A player's Silo is both:

- home base;
- dungeon another player may infiltrate.

PvP must use the same gameplay language as PvE.

No separate auto-battle mode.

---

# 2. Unlock

Prototype:

- PvP unlock at CCL8;
- player completes at least one NPC Silo Raid first;
- first PvP attacks use low-stake objectives.

---

# 3. Attack Flow

```
FIND TARGET
→ SCOUT
→ CHOOSE RAID OBJECTIVE
→ PREPARE SQUAD
→ INFILTRATE
→ REVEAL ROOMS
→ COMPLETE / ABANDON
→ EXTRACT
→ RESOLVE REWARDS
```

---

# 4. Defender Representation

Defender is offline/asynchronous.

Their real:

- room layout;
- defense assignment;
- doors;
- turrets;
- security rooms;
- selected defense squad;
- power topology;

are converted into raid state.

Defender cannot lose permanent building ownership.

---

# 5. Raid Objectives

### Resource Raid
Take exposed resources.

### Intelligence Raid
Steal Combat Data / scouting intel.

### Sabotage
Temporarily reduce room output.

### Blueprint Hunt
Reach protected research/armory objective.

### Command Assault
High prestige, low raw loot.

Not every objective is available against every target.

---

# 6. Layout Reveal

Initial scout:

- entry;
- 1–3 known rooms;
- approximate Command direction;
- security estimate.

During raid:

- adjacent rooms reveal progressively;
- hidden connection may remain unknown;
- decoy/false reading can exist later.

No full Clash-style overhead reveal.

---

# 7. Alarm

Uses NPC Silo Alarm model.

Player defenses can modify:

- Alarm gain;
- reinforcement threshold;
- response squad;
- door lockdown.

---

# 8. Defense Squad

Defender assigns up to:

- 3 defenders early PvP;
- 4 mid;
- 5 late.

They are AI-controlled.

Defense squad injury does not create permanent death from offline raid in baseline.

Reason:

asynchronous punishment must not destroy named survivor attachment while player sleeps.

Instead:

- temporary Injury/Fatigue;
- Clinic time;
- defense cooldown.

---

# 9. Permanent Death Rule in PvP

Attacker's deployed units:

- can die under normal expedition rules.

Defender offline units:

- cannot permanently die from normal async defense.

Special opt-in hardcore/event modes may change this later.

---

# 10. Exposed Resources

Only a protected fraction is raidable.

Prototype:

```
Exposed Pool =
10% of eligible common resources
+ uncollected Resource Site intel/loot
```

Attacker can extract only a portion.

Strategic materials:

- strongly protected;
- hard daily theft cap;
- some non-stealable.

---

# 11. Defender Loss

Defender may suffer:

- small resource loss;
- room temporary damage;
- defense squad Injury/Fatigue;
- short production disruption;
- rank change.

Never:

- lose room permanently;
- lose CCL;
- lose unique survivor;
- lose unique blueprint ownership.

---

# 12. Attacker Risk

Attacker risks:

- Supply;
- consumables;
- field loot;
- unit injury/death;
- failed raid charge;
- rank.

Attacker cannot endlessly probe without cost.

---

# 13. Retreat

Attacker may extract early.

This preserves PvE philosophy:

> knowing when to leave is skill.

Early extract:
- keeps secured raid loot;
- yields less prestige;
- avoids deeper defense.

---

# 14. Command Core

Reaching Command Core does not "destroy the base".

Reward:

- prestige;
- Combat Data;
- Encrypted Combat Cache;
- seasonal score;
- temporary defender debuff small/limited.

No total destruction mechanic.

---

# 15. Sabotage Limits

Possible temporary effects:

- Workshop -10% speed for 30 min;
- Security offline 15 min;
- Radio scan penalty 20 min;
- Resource Site link interrupted.

No effect longer than a few hours in baseline.

No overnight account ruin.

---

# 16. Defense Design

Player can influence raid path via:

- room placement;
- doors;
- security;
- power;
- traps;
- response squad;
- hidden route.

But must preserve mandatory path validity.

No impossible maze/exploit layout.

---

# 17. PvP Rewards

Main:

- Combat Data;
- Credits;
- Encrypted Combat Cache;
- rank/prestige;
- limited exposed resources.

PvP is not the only source of endgame power.

Most core power still has PvE route.

---

# 18. Anti-Grief

- matchmaking band;
- attack cooldown on same defender;
- protection after heavy loss;
- daily exposed-resource cap;
- no permanent defender death;
- no CCL downranking;
- no zeroing base.

---

# 19. Success Criteria

PvP works if:

1. attacker feels they are exploring another player's real base;
2. defender layout matters;
3. loss is meaningful but not devastating;
4. retreat remains valid;
5. PvP gives prestige/alternate progression, not mandatory domination.
