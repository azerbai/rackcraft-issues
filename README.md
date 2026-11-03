# Rackcraft: bugs, crashes and ideas

This is the public issue tracker for **Rackcraft** (a Fabric 1.20.1 mod about building and running data centers) and its add-ons, Quartermaster and the SBW Vehicle Charger. The mod's source isn't public; this repository holds issues only.

**[Open an issue](https://github.com/azerbai/rackcraft-issues/issues/new/choose)**

| You have | Use |
| --- | --- |
| The game closed with a crash screen or a crash report | **Crash report** |
| Something works wrong, but the game keeps running | **Bug report** |
| An idea for something new, or a change | **Feature request** |

In game, `/rcfeedback` shows the link again.

**[Changelog and what's coming next](CHANGELOG.md)** · **[Ideas that won't be done](WONT-DO.md)**

Before suggesting a feature, check both: requests for something already planned, already in the mod, or on the won't-do list are closed automatically with a link to the right place.

## Crash reports

1. Find the newest file in `.minecraft/crash-reports/` (in a launcher like Prism or CurseForge, open the instance's folder first). Drag the whole file into the issue form. Don't paste just the top few lines: the useful part is often near the bottom.
2. If there's no crash report (the game froze, or closed without one), attach `.minecraft/logs/latest.log` from right after it happened instead, before you start the game again.
3. Say what you were doing just before: placing a block, opening a screen, launching a rocket, joining a server.
4. Name the modpack and its version if you play one. Otherwise list the other mods you run.

Logs can also go on [mclo.gs](https://mclo.gs) (it hides your IP address and username); paste the link in the form.

## What happens after you report

Each new issue is read by an automated triage step within a few minutes. It labels the issue, checks whether the crash comes from Rackcraft or from another mod, and asks for anything missing (usually the crash report). Crashes in Rackcraft go to the developer with a diagnosis, often with a fix already drafted. Feature requests are read by the developer.

Labels you'll see:

- `crash`, `bug`, `feature`: what the issue is
- `needs-info`: waiting for something from you (reply in a comment and triage runs again)
- `other-mod`: the crash or bug comes from a different mod; the comment says which
- `fix-in-progress`: the cause is found and a fix is being prepared
- `fixed`: fixed in a released version (the comment says which)
- `duplicate`: already reported; follow the linked issue
- `planned`: the idea is already in **Coming next** in the changelog
- `already-added`: the idea is already in a released version (the comment says which)
- `wont-do`: the idea is on the [won't-do list](WONT-DO.md)
- `off-topic`: not about Rackcraft, its add-ons or the modpack

Please keep issues to one problem each, and search the open issues first.

## About Claude

You may see Claude (Anthropic's AI assistant) listed as a contributor here. It helps write this repository's docs, such as this README and the changelog, and it's the automated triage step described above: it reads new issues, sorts and labels them, and passes crash diagnoses to the developer. It doesn't post its own replies here; the triage comments are fixed messages.
