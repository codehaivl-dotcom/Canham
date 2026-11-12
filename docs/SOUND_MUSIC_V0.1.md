# BURROW ZERO — Sound & Music Direction v0.1

**Status:** Direction baseline  
**Production goal:** simple, reusable, AI-friendly audio package.

---

# 1. Audio Pillars

1. **Home feels warm.**
2. **Outside feels uncertain.**
3. **Technology has distinct sound identity.**
4. **Combat is readable before it is loud.**
5. **Music never fights the management loop.**

---

# 2. Silo Ambience

Base layer:

- low ventilation hum;
- distant generator;
- soft machinery;
- occasional footsteps;
- radio noise.

Room accents:

Generator:
- low turbine pulse.

Water:
- pump/liquid.

Hydroponics:
- fan + soft water trickle.

Clinic:
- quiet electronic beep.

Workshop:
- metal tap / tool servo.

Keep loops subtle.

---

# 3. Surface / Dungeon Ambience

Civilian ruin:
- wind;
- loose metal;
- distant structure creak.

Hospital:
- fluorescent hum;
- intermittent alarms;
- ventilation.

Military:
- heavy doors;
- relay clicks;
- distant machinery.

Alien:
- non-musical resonance;
- low harmonic pulse;
- unfamiliar spatial sound.

---

# 4. Music Identity

Main theme:

- warm but mysterious;
- simple motif;
- not epic orchestral by default.

Palette:

- soft synth;
- muted percussion;
- low strings/pads;
- sparse piano/mallet;
- processed texture.

---

# 5. Adaptive Music States

### Silo Calm
low intensity.

### Expedition Explore
sparse pulse.

### Threat
adds rhythm/bass.

### Combat
clear percussion.

### Boss
strong motif + threat layer.

### Extraction
rising urgency.

Transition via stems rather than new track every room.

---

# 6. Faction Music Hints

Continuity:
- disciplined pulse.

Free Settlements:
- organic/acoustic texture.

Earthborn:
- wind/percussion.

Archivists:
- clean synth/tones.

Ascendants:
- alien harmonic layer.

Keep subtle; no full soundtrack per faction initially.

---

# 7. Weapon Readability

Each weapon family must have distinct transient:

- Ballistic: sharp mechanical crack;
- Laser: clean charge + focused beam;
- Rocket: heavy launch + delayed blast;
- Fire: continuous roar;
- EMP: electrical snap + low shutdown pulse.

Player should recognize weapon class without looking.

---

# 8. Enemy Readability

Important ability gets pre-sound:

- Brute Slam windup;
- Spitter inhale;
- Drone charge;
- Void shield;
- Mimic reveal.

Audio telegraph supports fair combat.

---

# 9. UI Sound

UI palette:

- soft mechanical clicks;
- short confirmation;
- no casino jingle.

Cache opening:
- physical latch/decrypt;
- rarity sting short;
- Artifact/Alien unique but restrained.

No 5-second fanfare for common reward.

---

# 10. Survivor Voice

MVP:
- non-verbal vocalizations / short barks.

Examples:
- acknowledge;
- hurt;
- alert;
- revive;
- happy return.

Avoid full voiced dialogue initially.

Benefits:
- easier VI/EN localization;
- lower production cost;
- mascot charm.

---

# 11. Radio Story

Narrative transmissions can use:

- text + radio processing;
- optional limited voice for major story moments later.

Do not require full bilingual voice acting for MVP.

---

# 12. Dynamic Mix

Priority during combat:

1. danger telegraph;
2. player weapon;
3. enemy hit;
4. music;
5. ambience.

Sidechain/duck music slightly on critical alert.

---

# 13. Silence

Use silence intentionally:

- entering unknown room;
- after squad death;
- before alien reveal.

Not every moment needs music.

---

# 14. AI Production Guidance

Use reusable audio families.

Avoid hundreds of unique clips.

Target first package:

- 6 ambience loops;
- 5 music stems/themes;
- 9 weapon families;
- 20 enemy cues;
- 25 UI sounds;
- 15 survivor vocalizations.

AI-generated audio must be manually curated for consistency and licensing suitability.

---

# 15. Success Criteria

Audio succeeds if:

- Silo feels safe/home-like;
- player hears danger before reading text;
- weapons are distinct;
- audio scope remains production-realistic.
