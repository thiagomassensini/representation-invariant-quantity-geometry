# Formalization Standard

## 1. One repository, one audit surface

The paper must be auditable from this repository alone. Historical repositories may motivate migration work, but release theorems cannot depend on them.

## 2. Two trust zones

### Foundation

- No Mathlib.
- No external Lean package.
- No custom axioms.
- No `Classical.choice`, `propext`, `Quot.sound`, `sorryAx`, or equivalent hidden dependency.
- Each capstone declaration is checked with `#print axioms`.
- CI fails if any foundational declaration reports an axiom dependency.

### Analysis

- Mathlib is pinned.
- The allowed proof-principle surface is explicit and machine-audited.
- Release target: only `propext`, `Classical.choice`, and `Quot.sound` when genuinely inherited from Mathlib infrastructure.
- `sorryAx`, custom axioms, or additional trust escapes fail CI.

## 3. No hidden incompleteness

Forbidden in the release proof spine:

- `sorry`
- `admit`
- custom `axiom` declarations
- replacing a theorem by a numerical certificate without labeling it as such
- importing a historical project as a theorem dependency

## 4. Stable theorem identities

The paper uses stable identifiers such as `FND-007` and `OPR-002`.
Lean declarations retain semantic names. `THEOREM_INDEX.md` is the canonical bridge.

LeanBlueprint provides the machine-readable paper/source bridge:

```tex
\begin{theorem}[Quadratic half-scaling rigidity]
  \label{thm:FND-007}
  \lean{RIQGFoundation.quadraticHalfScaling_unique}
  \leanok
  \uses{def:depth-mass,def:quadratic-amplitude}
  ...
\end{theorem}
```

## 5. Mathematical statements before implementation details

Definitions are introduced in representation-invariant mathematical language first. Historical names, implementation adapters, and convenience encodings are secondary.

## 6. Exact status discipline

Every nontrivial result is labeled internally as one of:

- exact theorem;
- conditional theorem with named hypotheses;
- numerical audit;
- conjectural interpretation.

The paper may only state the first two as theorems.

## 7. Reproducible releases

Every cited release must pin:

- Lean toolchain;
- Mathlib revision;
- all other package revisions;
- workflow versions;
- manuscript source;
- blueprint source;
- theorem index.

A release tag should correspond to an immutable archival deposit.
