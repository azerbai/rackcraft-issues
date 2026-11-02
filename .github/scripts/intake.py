"""Gathers everything triage needs into intake/, so the AI step needs no network or GitHub access.

intake/issue.md         the issue and its comments (untrusted text, written by the public)
intake/open_issues.md   other open issues (number, title, labels), for spotting duplicates
intake/logs/NN-<name>   attached logs and crash reports, from GitHub attachments, mclo.gs and pastebin only

Env: GH_TOKEN (read the issue), ISSUE (number), REPO (owner/name).
"""

import json
import os
import re
import subprocess
import urllib.request
from pathlib import Path

MAX_BYTES = 8 * 1024 * 1024
MAX_FILES = 6
OUT = Path("intake")


def gh(*args):
    return subprocess.run(["gh", *args], check=True, capture_output=True, text=True).stdout


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "rackcraft-triage"})
    with urllib.request.urlopen(request, timeout=30) as response:
        data = response.read(MAX_BYTES + 1)
    return data[:MAX_BYTES]


def log_urls(text):
    """Links to logs, from hosts we trust to serve plain files. Everything else is ignored."""
    urls = []
    for match in re.finditer(r"https://[^\s)\]>\"']+", text):
        url = match.group(0).rstrip(".,")
        if re.match(r"https://github\.com/(user-attachments/files|[^/]+/[^/]+/files)/\d+/", url):
            urls.append(url)
        elif m := re.match(r"https://(?:www\.)?mclo\.gs/([A-Za-z0-9]+)$", url):
            urls.append(f"https://api.mclo.gs/1/raw/{m.group(1)}")
        elif m := re.match(r"https://pastebin\.com/(?:raw/)?([A-Za-z0-9]+)$", url):
            urls.append(f"https://pastebin.com/raw/{m.group(1)}")
        elif re.match(r"https://gist\.githubusercontent\.com/", url):
            urls.append(url)
    return list(dict.fromkeys(urls))


def main():
    repo, number = os.environ["REPO"], os.environ["ISSUE"]
    issue = json.loads(gh("issue", "view", number, "-R", repo, "--json", "title,body,author,labels,comments"))
    (OUT / "logs").mkdir(parents=True, exist_ok=True)

    parts = [f"# #{number}: {issue['title']}", f"Reporter: {issue['author']['login']}",
             f"Labels: {', '.join(l['name'] for l in issue['labels']) or 'none'}", "", issue["body"] or ""]
    texts = [issue["body"] or ""]
    for comment in issue["comments"]:
        parts += ["", f"## Comment by {comment['author']['login']}", "", comment["body"]]
        texts.append(comment["body"])
    (OUT / "issue.md").write_text("\n".join(parts))

    others = json.loads(gh("issue", "list", "-R", repo, "--state", "open", "--limit", "200", "--json", "number,title,labels"))
    (OUT / "open_issues.md").write_text("\n".join(
        f"#{o['number']} [{', '.join(l['name'] for l in o['labels'])}] {o['title']}" for o in others if str(o["number"]) != number))

    saved = 0
    for url in log_urls("\n".join(texts)):
        if saved >= MAX_FILES:
            break
        try:
            data = fetch(url)
        except Exception as error:  # a dead link is the reporter's to fix; note it and go on
            print(f"couldn't fetch {url}: {error}")
            continue
        name = re.sub(r"[^A-Za-z0-9._-]", "_", url.rsplit("/", 1)[-1])[:60] or "log"
        saved += 1
        (OUT / "logs" / f"{saved:02d}-{name}").write_bytes(data)
    print(f"intake: {len(issue['comments'])} comment(s), {saved} log file(s)")


if __name__ == "__main__":
    main()
