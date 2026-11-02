# Rackcraft changelog

What's coming next, and what changed in each release. There are two parts:

- **[Rackcraft (the mod)](#rackcraft-the-mod)**: Rackcraft and its add-ons, Quartermaster and the Grid Charger
- **[Rackcraft: The Modpack](#rackcraft-the-modpack)**: the CurseForge modpack built around it

The newest is at the top of each.

Found a problem with a release? [Open an issue](https://github.com/azerbai/rackcraft-issues/issues/new/choose), or type `/rcfeedback` in game.

---

# Rackcraft (the mod)

## Coming next

These are planned, not promised, and there are no dates. The order can change, and feature requests can move things up. Every compat feature is optional: without the other mod, Rackcraft plays exactly as before.

- **Recipes in JEI.** Every Rackcraft machine's recipes, so you can look up how anything is made.
- **Jade tooltips.** Look at a rack, reactor, Tokamak or Pylon to see its temperature, power, output and health.
- **Create power, both ways.** Turn Create rotation into Rackcraft power, and Rackcraft power back into rotation. The conversion rates are configurable, so Create-focused packs can balance it their own way.
- **Rackcraft companies follow FTB Teams.** Making or joining an FTB team makes or joins the matching Rackcraft company.
- **Fix: structures belong to the default company.** Racks and other machines in generated structures can't be taken over or reassigned. This fix covers worlds that already exist too.
- **The vehicle line, finished.** More vehicles (helicopters included), and upgrades for line-built vehicles so building one beats buying it.
- **Megaprojects.** Long late-game builds that use up RackCoin, materials and compute, and leave something permanent behind.

## Rackcraft 2.5.0 (2026-11-01)

- **Feedback from the game.** The first time you join a world, one chat message links to this issue tracker. `/rcfeedback` shows it again. To turn it off, set `feedback.prompt: false` in `rackcraft.json`.

## Rackcraft 2.4.1 (2026-10-31)

- **Fix:** `/locate` on a Rackcraft structure no longer freezes the game for minutes, especially with Tectonic or Terralith installed. Where structures generate is unchanged.

## Rackcraft 2.4.0 and Quartermaster 1.2.0 (2026-10-27)

- **Vehicle lines (first version).** With Superb Warfare installed, its ground vehicles can be built on the Assembly Line. The robots fit each part in turn until the finished vehicle drives off the belt. Needs Prime Brokerage research.
- Rackcraft's steel now counts as steel for other mods' recipes.
- **Fix:** Superb Warfare shells no longer pile up at spawn every time the server starts.

## Rackcraft 2.3.0 (2026-10-27)

- **A fair final fight in armed worlds.** With Superb Warfare or TaCZ installed, the final boss is much tougher and won't let you hide in a vehicle. To turn this off, set `ending.armedWorld: false`.
- **Fix:** the first quarter's target after going public is now reachable.

## Rackcraft 2.2.2 (2026-10-22)

- **Pylons keep their grids loaded,** so two bases far apart can share power. There's a cap on loaded chunks, and `building.pylonsLoadChunks: false` turns it off.

## Rackcraft 2.2.1 and Quartermaster 1.1.1 (2026-10-21)

- **A Company tab** on the Ops Terminal once you go public, and you can pick your own stock ticker.
- **Fix:** the vehicle dealership no longer drops ammo near spawn.

## Rackcraft 2.2.0 (2026-10-21)

- **The Helium-3 supply line.** The Regolith Excavator mines on the Moon, and Cargo Pods fly home to a Docking Port in the Overworld.

## Rackcraft 2.1.0 and Quartermaster 1.1.0 (2026-10-20)

- **The vehicle dealership.** With Superb Warfare installed, buy any vehicle at the Exchange and it parachutes in, charged and loaded.

## Rackcraft 2.0.1 (2026-10-20)

- **Fusion is five times stronger**, with heat, fuel and ignition scaled to match.

## Rackcraft 2.0.0 (2026-10-20)

The first numbered release: the data center (racks, RackCoin, the Exchange, power, cooling, storage and the Assembly Line), the world (abandoned data centers, the Military Base, weapons and getting around), multiplayer companies, and space (rockets, orbit, the Moon and fusion).

---

# Rackcraft: The Modpack

Each Rackcraft release reaches the modpack as an update, so the mod's changes above apply to the pack too. This part lists what changed in the pack itself: mods added, updated or removed, quests, configs and defaults.

## Coming next

- **Rackcraft updates.** Each new Rackcraft release ships as a pack update, with the quest book updated to match.
- **Being considered: a server pack** for hosting a dedicated server, instead of hosting from your own game with Essential.

## 1.0.0 (2026-11-01)

The first release, on CurseForge. Fabric 1.20.1 with Rackcraft 2.5.0, Quartermaster and the Grid Charger, Create, TaCZ with 50 gun packs, Superb Warfare, Terralith and Tectonic, a 21-chapter quest book, and Essential and Simple Voice Chat for playing with friends.
