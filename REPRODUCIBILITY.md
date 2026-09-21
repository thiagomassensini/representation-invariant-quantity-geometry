# Reproducibility

A clean audit should be possible from a fresh clone.

## Foundation

```bash
cd foundation
lake build --wfail
lake env lean RIQGFoundation/Audit.lean | tee ../artifacts/foundation-axioms.txt
python ../scripts/check_axioms.py --mode foundation ../artifacts/foundation-axioms.txt
```

## Analysis

```bash
cd analysis
lake update
lake build --wfail
lake env lean RIQG/Audit.lean | tee ../artifacts/analysis-axioms.txt
python ../scripts/check_axioms.py --mode analysis ../artifacts/analysis-axioms.txt
```

## Blueprint

The release workflow will run LeanBlueprint declaration checks so each `\lean{...}` reference resolves to an actual declaration.

## Independent checking

CI is configured to use Lean's standard checking pipeline and should enable independent checking (`nanoda`) on release candidates where supported.
