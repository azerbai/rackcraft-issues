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

- **Native Create power blocks.** A Dynamo Coupler and Rack Motor that connect Rackcraft power to Create shafts directly, without Crafts & Additions.
- **The vehicle line, finished.** More vehicles (helicopters included), and upgrades for line-built vehicles so building one beats buying it.
- **Megaprojects.** Long late-game builds that use up RackCoin, materials and compute, and leave something permanent behind.

## Rackcraft 2.7.0 (2026-11-02)

- **Companies follow FTB Teams.** With FTB Teams installed, your FTB party is your company: same name, same members, and the party owner leads it. If you already had a company, your party takes it over, with its balance, research and machines. Leaving the party leaves the company. Players who aren't in a party keep the company they have.
- **The Grid Interface**, a new block that connects Rackcraft power to other mods' energy. With Crafts & Additions, an Alternator on a Create shaft powers your grid at about 1 kW per 256 SU. After the cheap new **Grid Export Permit** research, the grid can run an Electric Motor too, but at a poor rate and with a cap, so a fusion ring can't spin Create forever. Server owners can change all the rates in the config.
- **Create recipes** (only with Create installed): crush Bauxite Ore and Failed Modules, press Copper Wire, and mix Steel in a heated Basin.
- **Create Display Links**: show your RackCoin balance, mining rate, share price, a machine's power or a battery's charge on display boards and nixie tubes.

## Rackcraft 2.6.0 (2026-11-02)

- **Ruins are finders keepers.** Machines in Rackcraft structures (abandoned data centers, the Hyperscale Campus, the Military Base, the Moon sites) now belong to nobody, and the first company to use one claims it, free. Before, they all belonged to the default company, so anyone in a company of their own was locked out of every ruin. Ruins in existing worlds work the same way, until someone in the default company uses them. Server operators can move machines between companies with `/company reassign`.
- **JEI recipe pages** for the Assembly Line (each part in order, the robots, the time and the research needed) and for all 12 processing machines. Items with no recipe, like ores, Moon soil and ruin loot, get a page saying where they come from.
- **Jade tooltips** for machines and cables: a machine's readings and who owns it, and a cable's paint and status. Hold Shift for the power network and coolant loop.

JEI and Jade are optional: without them, Rackcraft plays exactly as before.

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


## Before 2.0.0: the early builds

Rackcraft had no version numbers for its first two weeks: every build was called 1.0.0. The labels below were given afterwards, by date, to show how the mod grew. They were never separate downloads.

### 0.9 (2026-10-18 to 10-20): orbit, the Moon and fusion
- **Low Orbit as a place:** ride a Crew Capsule up, with zero-g, Mag Boots, a Pressure Suit, sealed rooms and airlocks, radiators, Station Cores, Ground Links, Cargo Pods, Docking Ports, station debris and Whipple Shields.
- **The Moon:** 1/6 gravity on a finite globe, the Lunar Lander, Ilmenite and titanium, Lunar Ice, the Regolith Sifter, the long lunar night, dust, solar storms and micrometeorites, the Apollo site, a crashed lunar data center, and Lunar Claim Beacons.
- **Fusion:** a real ring-shaped Tokamak with Deuterium, ignition, Divertor heat and a fail-safe quench, plus a build guide.
- **After the IPO:** quarterly earnings, board mandates, Display Cases and a museum, and the ending reaching into orbit.
- Fixed: the IPO's Personal Funds count stopping at 2,147,483,647.

### 0.8 (2026-10-17): arms and companies
- **TaCZ and Superb Warfare support:** every gun pack and vehicle on the Exchange, in an Arms tab.
- **New add-ons:** Quartermaster (keeps your guns and vehicles loaded) and the Grid Charger (charges SBW vehicles from your grid).
- **Multiplayer companies:** each team gets its own balance, research and machines.
- The rail cannon, column skids and cable paint.
- Five unused blocks retired; the Photonic Spine Router and Topological Core added.

