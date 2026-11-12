# BURROW ZERO — First 1–2 Hours / Tutorial Flow v0.1

**Status:** Onboarding baseline  
**Goal:** teach by need and action, not popup overload.

---

# 1. Tutorial Philosophy

Player should understand within first 10 minutes:

- this is my Silo;
- these pandas are my survivors;
- I need Power/Water/Food;
- I can expand;
- outside world contains what I cannot make.

Tutorial uses curated outcomes, not randomness.

---

# 1.1 CCL milestones during onboarding

Curated tutorial progression:

- Start at **CCL1**.
- After restoring basic life support, upgrade to **CCL2** → Surface Gate + squad cap 3.
- Before the first full expedition, curated objectives advance to **CCL3** → Radio/Scout + Workshop.
- After first expedition/return milestone, advance to **CCL4** → Clinic/Training.

Use prototype CCL/repair costs and deterministic ledger in [PROTOTYPE_CONTENT_PACK_V0.1.md](PROTOTYPE_CONTENT_PACK_V0.1.md); final live costs remain tunable. Before first Quick Scout the repaired RadioL1 is operational, not just unlocked.

---

# 2. 0–5 Minutes — Wake the Silo

Scene:
Emergency lights.

Tasks:

1. activate Emergency Core;
2. inspect 6 starting survivors;
3. restore Generator;
4. restore Water Treatment.

Teach:
- room click;
- worker assignment;
- Power bar;
- Water.

No combat yet.

---

# 3. 5–15 Minutes — Make It Livable

Tasks:

1. repair Living Quarters;
2. assign worker;
3. clear first adjacent sector:
   - debris;
   - 2 easy Crawler;
4. build Hydroponics;
5. upgrade CCL2 then CCL3 using fixed tutorial costs;
6. repair RadioL1 before first Quick Scout. Living does not require a worker; staff Generator/Water/Hydro with3residents while squad3 deploys.

Teach:
- population;
- Food;
- sector state;
- basic combat;
- construction.

First combat cannot permanently kill tutorial survivor.

---

# 4. 15–25 Minutes — First Expedition

A nearby House signal appears.

Curated:

- squad 3;
- Vanguard/Assault/Medic;
- simple loadout;
- Quick Scout.

House has:
- 4 rooms;
- one branch;
- one cache;
- one wounded survivor.

Teach:
- Scout;
- Deploy;
- room progression;
- loot;
- Extract.

---

# 5. 25–35 Minutes — Return Home

Post-run:

- survivor injury;
- CCL4 upgrade then Clinic repair;
- loot used for Workshop;
- open first Supply Cache;
- rescue survivor joins;
- Living Quarters upgrade/expansion objective appears if beds are full.

Teach:
- injury;
- recovery;
- card reward reveal;
- roster growth.

---

# 6. 35–50 Minutes — Need Parts

Silo needs Components.

Contract points to Warehouse.

Player chooses:
- Quick Scout;
- recommended AOE hint.

Warehouse:
- first swarm;
- locked side room;
- optional deeper loot.

Teach:
- weapon identity;
- optional route;
- retreat decision.

---

# 7. 50–65 Minutes — Expand Radio Use

RadioL1 was repaired before minute15. Teach its existing World Map search/filter; do not charge a second repair. GeneratorL2 upgrade is available after Warehouse for Clinic/Training power headroom.

A distant Hospital appears.

Teach:
- World Map;
- search radius;
- target card;
- threat/loot/intel.

No need to enter Hospital immediately.

---

# 8. 65–80 Minutes — Survivor Identity

Open roster screen.

Teach:

- profession;
- combat role;
- trait;
- job;
- gear.

Player chooses one survivor for Training.

Avoid showing every stat formula.

---

# 9. 80–100 Minutes — The Unknown Sector

Silo excavation finds unusual old room.

Player may:

- restore;
- convert.

Curated room:
Old Sensor Room.

Restore:
unlocks better Radio hint.

Teach:
- Restore vs Convert;
- Silo history;
- meaningful base layout.

---

# 10. 100–120 Minutes — First Signal Hook

Radio receives:

```
UNKNOWN SILO SIGNAL
DISTANCE: 18.4 KM
STATUS: ACTIVE
```

Player gets objective:

**Investigate when ready.**

This is a passive story transmission preview, not a deployable18.4km target outside RadioL1 range. Investigation unlocks at CCL7 with RadioL3; existing range limits still apply. This points toward Chapter3/NPC Silo. Sensor Room restore adds a clue, never a mandatory range bypass.

Tutorial ends.

---

# 11. Tutorial Safety Rules

During first hour:

- no permanent death in protected tutorial missions/sector; SAFE_DOWN handling in SURVIVOR_RECOVERY_V0.1.md;
- no PvP;
- no Mimic;
- no Resource Site contest;
- no hard hunger spiral;
- no expiring critical target.

After first hour:
normal rules phase in gradually.

---

# 12. Popup Budget

Maximum:
- one short tooltip per new system;
- no full-screen tutorial longer than 2–3 steps.

Prefer:
- highlighted button;
- character speech bubble;
- objective card.

---

# 13. Skip / Returning Player

Player can:

- skip tutorial explanation;
- not skip required core unlocks.

Settings:
"Reduced Guidance".

---

# 14. First Session Success

First2h is onboarding scope, not the whole extended slice. At2h player should haveCCL4 and:

- functioning Silo;
- 7–8 survivors;
- squad 3;
- 2–3 expeditions completed;
- one cache opened;
- one injury treated;
- World Map unlocked;
- first unknown signal.

Player should already understand the full loop in miniature. Extended2–4h slice adds CCL5,squad4,ResearchLabL1 and one tierI research. Content/ledger and longer-slice checklist live in PROTOTYPE_CONTENT_PACK_V0.1.md and PROTOTYPE_PROGRESSION_V0.1.md.
