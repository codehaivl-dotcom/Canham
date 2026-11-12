# BURROW ZERO — Social, Player Profile & Safety v0.1

**Status:** Online product baseline  
**Scope:** lightweight social layer supporting PvP and Alliances without turning the game into a social network.

---

# 1. Principles

Social features must:

- support cooperation and rivalry;
- protect players from repeated harassment;
- remain optional;
- expose minimal personal information;
- work across Vietnamese and English players.

---

# 2. Player Profile

Public profile may show:

- display name;
- avatar/banner;
- CCL;
- PvP league;
- Alliance;
- selected achievements/titles;
- optional showcased survivor/Silo badge.

Do NOT show:

- real name;
- email;
- exact location;
- private resource totals;
- full defense layout.

---

# 3. Display Name

Requirements:

- unique identifier may be separate from display name;
- display name can be changed with cooldown;
- profanity filter;
- no impersonation of official/system accounts.

Localized UI must not depend on display name length.

---

# 4. Friends

Friend functions:

- send request;
- accept/decline;
- remove;
- view online/recent status only if privacy settings allow;
- invite to Alliance if eligible.

Friends do not receive combat advantages.

---

# 5. Block

Blocked player cannot:

- send friend request;
- send direct messages;
- invite to Alliance;
- appear as a manually selected social target.

Normal automated matchmaking may avoid blocked pairs when practical.

Block does not alter rankings.

---

# 6. Report

Report categories:

- harassment;
- hate/abuse;
- inappropriate name;
- spam;
- cheating/exploit;
- offensive Alliance content;
- other.

Report submission should attach:
- relevant message/log IDs;
- target player ID;
- recent interaction context.

No need for user to manually screenshot as the only evidence path.

---

# 7. Chat Channels

Baseline:

### Alliance Chat
Unlocked with Alliance membership.

### Direct Message
Friends-only by default.

### System/Event Feed
Read-only.

No global free-for-all chat required for launch.

This reduces moderation load and spam.

---

# 8. Chat Safety

Features:

- mute;
- block;
- report;
- basic profanity/spam filtering;
- rate limits;
- link restrictions.

Never expose exact real-world location.

---

# 9. Cross-Language Support

VI/EN launch baseline:

- messages are user-generated and not automatically translated in v0.1;
- system messages localized;
- optional quick-chat phrases can be localized.

Examples:

- Need help
- Boss ready
- Resource Site spotted
- Thanks
- Retreat

---

# 10. PvP Interaction Safety

PvP already limits harassment through:

- matchmaking bands;
- same-target cooldown;
- loss caps;
- protection shields;
- finite Revenge chain.

Social block/report complements these systems.

---

# 11. Alliance Moderation

Alliance Leader/Officer can:

- remove member;
- mute member from Alliance chat temporarily if supported;
- manage invite permissions.

Platform/system moderation remains authoritative over abusive conduct.

---

# 12. Privacy

Default:

- only game identity is public;
- online presence can be hidden;
- friend requests can be disabled;
- DMs friends-only.

No public location, age, or external account data.

---

# 13. Success Criteria

Social layer succeeds if:

1. players can coordinate Alliance play;
2. rivals cannot harass indefinitely;
3. reporting is straightforward;
4. privacy is conservative by default;
5. moderation scope remains manageable.
