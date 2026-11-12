# Legion TD Fembussy 1.0.0

First public release of the Fembussy edition, based on Legion TD 11.4c-hf9.

| Type | Change |
| :---: | --- |
| **Added** | Added **Pick** mode, enabled by the host during the initial mode selection. Each player can lock one unit from their current roll once per game; that slot keeps the selected unit through rerolls. |
| **Added** | Added the host command `-wave N` to jump to any wave from 1 to 31, forward or backward. If combat is active, the map starts the requested wave after the round or arena is cleared. |
| **Added** | Added player-leave compensation. If a player leaves and their team is at least 15% behind in average value or income, each remaining teammate receives Basic Lumberjack Training based on the current wave: +1, +2 from wave 10, or +3 from wave 20. The team's King also gains 10% regeneration if it has already lost a life. |
| **Added** | Added incremental local tracking of games played, wins, and departures, displayed in the area previously used for ranking score. |
| **Fixed** | The King now recovers 100% of its maximum health when it loses a life. |
| **Balance** | Ent root cooldown reduced to 6 seconds. Wolverine's damage immunity after reaching 0 health increased to 3 seconds. |
| **Fixed** | Removed protection and expiration checks that could end a game, and fixed game start when testing solo. |
| **Removed** | Disabled the old ELO/ranking system and its external API calls. |

**Download:** `Legion_TD_Fembussy_1.0.0.w3x`  
**Base:** Legion TD 11.4c-hf9 Team OZE  
**Testing note:** The map archive and its internal metadata were checked. Full matches and local save behavior still need validation in the Warcraft III client.
