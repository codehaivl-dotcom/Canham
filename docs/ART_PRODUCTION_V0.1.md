# BURROW ZERO — AI-First Art Production Spec v0.1

**Status:** LOCKED production direction  
**Date:** 2026-11-12  
**Goal:** every core visual asset must be practical for an AI coding/3D agent to build directly from simple meshes, reusable rigs, reusable materials and modular kits.

---

# 1. North Star

BURROW ZERO must look:

- cute and readable;
- simple enough to build procedurally;
- distinct at gameplay distance;
- consistent across hundreds of assets;
- low-cost to rig and animate;
- not dependent on photoreal textures or external 3D generation.

Production rule:

> If an asset cannot be approximated convincingly with primitives + simple low-poly mesh editing, it is too complex for the default art pipeline.

---

# 2. Primary Visual Style

**Simple mascot low-poly 3D**

Target qualities:

- chunky shapes;
- rounded/blocky silhouettes;
- matte materials;
- broad color regions;
- minimal texture detail;
- no realistic fur;
- no cloth simulation;
- no skin shading;
- no complex hair;
- no micro-surface detail;
- no photoreal PBR dependence.

The style should survive:
- mobile-like camera distance;
- medium PC zoom;
- low texture resolution;
- simplified lighting.

---

# 3. Panda Survivor Body — LOCKED

All standard panda survivors use **one shared base body and skeleton**.

## Proportions

Approximate:

- head = ~38% total character height;
- torso = ~32%;
- legs = ~20%;
- feet = ~10%;
- arms short and thick;
- no visible fingers required in gameplay.

Target body height in engine:

```
1.0 game unit = standard panda height reference
```

Exact world scale can change, but all survivors share one reference.

## Base body parts

Preferred separate meshes:

1. head;
2. left ear;
3. right ear;
4. torso;
5. left upper arm;
6. right upper arm;
7. left lower arm/mitten;
8. right lower arm/mitten;
9. left leg;
10. right leg;
11. left foot;
12. right foot.

Face can be:
- simple material regions;
- minimal texture/decal;
- or low-poly face pieces.

No articulated fingers.

---

# 4. Primitive Budget Per Survivor

Default survivor should be reproducible with roughly:

- 12–20 main primitive/low-poly body pieces;
- 5–12 gear pieces;
- 1 weapon/tool assembly;
- 1 backpack assembly.

Target:

```
< 40 meaningful mesh objects before merge
```

After mesh combine/export:
- body may become 1–3 skinned meshes;
- accessories may remain modular.

Agent rule:

> Do not add geometry that cannot be noticed at normal gameplay zoom.

---

# 5. Polygon Budget

These are **production ceilings**, not targets to fill.

## Survivor

- base body: 1,500–3,000 triangles;
- full normal outfit: 2,500–5,000 triangles;
- hero/story survivor ceiling: ~7,000 triangles.

## Standard enemy

- 1,500–4,500 triangles.

## Elite

- 3,000–7,000 triangles.

## Boss

- 8,000–15,000 triangles.

## Room prop

- tiny prop: 20–150 triangles;
- normal prop: 100–500;
- hero machine: 500–1,500.

If procedural primitive meshes look good enough, lower is better.

---

# 6. Shared Rig

One standard panda humanoid-lite rig.

Minimum bones:

- root;
- pelvis;
- spine;
- chest;
- head;
- left/right upper arm;
- left/right lower arm;
- left/right hand;
- left/right upper leg;
- left/right lower leg;
- left/right foot.

Optional:
- backpack anchor;
- weapon anchor;
- headgear anchor.

Do NOT require:

- finger bones;
- facial bones;
- cloth bones;
- tail simulation.

Facial emotion should use:
- eye shapes;
- brow shapes;
- mouth decal/sprite;
- simple head/body animation.

---

# 7. Animation Set

Reuse one animation library across survivor roles.

## Core locomotion

- Idle;
- Walk;
- Run;
- Turn;
- Hurt;
- Down;
- Death;
- Revive;
- Celebrate/Return.

## Combat

- Rifle attack;
- Heavy attack;
- Shotgun attack;
- Medic use;
- Engineer interact;
- Throw consumable;
- Hit reaction;
- Stagger.

## Base

- Work;
- Carry;
- Repair;
- Type/use console;
- Rest;
- Eat/drink generic.

Target MVP:

```
~25–35 reusable survivor clips
```

No bespoke animation per cosmetic.

---

# 8. Animation Style

