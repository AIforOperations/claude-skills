"""Casual-name conventions for cold-email greetings. Conservative on purpose:
the lead-enricher agent returns the name a person actually goes by, so the
nickname map is only a fallback. Overrides always win.

casual_company also: drops legal/credential suffixes (Inc, LLC, LLP, PC, CPA,
CPAs, EA, PA, incl. dotted forms like L.l.p.), drops a tagline after a separator,
drops a trailing ", a/an <descriptor>" tail, uppercases known acronyms (HOA, ADU,
IRS, CPA, MMI, ...), and collapses a firm named after the contact to
"your practice".
"""
import re

# Only near-universal short forms. Risky ones (Michael->Mike, Daniel->Dan) are
# intentionally omitted; pass an override when you have confirmed the nickname.
NICKNAMES = {
    "jeffrey": "Jeff", "steven": "Steve", "stephen": "Steve", "william": "Bill",
    "gregory": "Greg", "kenneth": "Ken", "thomas": "Tom", "nicholas": "Nick",
    "ronald": "Ron", "edward": "Ed", "timothy": "Tim",
}

# Standalone tokens to force UPPERCASE when they survive cleaning. Curated on
# purpose (a blind all-consonant rule mangles St./Dr./Mt.). Extend as needed.
ACRONYMS = {
    "HOA", "ADU", "IRS", "CPA", "GIS", "EHS", "MMI", "RRS", "MTX", "KSA", "LDA",
    "NES", "ZC", "AMD", "EIC", "GSI", "ATL", "CDMS", "RSI", "TKG", "JH", "SK",
    "AB", "NA", "KP", "DG", "KMEA", "BMH", "BND", "SVA", "NAC", "PRA", "OMM",
    "HDS", "LCDG", "CFO", "HR", "PSBS", "MJF", "AHP", "ICS",
}

# Trailing legal / credential tokens to drop (letters compared after stripping dots).
_LEGAL_WORDS = {
    "inc", "incorporated", "llc", "llp", "pllc", "pc", "ltd", "lp", "co", "corp",
    "corporation", "company", "cpa", "cpas", "ea", "pa", "apc", "aps",
}


def casual_first(first_name, override=None):
    if override:
        return override.strip()
    fn = (first_name or "").strip()
    if not fn:
        return ""
    return NICKNAMES.get(fn.lower(), fn)


def _alpha_tokens(s):
    return re.findall(r"[A-Za-z]+", (s or "").lower())


def _strip_trailing_legal(s):
    # repeatedly drop a trailing legal/credential token (tolerating dots: L.l.p.)
    changed = True
    while changed:
        changed = False
        m = re.search(r"[,\s]+([A-Za-z.&']+)\.?$", s)
        if m:
            tok = re.sub(r"[^a-z]", "", m.group(1).lower())
            if tok in _LEGAL_WORDS:
                s = s[:m.start()].rstrip(" ,.&")
                changed = True
    return s


def _uppercase_acronyms(s):
    out = []
    for tok in s.split(" "):
        core = re.sub(r"[^A-Za-z]", "", tok)
        if core and core.upper() in ACRONYMS and core != core.upper():
            tok = tok.replace(core, core.upper())
        out.append(tok)
    return " ".join(out)


def casual_company(name, override=None, contact_name=None):
    if override:
        return override.strip()
    s = (name or "").strip()
    if not s:
        return ""
    for sep in (" - ", " — ", " | ", " – ", " -- "):
        if sep in s:
            s = s.split(sep)[0]
    s = re.split(r"\s*\(", s)[0]                       # drop "(...)"
    s = re.sub(r"^the\s+", "", s, flags=re.I)          # drop leading "The"
    s = re.sub(r",\s+an?\s+.*$", "", s, flags=re.I)    # drop ", a/an <descriptor>" tail
    s = _strip_trailing_legal(s)
    parts = s.split()
    # drop a trailing generic Group/Companies/Company only if a 2+ word brand remains
    # (so "Avalon Management Group" -> "Avalon Management" but "JH Group" stays "JH Group")
    if len(parts) > 2 and parts[-1].lower() in ("group", "companies", "company"):
        s = " ".join(parts[:-1])
    s = s.strip().rstrip(",").strip()
    s = _uppercase_acronyms(s)
    # a firm named after the contact: the firm name is a subset of their name AND
    # carries both first + last (>=2 shared tokens), so a shared surname alone
    # ("Henderson", "Muller") is NOT treated as a namesake solo firm.
    if contact_name:
        comp = set(t for t in _alpha_tokens(s) if len(t) > 1)
        nm = set(t for t in _alpha_tokens(contact_name) if len(t) > 1)
        if comp and nm and comp <= nm and len(comp & nm) >= 2:
            return "your practice"
    return s.strip()
