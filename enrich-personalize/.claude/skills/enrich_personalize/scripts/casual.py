"""Casual-name conventions for cold-email greetings. Conservative on purpose:
the lead-enricher agent returns the name a person actually goes by, so this is
only a fallback. Overrides always win."""
import re

# Only near-universal short forms. Risky ones (Michael->Mike, Daniel->Dan) are
# intentionally omitted; pass an override when you have confirmed the nickname.
NICKNAMES = {
    "jeffrey": "Jeff", "steven": "Steve", "stephen": "Steve", "william": "Bill",
    "gregory": "Greg", "kenneth": "Ken", "thomas": "Tom", "nicholas": "Nick",
    "ronald": "Ron", "edward": "Ed", "timothy": "Tim",
}

_LEGAL = re.compile(
    r"[,\s]+(?:inc|incorporated|llc|l\.l\.c\.|llp|pllc|p\.c\.|pc|ltd|co|corp|"
    r"corporation|company)\.?$",
    re.I,
)


def casual_first(first_name, override=None):
    if override:
        return override.strip()
    fn = (first_name or "").strip()
    if not fn:
        return ""
    return NICKNAMES.get(fn.lower(), fn)


def casual_company(name, override=None):
    if override:
        return override.strip()
    s = (name or "").strip()
    if not s:
        return ""
    for sep in (" - ", " — ", " | ", " – "):
        if sep in s:
            s = s.split(sep)[0]
    s = re.split(r"\s*\(", s)[0]            # drop "(...)"
    s = re.sub(r"^the\s+", "", s, flags=re.I)
    prev = None
    while prev != s:                         # strip trailing legal tokens repeatedly
        prev = s
        s = _LEGAL.sub("", s).strip().rstrip(",").strip()
    parts = s.split()
    if len(parts) > 1 and parts[-1].lower() in ("group", "companies", "company"):
        s = " ".join(parts[:-1])
    return s.strip()
