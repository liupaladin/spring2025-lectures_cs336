#!/usr/bin/env python3
"""Generate the progress tracker markdown table in README.md from progress.json.

Fixes table alignment and supports 17 lectures by default.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
PROG_FILE = ROOT / "progress.json"
TOTAL_LECTURES = 17
BAR_WIDTH = 10


def render_table(progress: dict, users=None, total=TOTAL_LECTURES) -> str:
    if users is None:
        users = list(progress.keys()) or ["User 1", "User 2", "User 3"]
    lines = []
    # Header
    lines.append("| User | Progress | " + " | ".join(f"L{i+1}" for i in range(total)) + " |")
    # Separator: ensure there's a pipe between every column
    lec_separators = "|".join(":--:" for _ in range(total))
    lines.append("|---|---:|" + lec_separators + "|")
    # Rows
    for user in users:
        finished = int(progress.get(user, 0) or 0)
        finished = max(0, min(finished, total))
        pct = round((finished / total) * 100) if total else 0
        filled = int(round((pct / 100) * BAR_WIDTH))
        bar = "▰" * filled + "▱" * (BAR_WIDTH - filled)
        lec_cells = " | ".join("🟩" if i < finished else "⬜" for i in range(total))
        lines.append(f"| {user} | {pct}% {bar} | {lec_cells} |")
    return "\n".join(lines)


def regenerate_readme():
    text = README.read_text(encoding="utf-8")
    if not PROG_FILE.exists():
        PROG_FILE.write_text(json.dumps({"User 1": 0, "User 2": 0, "User 3": 0}, indent=2))
    progress = json.loads(PROG_FILE.read_text(encoding="utf-8"))
    users = list(progress.keys())
    table_md = render_table(progress, users=users, total=TOTAL_LECTURES)
    start_marker = "<!-- PROGRESS-START -->"
    end_marker = "<!-- PROGRESS-END -->"
    if start_marker in text and end_marker in text:
        before, rest = text.split(start_marker, 1)
        _, after = rest.split(end_marker, 1)
        new_section = start_marker + "\n" + table_md + "\n" + end_marker
        new_text = before + new_section + after
        README.write_text(new_text, encoding="utf-8")
        print(f"Regenerated progress table for {len(users)} users, {TOTAL_LECTURES} lectures.")
    else:
        print("Markers not found in README.md — please add <!-- PROGRESS-START --> and <!-- PROGRESS-END --> markers.")


if __name__ == "__main__":
    regenerate_readme()
