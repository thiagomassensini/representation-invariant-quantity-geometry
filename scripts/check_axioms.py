#!/usr/bin/env python3
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

ALLOWED_ANALYSIS = {"propext", "Classical.choice", "Quot.sound"}

p = argparse.ArgumentParser()
p.add_argument("--mode", choices=["foundation", "analysis"], required=True)
p.add_argument("log", type=Path)
a = p.parse_args()
text = a.log.read_text(encoding="utf-8", errors="replace")

bad = []
for line in text.splitlines():
    if "depends on axioms:" not in line:
        continue
    m = re.search(r"depends on axioms:\s*\[(.*)\]", line)
    if not m:
        bad.append((line, {"<unparsed>"}))
        continue
    names = {x.strip() for x in m.group(1).split(",") if x.strip()}
    if a.mode == "foundation":
        if names:
            bad.append((line, names))
    else:
        extra = names - ALLOWED_ANALYSIS
        if extra:
            bad.append((line, extra))

for forbidden in ("sorryAx",):
    if forbidden in text:
        bad.append((f"forbidden trust escape: {forbidden}", {forbidden}))

if bad:
    print("AXIOM AUDIT FAILED", file=sys.stderr)
    for line, names in bad:
        print(f"- {line}\n  offending: {sorted(names)}", file=sys.stderr)
    raise SystemExit(1)

print(f"axiom audit passed ({a.mode})")
