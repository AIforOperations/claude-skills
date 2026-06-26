"""Build the workflow work-list from a lead CSV.

--rows "26-69" or "1,5,9-12"  -> those rows.
omitted                       -> every row whose personalization_v2 is empty.

Schema-tolerant: accepts both the native column names (website, city, state,
contact_name, contact_title, niche) and the leads-finder/scrape_leads names
(company_website, company_city, company_state, first_name+last_name, job_title,
industry). Also passes the person + company LinkedIn URLs through to the agent.
"""
import argparse
import csv
import json


def pick(row, *names):
    """First non-empty value among the given column names."""
    for n in names:
        v = (row.get(n) or "").strip()
        if v:
            return v
    return ""


def contact_of(row):
    c = pick(row, "contact_name", "full_name")
    if c:
        return c
    fn, ln = pick(row, "first_name"), pick(row, "last_name")
    return (fn + " " + ln).strip()


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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--rows", default="")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    rows = list(csv.DictReader(open(a.csv, newline="", encoding="utf-8")))
    sel = parse_rows(a.rows) if a.rows else None

    leads = []
    for i, row in enumerate(rows, 1):
        if sel is not None:
            if i not in sel:
                continue
        elif pick(row, "personalization_v2", "personalization"):
            continue
        leads.append({
            "row": i,
            "company": pick(row, "company_name", "company"),
            "website": pick(row, "website", "company_website"),
            "city": pick(row, "city", "company_city"),
            "state": pick(row, "state", "company_state"),
            "contact": contact_of(row),
            "title": pick(row, "contact_title", "job_title"),
            "niche": pick(row, "niche", "industry"),
            "linkedin": pick(row, "linkedin", "linkedin_person"),
            "company_linkedin": pick(row, "company_linkedin", "linkedin_company"),
            "domain": pick(row, "company_domain", "domain"),
        })

    json.dump(leads, open(a.out, "w"), indent=2)
    print(f"{len(leads)} leads -> {a.out}")


if __name__ == "__main__":
    main()
