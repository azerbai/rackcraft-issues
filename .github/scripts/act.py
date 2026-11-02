"""Turns the AI step's verdict (out/triage.json) into actions. Nothing the AI wrote reaches the public issue except
values checked against fixed lists; its free text goes only to the private Rackcraft repository.

Public issue:  labels, and one comment built from the fixed replies below.
Private repo:  an issue with the diagnosis (out/owner_report.md), and a draft PR when the AI changed the source.

Env: GH_TOKEN (public repo), PRIVATE_TOKEN (private repo), REPO, ISSUE, PRIVATE_REPO, PRIVATE_BRANCH.
"""

import json
import os
import re
import subprocess
from pathlib import Path

KINDS = {"crash", "bug", "feature", "question", "spam"}
CAUSES = {"rackcraft", "addon", "other_mod", "conflict", "environment", "unknown"}
MISSING = {
    "crash_report": "the crash report: the newest file in `.minecraft/crash-reports/` (drag the whole file into a comment, or paste an https://mclo.gs link)",
    "latest_log": "`.minecraft/logs/latest.log` from right after the problem, before the game is started again",
    "versions": "the Rackcraft version and the modpack (name and version), or the list of other mods",
    "steps": "what you were doing just before it happened, or steps that make it happen",
    "screenshot": "a screenshot or short video of the problem",
}
LABELS = {"crash", "bug", "feature", "question", "needs-info", "other-mod", "fix-in-progress", "duplicate", "triaged", "invalid"}


def run(*args, token=None, check=True, cwd=None):
    env = dict(os.environ)
    if token:
        env["GH_TOKEN"] = token
    return subprocess.run(args, check=check, capture_output=True, text=True, env=env, cwd=cwd).stdout.strip()


def verdict():
    try:
        raw = json.loads(Path("out/triage.json").read_text())
    except (OSError, ValueError):
        return None
    kind = raw.get("kind") if raw.get("kind") in KINDS else None
    if not kind:
        return None
    cause = raw.get("cause") if raw.get("cause") in CAUSES else "unknown"
    mod = raw.get("other_mod") or ""
    mod = mod if re.fullmatch(r"[A-Za-z0-9 _.:'-]{1,40}", mod) else ""
    dup = raw.get("duplicate_of")
    dup = dup if isinstance(dup, int) and dup > 0 else None
    missing = [m for m in raw.get("missing", []) if m in MISSING]
    return {"kind": kind, "cause": cause, "mod": mod, "dup": dup, "missing": missing,
            "fix_drafted": bool(raw.get("fix_drafted")), "title": str(raw.get("owner_title", ""))[:120]}


def public_reply(v, fixing):
    if v["kind"] == "spam":
        return None
    if v["dup"]:
        return f"Thanks! This is already covered by #{v['dup']}, so I'm closing this one in favour of it. Follow that issue for updates, and add anything new there."
    if v["missing"]:
        items = "\n".join(f"- {MISSING[m]}" for m in v["missing"])
        return ("Thanks for the report! To work out what went wrong, please add:\n\n" + items +
                "\n\nReply in a comment here and this issue is looked at again automatically.")
    if v["kind"] == "feature":
        return "Thanks for the idea! It's been passed to the developer, who reads every request. Upvote with a 👍 if you'd like it too."
    if v["kind"] == "question":
        return "Thanks! This has been passed to the developer."
    if v["cause"] in ("other_mod", "conflict") and v["mod"]:
        verb = "comes from" if v["cause"] == "other_mod" else "looks like a clash between Rackcraft and"
        return (f"Thanks for the report! This {v['kind']} {verb} **{v['mod']}**. "
                f"{'Reporting it to that mod as well will help. ' if v['cause'] == 'other_mod' else ''}"
                "The developer has the details and will follow up here.")
    if v["cause"] == "environment":
        return ("Thanks for the report! This looks like it comes from the setup rather than a mod: often memory "
                "(raise the RAM given to the game), graphics drivers or a broken install. The developer has the details "
                "and will follow up here.")
    if fixing:
        return "Thanks for the report! The cause is found and a fix is being prepared; this issue will say which version has it."
    return "Thanks for the report! It's been passed to the developer with what was found so far."