### 0.7 (2026-10-14): strikes and the ending
- **The ending:** the IPO, the [redacted], the [redacted] and the [redacted].
- Orbital strikes, the tactical warhead and space debris.
- **Exchange tiers and surge pricing.**
- 45 advancements in a Rackcraft tab.
- A reworked campus, and more power and storage tiers.
- The Desalination Plant was removed; the Water Pump takes any water now.

### 0.6 (2026-10-13): polish
- The simulation runs about 4x faster on big bases.
- Proper GeckoLib guns with real damage, hit markers and effects (flame jets, beams, lightning, plasma bolts).
- Client-side Jetpack and Grapple with sounds, smooth Mag-Lev, pylon wires and masts, turret heads, guard skins and Blast Doors.
- Structure placement checks, and Hard difficulty balanced.

### 0.5 (2026-10-09): building, movement and arms
- **Wiring and building:** Trunk Bundles, the Cable Planner, Patch Panels, Pylons, the Power Beacon, the Constructor's Gauntlet and the Terraformer Cannon.
- **Blueprints:** the Blueprint Scanner, retrofits, Overclocking and Compute Pods.
- **Getting around:** the Grapple, the Hydrogen Jetpack, Quantum Teleport Pads and Mag-Lev.
- **Arms and ruins:** energy weapons, EMPs, Sentry Turrets, guards, the Military Base, hostile data centers and bounties.

### 0.4 (2026-10-08): building at scale
- The Saturn V, and megastructure research up to 10x10x10 cubes.
- Solar Arrays, Wind Towers, wear and servicing, belt loaders and storage-fed Drone Docks.
- **Site Planner:** the Survey Stake, Construction and Terraforming Drones, Data Hall and Reactor Cube layouts, price quotes and a ledger.
- Advanced hardware: rack tiers, binned chiplets, new materials and modules, and the Cryostat.
- Storage Links, Hydrogen Tanks, the Auto-Buyer, Tanker Drones and the Procurement Wall.
- Fixed: the big-facility slowdown.

### 0.3 (2026-10-07): research and industry
- **R&D:** research, Compute Leases, frontier runs, the Wafer Fab and the Darknet Terminal.
- **Industry:** utility plants, the Electrolyser, Assembly Line robots and Maintenance Drones.
- **The launch programme:** the first rockets.
- Multiblock ports and casings, and new cubes.

### 0.2 (2026-10-07): cooling and nuclear
- Cooling reworked into coolant loops.
- Reactor arrays and the nuclear fuel cycle, item pipes, the Grid-Scale Battery, the fault finder and rack health lights.
- Fixed: a worldgen crash, solar panels making nothing, and duplication in terminal crafting.

### 0.1 (2026-10-06): the first build
- Server racks, RackCoin mining, the Crypto Exchange, fuels and the Field Manual.
- Abandoned data centers to find, the ASIC miner, the Multimeter and the HUD.
- Storage arrays, tape tiering, a storage terminal, rack-powered autocrafting and wireless access.
- AI contracts, a compute scheduler, freshwater cooling and smog.

---

# Rackcraft: The Modpack

Each Rackcraft release reaches the modpack as an update, so the mod's changes above apply to the pack too. This part lists what changed in the pack itself: mods added, updated or removed, quests, configs and defaults.

## Coming next

- **Rackcraft updates.** Each new Rackcraft release ships as a pack update, with the quest book updated to match.
- **Being considered: a server pack** for hosting a dedicated server, instead of hosting from your own game with Essential.

## 1.0.0 (2026-11-01)

The first release, on CurseForge. Fabric 1.20.1 with Rackcraft 2.5.0, Quartermaster and the Grid Charger, Create, TaCZ with 50 gun packs, Superb Warfare, Terralith and Tectonic, a 21-chapter quest book, and Essential and Simple Voice Chat for playing with friends.