- short;
- readable;
- slightly exaggerated;
- no realistic mocap requirement;
- clear anticipation for heavy attacks;
- clear recovery for dangerous enemy abilities.

Avoid:
- subtle finger acting;
- realistic body mechanics that expose rig limitations;
- long cinematic transitions during gameplay.

---

# 9. Role Silhouette

Role identity must come from **3 readable features maximum**.

## Vanguard
- large shoulder/chest shape;
- shield/heavy armor;
- broad stance.

## Assault
- medium rifle;
- compact armor;
- neutral silhouette.

## Scout
- hood/cap/goggles;
- small backpack/binoculars;
- light weapon.

## Engineer
- yellow/orange headgear;
- tool/wrench;
- utility backpack.

## Medic
- white/red medical headgear;
- med pack;
- compact weapon.

## Heavy
- large weapon;
- heavier backpack;
- wide stance.

Do not create unique body topology per role.

---

# 10. Outfit System

Modular slots:

```
HEAD
BODY_LAYER
BACKPACK
WEAPON_OR_TOOL
UTILITY_PROP
```

Optional cosmetic:
- scarf;
- badge;
- glasses.

Avoid:
- long coats;
- flowing fabric;
- thin straps;
- dangling cables;
- complex layered clothing.

---

# 11. Materials

Target standard character:

- 3–6 materials maximum before batching;
- preferably atlas/shared materials.

Core palette materials:

- Panda white/cream;
- Panda charcoal/black;
- Industrial dark gray;
- Warm yellow/orange;
- Medical red;
- Scout olive;
- Tech cyan/teal;
- Alien violet/cyan accents.

Material properties:
- matte;
- roughness high;
- metallic used only for machinery/weapon accents;
- little/no normal-map dependency.

---

# 12. Texture Policy

Default:
- flat color materials;
- small decals where needed.

Preferred:
- no unique 4K textures;
- no baked photoreal surfaces.

If textures are used:

- characters: 512–1024 atlas;
- props: 256–512;
- room kit: shared atlas.

Text must never be baked if it needs localization.

---

# 13. Face Design

Panda face must remain extremely simple.

Allowed:

- black eye patches;
- dot/oval eyes;
- simple brow;
- tiny nose;
- small mouth.

Expression set:

- neutral;
- happy;
- worried;
- angry/focused;
- hurt;
- surprised.

Can be achieved by:
- texture swap;
- sprite/decal;
- blend shape only if trivial.

No lip sync required for MVP.

---

# 14. Weapon Construction

Weapons should be built from:
- boxes;
- cylinders;
- wedges;
- 5–12 primary shapes.

Readable class > realistic firearm engineering.

Examples:

Assault Rifle:
- body box;
- barrel cylinder;
- stock;
- magazine;
- sight.

Rocket Launcher:
- main tube;
- grip;
- sight;
- rear cap.

Laser:
- body;
- emitter;
- energy cell;
- small glow strip.

Do not model:
- screws;
- rails;
- tiny switches;
- complex moving internals.

---

# 15. Enemy Art Rules

Enemies must follow same production simplicity.

## Infected
- panda-derived or creature primitive silhouette;
- 1 major mutation feature.

## Mechanical
- boxes/cylinders;
- obvious sensor/light;
- modular limbs.

## Alien
- 2–4 unusual large shapes;
- non-human silhouette;
- emissive accent;
- avoid dense tentacle anatomy.

Rule:

> One strong visual idea per enemy is better than ten small details.

---

# 16. Boss Art

Bosses may exceed standard complexity, but still use modular large shapes.

Boss readability:
- core;
- weak point;
- attack limb/module;
- shield state.

At gameplay camera, player must see mechanic state without zooming.

---

# 17. Environment Style

Environment uses modular low-poly kits.

Primary kits:

1. Silo;
2. Civilian ruin;
3. Industrial/Warehouse;
4. Hospital;
5. Military;
6. Research;
7. Metro;
8. Alien.

Each kit should contain:
- wall;
- floor;
- door;
- corner;
- light;
- 5–10 props;
- one hero prop.

Do not build every room uniquely.

---

# 18. Room Complexity Budget

Normal gameplay room:

- 1 room shell;
- 1 hero function prop;
- 5–12 supporting props;
- 0–3 decorative debris groups;
- 1–3 lights.

Target:
```
10–20 meaningful visible objects
```

This keeps agent generation and scene performance predictable.

---

# 19. Silo Room Identity

Each room must be recognizable from one large object.

Examples:

