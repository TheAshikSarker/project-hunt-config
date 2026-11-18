"""Checks sources.json before the app ever sees it. Run: python3 scripts/validate.py"""
import json
import sys

SUPPORTED = {"ATS_LEVER", "ATS_GREENHOUSE", "ATS_RECRUITEE", "ATS_ASHBY", "BOARD_REMOTIVE", "RSS"}
KNOWN = SUPPORTED | {"ATS_WORKABLE", "ATS_SMARTRECRUITERS", "ATS_WORKDAY", "HTML", "REDDIT", "UPWORK", "MANUAL"}

def main(path="sources.json"):
    errors, warnings = [], []
    try:
        data = json.load(open(path, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        print(f"ERROR: {path} is not valid JSON: {e}")
        return 1
    if data.get("schemaVersion") != 1:
        errors.append("schemaVersion must be 1 (newer versions are ignored by current app builds)")
    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("'sources' must be a non-empty list")
        sources = []
    seen = set()
    for i, s in enumerate(sources):
        sid = s.get("id", f"#{i}")
        if not s.get("id") or not s.get("name"):
            errors.append(f"{sid}: id and name are required")
        if sid in seen:
            errors.append(f"{sid}: duplicate id")
        seen.add(sid)
        t = s.get("type")
        if t not in KNOWN:
            errors.append(f"{sid}: unknown type {t!r}")
        elif t not in SUPPORTED:
            warnings.append(f"{sid}: type {t} has no adapter yet, the app will show it as not supported")
        if t and t.startswith("ATS_") and not s.get("slug"):
            errors.append(f"{sid}: ATS sources need a 'slug'")
        if t in {"RSS", "HTML"} and not str(s.get("url", "")).startswith("https://"):
            errors.append(f"{sid}: {t} sources need an https 'url'")
        if t == "BOARD_REMOTIVE" and not s.get("keywords"):
            warnings.append(f"{sid}: no keywords, the app will search 'bengali'")
        h = s.get("fetchIntervalHours", 6)
        if not isinstance(h, int) or not 1 <= h <= 168:
            errors.append(f"{sid}: fetchIntervalHours must be a whole number from 1 to 168")
        if not s.get("notes"):
            warnings.append(f"{sid}: add 'notes' saying what was checked")
    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("ERROR:", e)
    print(f"{len(sources)} sources, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
