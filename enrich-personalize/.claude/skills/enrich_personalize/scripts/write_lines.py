"""Write personalization lines + casual columns into a lead CSV.

signals JSON = array of:
  {row:int, line:str, flag?:str, contact_name?:str, first_name?:str,
   casual_first_name?:str, casual_company_name?:str}
`line` must NOT include the greeting; this script prepends `hey {casual_first_name}, `.
"""
import argparse
import csv
import json
import os
import shutil
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from casual import casual_first, casual_company

NEW_COLS = ("personalization_v2", "v2_qa_flag", "casual_first_name", "casual_company_name")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--signals", required=True)
    ap.add_argument("--no-backup", action="store_true")
    a = ap.parse_args()

    sig = {int(s["row"]): s for s in json.load(open(a.signals))}
    with open(a.csv, newline="", encoding="utf-8") as fh:
        rd = csv.DictReader(fh)
        fields = list(rd.fieldnames)
        rows = list(rd)
    for c in NEW_COLS:
        if c not in fields:
            fields.append(c)

    if not a.no_backup:
        shutil.copy(a.csv, f"{a.csv}.backup_{int(time.time())}.csv")

    n = 0
    for i, row in enumerate(rows, 1):
        if i not in sig:
            continue
        s = sig[i]
        if s.get("contact_name") and "contact_name" in fields:
            row["contact_name"] = s["contact_name"]
        if s.get("first_name") and "first_name" in fields:
            row["first_name"] = s["first_name"]
        # name source: override -> signal/CSV first_name -> first token of contact_name
        # (so greetings never silently drop on a CSV that only has contact_name)
        raw_fn = (s.get("first_name") or row.get("first_name") or "").strip()
        if not raw_fn:
            cn = (s.get("contact_name") or row.get("contact_name") or "").strip()
            raw_fn = cn.split()[0] if cn else ""
        cfn = casual_first(raw_fn, s.get("casual_first_name"))
        ccn = casual_company(row.get("company_name", ""), s.get("casual_company_name"))
        # store lowercase so it renders lowercase when used as a merge tag in the all-lowercase email
        row["casual_first_name"] = cfn.lower()
        row["casual_company_name"] = ccn
        row["v2_qa_flag"] = s.get("flag", "") or ""
        line = (s.get("line") or "").strip()
        if line and cfn and not line.lower().startswith("hey "):
            line = f"hey {cfn.lower()}, {line}"
        row["personalization_v2"] = line
        n += 1

    with open(a.csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {n} rows into {a.csv}")


if __name__ == "__main__":
    main()
