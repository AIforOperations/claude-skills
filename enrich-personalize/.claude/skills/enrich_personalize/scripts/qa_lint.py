"""Gate the personalization lines against the voice rules. Exit 1 on any failure.

Checks: no question mark, no em/en dash, no banned filler, starts with a
`hey {name},` greeting, core line (after the greeting) is <= 9 words.
Blank lines are treated as intentionally skipped (must carry a flag).
"""
import argparse
import csv
import re
import sys


def parse_rows(spec):
    sel = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            lo, hi = part.split("-")
            sel |= set(range(int(lo), int(hi) + 1))
        else:
            sel.add(int(part))
    return sel


BANNED = [
    "seamlessly", "vibrant", "cutting-edge", "leverage", "robust", "transformative",
    "streamline", "delve", "foster", "utilize", "comprehensive", "harness", "elevate",
    "empower", "landscape", "paradigm", "synergy", "game-changer", "revolutionize",
    "innovative", "holistic", "optimize", "facilitate", "scalable", "ecosystem",
    "proactive", "actionable", "deep dive", "unlock", "next-level", "best-in-class",
    "end-to-end", "world-class",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--col", default="personalization_v2")
    ap.add_argument("--rows", default="", help="only check these rows, e.g. 1-50 (default: all)")
    a = ap.parse_args()

    rows = list(csv.DictReader(open(a.csv, newline="", encoding="utf-8")))
    sel = parse_rows(a.rows) if a.rows else None
    fails = 0
    blanks = 0
    seen = 0
    for i, row in enumerate(rows, 1):
        if sel is not None and i not in sel:
            continue
        seen += 1
        line = (row.get(a.col) or "").strip()
        if not line:
            blanks += 1
            if not (row.get("v2_qa_flag") or "").strip():
                fails += 1
                print(f"FAIL row {i}: blank line with no v2_qa_flag explaining why")
            continue
        errs = []
        if "?" in line:
            errs.append("question mark")
        if "—" in line or "–" in line:
            errs.append("em/en dash")
        low = line.lower()
        for b in BANNED:
            if re.search(r"\b" + re.escape(b) + r"\b", low):
                errs.append(f"banned:{b}")
        if not low.startswith("hey "):
            errs.append("missing 'hey <name>,' greeting")
        # strip the greeting, then exempt a trailing casual closer (<=3 words
        # after the last comma, e.g. ", that's super cool!") from the count.
        core = re.sub(r"^hey\s+[^,]+,\s*", "", line)
        m = re.match(r"^(.*),\s*([^,]{1,30})$", core)
        signal = m.group(1) if (m and len(m.group(2).split()) <= 3) else core
        wc = len(signal.split())
        if wc > 9:
            errs.append(f"signal {wc} words (>9, excl. closer)")
        if errs:
            fails += 1
            print(f"FAIL row {i}: {line}\n    -> {', '.join(errs)}")

    print(f"\n{seen - blanks} lines checked, {blanks} blank/skipped, {fails} failing")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