def main():
    repo, issue = os.environ["REPO"], os.environ["ISSUE"]
    private_repo, branch = os.environ["PRIVATE_REPO"], os.environ.get("PRIVATE_BRANCH", "main")
    private_token = os.environ.get("PRIVATE_TOKEN") or None
    v = verdict()
    if v is None:
        run("gh", "issue", "edit", issue, "-R", repo, "--add-label", "triaged")
        print("no usable verdict; marked triaged for a human")
        return

    # A drafted fix: commit whatever the AI changed in the private checkout to a branch, open a draft PR.
    pr_url = None
    if v["fix_drafted"] and private_token and run("git", "status", "--porcelain", cwd="rackcraft"):
        name = f"auto/issue-{issue}"
        run("git", "checkout", "-B", name, cwd="rackcraft")
        run("git", "add", "-A", cwd="rackcraft")
        run("git", "-c", "user.name=rackcraft-triage", "-c", "user.email=triage@users.noreply.github.com",
            "commit", "-m", f"Draft fix for {repo}#{issue}: {v['title']}", cwd="rackcraft")
        remote = f"https://x-access-token:{private_token}@github.com/{private_repo}.git"
        run("git", "push", "--force", remote, f"HEAD:refs/heads/{name}", cwd="rackcraft")
        body = (f"Drafted automatically for https://github.com/{repo}/issues/{issue}. Review before merging.\n\n"
                + (Path("out/owner_report.md").read_text() if Path("out/owner_report.md").exists() else ""))
        pr_url = run("gh", "pr", "create", "-R", private_repo, "--draft", "--base", branch, "--head", name,
                     "--title", f"[auto] {v['title'] or 'Fix for issue ' + issue}", "--body", body[:60000],
                     token=private_token, check=False)

    # The diagnosis, privately: it may quote source code.
    if private_token and v["kind"] in ("crash", "bug", "feature", "question") and not v["dup"]:
        report = Path("out/owner_report.md").read_text() if Path("out/owner_report.md").exists() else "(no report written)"
        title = f"[{v['kind']}] {v['title'] or 'Public issue ' + issue} ({repo}#{issue})"
        body = f"Public issue: https://github.com/{repo}/issues/{issue}\n" + (f"Draft PR: {pr_url}\n" if pr_url else "") + "\n" + report
        run("gh", "issue", "create", "-R", private_repo, "--title", title[:250], "--body", body[:60000],
            "--label", "triage", token=private_token, check=False)

    labels = {v["kind"] if v["kind"] in LABELS else "triaged", "triaged"}
    if v["missing"]:
        labels.add("needs-info")
    if v["cause"] in ("other_mod", "conflict") and v["mod"]:
        labels.add("other-mod")
    if pr_url and pr_url.startswith("https://"):
        labels.add("fix-in-progress")
    if v["dup"]:
        labels.add("duplicate")
    if v["kind"] == "spam":
        labels = {"invalid"}
    current = json.loads(run("gh", "issue", "view", issue, "-R", repo, "--json", "labels"))["labels"]
    stale = [l["name"] for l in current if l["name"] == "needs-info" and "needs-info" not in labels]
    args = ["gh", "issue", "edit", issue, "-R", repo, "--add-label", ",".join(sorted(labels))]
    if stale:
        args += ["--remove-label", ",".join(stale)]
    run(*args)

    reply = public_reply(v, bool(pr_url and pr_url.startswith("https://")))
    if reply:
        run("gh", "issue", "comment", issue, "-R", repo, "--body", reply)
    if v["dup"] or v["kind"] == "spam":
        run("gh", "issue", "close", issue, "-R", repo, "--reason", "not planned")
    print(json.dumps(v), pr_url or "")


if __name__ == "__main__":
    main()
