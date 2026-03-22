#!/usr/bin/env python3
"""Helper to set a user's finished lecture and regenerate README table."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROG_FILE = ROOT / "progress.json"


def load_progress():
    if not PROG_FILE.exists():
        PROG_FILE.write_text(json.dumps({"User 1": 0, "User 2": 0, "User 3": 0}, indent=2))
    return json.loads(PROG_FILE.read_text(encoding="utf-8"))


def save_progress(p):
    PROG_FILE.write_text(json.dumps(p, indent=2))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--user", required=True, help="User name (e.g. 'User 1')")
    p.add_argument("--finished", required=True, type=int, help="Number of lectures finished (0..17)")
    args = p.parse_args()
    prog = load_progress()
    prog[args.user] = args.finished
    save_progress(prog)
    # regenerate README
    from scripts.generate_progress_table import regenerate_readme

    regenerate_readme()
    print(f"Set {args.user} finished to {args.finished} and regenerated README.md")


if __name__ == "__main__":
    main()
