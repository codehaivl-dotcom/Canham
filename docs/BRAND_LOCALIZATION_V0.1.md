# BURROW ZERO — Brand & Localization v0.1

**Status:** LOCKED  
**Date:** 2026-11-12

---

# 1. Game Name — LOCKED

**BURROW ZERO**

This replaces the previous internal names:

- Căn Hầm / Canham;
- Echo Silo.

Older documents may still contain historical references to those names. From this point forward, all new product-facing content uses **BURROW ZERO**.

---

# 2. Official Slogan — LOCKED

> **Deep Below. Far Beyond.**

Meaning:

- **Deep Below** — the player's home, Silo, excavation, underground survival and expansion;
- **Far Beyond** — expeditions, unknown locations, alien threats, other Silos, PvP and the persistent world.

The slogan remains in English in the primary logo lockup for both initial languages.

Vietnamese meaning for localization/context only:

> **Sâu dưới lòng đất. Vươn tới tận xa.**

This Vietnamese line is not the primary official slogan.

---

# 3. Brand Core

BURROW ZERO should feel:

- accessible;
- adventurous;
- slightly mysterious;
- survival-focused without being grimdark;
- cute enough to create attachment;
- serious enough for death, danger, bosses and PvP.

---

# 3.1 Canonical Art Production

Detailed production rules:

[ART_PRODUCTION_V0.1.md](./ART_PRODUCTION_V0.1.md)

Core visual screen targets:

[VISUAL_SCREEN_TARGETS_V0.1.md](./VISUAL_SCREEN_TARGETS_V0.1.md)

---

# 4. Mascot Direction — LOCKED

Primary survivor species:

**Panda**

Art direction:

- simple stylized 3D;
- low-poly / primitive-friendly;
- chunky silhouette;
- large head;
- short limbs;
- mitten/simple hands;
- one shared base body/rig;
- role identity mainly through helmet/headgear, backpack, weapon/tool and one body layer;
- no realistic fur simulation;
- no detailed cloth simulation;
- no tiny buckles, straps or decorative geometry unless gameplay-readable.

Target:

> An AI agent should be able to recreate most characters from primitive meshes without requiring external 3D generation tools.

---

# 5. Logo Direction

Master lockup:

```
[PANDA / BURROW ICON]  BURROW ZERO
                       Deep Below. Far Beyond.
```

Logo principles:

- bold geometric wordmark;
- readable at small size;
- simple silhouette;
- minimal number of shapes;
- BURROW may use off-white/light neutral;
- ZERO may use warm yellow/orange accent;
- optional panda/burrow icon;
- slogan smaller and secondary;
- no complex illustration inside the wordmark;
- no gradients required for the production logo;
- must work in monochrome.

Logo variants needed later:

1. horizontal master;
2. stacked;
3. icon-only;
4. monochrome;
5. dark-background;
6. light-background.

---

# 6. Initial Languages — LOCKED

The first supported languages are:

1. **Vietnamese — vi**
2. **English — en**

Both languages are first-class launch languages.

---

# 7. Localization Architecture

All user-facing text must be externalized.

Do not hardcode UI strings into gameplay logic.

Recommended structure:

```
localization/
  en.json
  vi.json
```

Stable semantic keys:

```
ui.deploy
ui.extract
ui.scout
resource.power
resource.water
room.clinic
role.medic
mission.hospital.title
```

Avoid keys based on literal English text.

---

# 8. Source Language Policy

Design docs may continue to be primarily Vietnamese because the project owner works in Vietnamese.

In-game localization source-of-truth:

- stable localization key = canonical identifier;
- English and Vietnamese are parallel values;
- game logic never depends on translated display strings.

Example:

```json
{
  "ui.deploy": {
    "en": "Deploy",
    "vi": "Triển khai"
  },
  "ui.extract": {
    "en": "Extract",
    "vi": "Rút lui"
  }
}
```

---

# 9. Language Selection

First launch behavior:

- if device/system language is Vietnamese → default Vietnamese;
- otherwise → default English;
- player can change language at any time in Settings;
- language change does not affect save data.

---

# 10. UI Rules for Bilingual Production

Because Vietnamese text can be longer than English:

- buttons support at least ~30% text expansion;
- avoid fixed-width text baked into 3D assets;
- avoid text baked into textures;
- use icons + localized labels where useful;
- UI containers resize or wrap;
- all fonts include full Vietnamese diacritics;
- uppercase Vietnamese must be tested explicitly.

Examples:

- TRIỂN KHAI
- RÚT LUI
- NGHIÊN CỨU
- ĐỘI HÌNH
- CĂN CỨ
- TÀI NGUYÊN

---

# 11. Text in Concept Art

Concept images may contain English placeholder UI for speed.

Production assets must not use concept-art text as final UI.

Agent implementation rule:

> recreate layout and visual hierarchy, not rasterized text from concept images.

All real UI text comes from localization files.

---

# 12. Tone of Voice

English:

- short;
- direct;
- tactical;
- slightly mysterious.

Vietnamese:

- natural Vietnamese;
- concise;
- avoid literal machine translation;
- prefer familiar game terminology where clearer.

Examples:

| English | Vietnamese |
|---|---|
| Deploy | Triển khai |
| Extract | Rút lui |
| Scout | Trinh sát |
| Unknown Sector | Khu vực chưa biết |
| Threat | Mối đe dọa |
| Loot | Chiến lợi phẩm |
| Survivor | Người sống sót |
| Workshop | Xưởng |
| Research | Nghiên cứu |

---

# 13. Product Naming Rule

Always write:

**BURROW ZERO**

Do not use:

- BurrowZero;
- Burrow zero;
- BURROW 0;
- The Silo as the game title;
- Căn Hầm as public title.

"Căn Hầm" remains only a historical/internal reference where needed.

---

# 14. Current Brand Lock

```
GAME
BURROW ZERO

SLOGAN
Deep Below. Far Beyond.

PRIMARY CHARACTER
Panda survivor

ART
Simple AI-first low-poly 3D

INITIAL LANGUAGES
Vietnamese + English
```

Before commercial public release, perform final store/domain/trademark clearance for the name.
