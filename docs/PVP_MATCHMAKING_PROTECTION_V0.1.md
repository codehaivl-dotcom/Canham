# BURROW ZERO — PvP Matchmaking, Protection, Loss & Revenge v0.1

**Status:** Prototype policy baseline

---

# 1. Goals

Matchmaking should:

- avoid high-level crushing new players;
- preserve target variety;
- create fair but not perfectly mirrored fights;
- prevent repeated harassment.

---

# 2. Match Score

Prototype hidden score:

```
Match Score =
CCL Weight
+ Defense Rating
+ Best Defense Squad Power
+ Tech Tier
+ PvP Rating modifier
```

CCL is primary.

Suggested candidate band:

- CCL ±1;
- Defense Rating ±20%;
- PvP rating soft band.

System can expand band after search timeout.

---

# 3. Defense Rating

Derived from:

- active security rooms;
- door level;
- turret/drone capacity;
- defense squad;
- power redundancy;
- relevant research.

Not from total account wealth.

---

# 4. Raid Charges

Prototype:

- 3 PvP Raid Charges;
- regenerate 1 every 4h;
- hard cap 3.

No paid-only infinite attacks in core design.

Season/event may grant extra.

---

# 5. Protection States

### New Player Protection
Until PvP unlock + first voluntary PvP action.

### Post-Loss Shield
Triggered after meaningful loss.

Prototype:
- minor loss: 2h;
- major loss / Command breach: 6h.

### Offline Chain Protection
If attacked 2 times in 8h:
- next protection 8h.

Protection may end early if player launches offensive PvP.

---

# 6. Same-Target Cooldown

Same attacker cannot attack same defender again for:

```
24 hours
```

unless:
- Revenge;
- special event.

Even then, max one additional direct interaction.

---

# 7. Revenge

Defender receives:

- attacker identity;
- raid objective;
- rooms breached;
- resources lost;
- approximate attacker squad.

Revenge window:

```
24 hours
```

Benefits:

- free Quick Scout;
- +10% Intel confidence;
- no additional matchmaking search.

Revenge does not ignore CCL safety rules.

---

# 8. Revenge Chain Limit

No infinite revenge loop.

Sequence:

```
A attacks B
→ B may Revenge A
→ chain ends
```

A does not get "revenge revenge".

---

# 9. Rank

PvP Rating changes by:

- objective difficulty;
- target rating;
- extraction success;
- Command breach.

Resource Raid gives lower rating than Command Assault.

Rank should reflect PvP performance, not spending.

---

# 10. Leagues

Prototype seasonal bands:

- Rust;
- Iron;
- Steel;
- Titanium;
- Prototype;
- Zero.

Names provisional.

Rewards focus on:

- cosmetic;
- Combat Data;
- cache;
- banner/title;
- limited convenience.

Avoid exclusive must-have weapon.

---

# 11. Resource Loss Cap

Per 24h defender account:

```
Max common resource loss = 15% protected daily production equivalent
```

Strategic resource loss:

- much lower;
- some categories non-stealable.

Once cap reached:
- attacks can still happen for rank/prestige;
- resource theft disabled/reduced.

---

# 12. Protection of New Progress

Recently crafted or first-clear unique rewards:

- cannot be stolen.

Blueprint ownership:
- never stolen.

Survivors:
- never stolen.

---

# 13. Smurf / Sandbag Prevention

Matchmaking uses:

- highest CCL reached;
- highest defense tier built;
- best squad power in recent window.

Removing gear or disabling rooms does not drastically lower match band immediately.

Use rolling peak.

---

# 14. Inactivity

Inactive players:

- gradually leave ranked pool;
- may remain NPC-like world targets only with heavily protected rewards;
- no farming dead accounts for progression.

---

# 15. Anti-Collusion

Track repeated reciprocal attacks.

Reduce rewards if:

- same pair repeatedly trades attacks;
- alliance members attempt exploit;
- suspicious low-defense feeding.

Alliance members cannot normal-raid each other.

---

# 16. Battle Log

Defender sees:

- timestamp;
- attacker;
- objective;
- result;
- route;
- alarm peak;
- loot lost;
- defense injuries;
- replay summary/event log later.

Not full deterministic replay required in MVP.

---

# 17. Success Criteria

System works if:

- new players are protected;
- strong players still find worthwhile targets;
- no one can zero another account;
- revenge feels satisfying;
- repeated harassment is structurally limited.