- Generator → turbine/generator cylinder;
- Water → blue tanks/pipes;
- Hydroponics → green grow beds;
- Clinic → bed + medical monitor;
- Workshop → bench + tool wall;
- Research → console/scanner;
- Radio → dish/signal console;
- Security → reinforced door/monitor;
- Storage → stacked crates.

Do not rely on text label for room identity.

---

# 20. Color Language

Base palette:

- dark charcoal;
- medium cool gray;
- warm cream;
- warm yellow/orange.

Functional accents:

- Water → blue;
- Food/Hydroponics → green;
- Medical → red/white;
- Research/Tech → cyan;
- Alien → violet + cyan;
- Danger → red/orange.

Use broad accent blocks.

Avoid rainbow UI/rooms.

---

# 21. Lighting

## Silo
- warm amber practical lights;
- safe/home feeling.

## Surface
- cooler daylight;
- desaturated environment.

## Dungeon
- dark neutral;
- strong practical light pools.

## Alien
- low ambient + emissive accents.

No expensive volumetrics required.

Use:
- baked/static where possible;
- few dynamic lights;
- emissive materials for readability.

---

# 22. Camera

Primary Silo:
- cutaway side/isometric hybrid.

Expedition:
- shallow isometric / 2.5D;
- ~25–35° downward angle;
- full-body survivor visible;
- room readable in one frame.

No free third-person camera required.

Camera should reduce asset requirements by avoiding unseen backsides when possible.

---

# 23. VFX

VFX must be simple and iconic.

Ballistic:
- small flash + impact.

Laser:
- straight beam + glow.

Rocket:
- simple expanding blast.

Fire:
- stylized flame cards/particles.

EMP:
- radial electrical ring.

Heal:
- short medical pulse.

Alien:
- geometric emissive pulse.

Avoid particle storms.

---

# 24. UI Art

UI should match world:

- dark charcoal panels;
- warm yellow primary action;
- rounded/chunky geometry;
- large icons;
- limited gradients;
- high contrast.

Text remains real UI text, never rasterized into generated image assets.

---

# 25. Logo

Official:

**BURROW ZERO**

Slogan:

**Deep Below. Far Beyond.**

Master logo:
- bold geometric;
- panda/burrow icon optional;
- BURROW light/cream;
- ZERO yellow/orange;
- works on white and dark backgrounds.

Vietnamese translation is localization context, not master logo slogan.

---

# 26. AI Agent Asset Workflow

Preferred asset pipeline:

```
SPEC
→ PRIMITIVE BLOCKOUT
→ SILHOUETTE CHECK
→ SIMPLE MATERIALS
→ SHARED RIG / MODULE
→ BASIC ANIMATION
→ GAMEPLAY CAMERA CHECK
→ ONLY THEN ADD DETAIL
```

Never start with:
- high-detail concept sculpt;
- photoreal reference;
- complex texture;
- unique rig.

---

# 27. Agent Acceptance Test

An asset is accepted when:

1. readable at gameplay zoom;
2. role/function obvious without text;
3. fits shared palette;
4. uses reusable materials;
5. does not require custom skeleton unless boss;
6. has no unnecessary micro-geometry;
7. can be recreated by another agent from written spec.

---

# 28. LOD / Performance

MVP:

- LOD0 standard;
- optional simplified LOD1 for world scenes;
- distant Silo survivors can use reduced animation/update frequency.

Do not build advanced LOD pipeline before profiling.

---

# 29. Naming Convention

Examples:

```
CHR_Panda_Base
CHR_Panda_Medic
GEAR_Head_Medic01
GEAR_Backpack_Engineer01
WPN_Rifle_Assault01
ENV_Silo_Wall_A
ENV_Hospital_Bed_A
VFX_EMP_Burst
UI_Icon_Resource_Water
```

Use English asset identifiers even though game supports VI/EN.

---

# 30. Hard "Do Not" List

Do NOT:

- create realistic human survivors;
- create realistic fur;
- use five-finger detailed hands;
- make unique skeleton for every role;
- use cloth simulation as dependency;
- require Tripo3D for standard assets;
- use photogrammetry;
- bake localized words into environment textures;
- model tiny details invisible from gameplay camera;
- create weapons with realistic mechanical complexity;
- use dozens of unique materials per scene.

---

# 31. Production Success Criteria

The art direction succeeds if:

- one agent can produce a new standard survivor variation quickly;
- one environment kit can generate many rooms;
- game remains charming with primitive geometry;
- 5-unit squad stays readable;
- visual style is consistent even when assets are generated across many AI sessions.
