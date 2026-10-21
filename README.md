<div align="center">

# Representation-Invariant Geometry of Quantity

### From emergent carry to a real self-adjoint realization

*A formally verified study of what remains invariant when the representation of quantity changes.*

[![Lean](https://img.shields.io/badge/Lean-4.32.0-blue)](https://lean-lang.org/)
[![CI](https://github.com/thiagomassensini/representation-invariant-quantity-geometry/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/thiagomassensini/representation-invariant-quantity-geometry/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-Apache--2.0-green.svg)](LICENSE)

</div>

---

## Guiding question

A quantity may be represented in many coordinate systems. Digits, bases, local states, residual labels, and finite encodings may all change.

This project asks:

> **Which structures belong to quantity itself, rather than to the coordinates used to represent it?**

The development begins before positional notation is assumed. Carry is derived as an emergent saturation/transport event, then used to build a representation-invariant hierarchical geometry.

The foundational chain is intended to culminate in the decomposition

$$
n=b^k m+a,
$$

with depth $k$, residual coordinate $a$, and a natural depth mass

$$
\mu_{b,k}=b^{-k}.
$$

A quadratic realization assigns an amplitude whose squared norm reproduces this mass,

$$
\lVert A_{b,k}\rVert^2=\mu_{b,k}.
$$

For a scaling family

$$
A_{b,k}^{(\theta)}\sim b^{-k\theta},
$$

quadratic compatibility forces

$$
b^{-2k\theta}=b^{-k},
$$

hence the unique representation-independent quadratic scaling exponent

$$
\boxed{\theta=\frac12}.
$$

This is the first rigidity landmark of the project.

---

## Formal trust boundary

The repository is intentionally split into two formal zones.

### I. `foundation/` — constructive core

The foundational spine is built without Mathlib or any external Lean package.
Its public capstone is required to satisfy:

```text
#print axioms ...
-- '<declaration>' does not depend on any axioms
```

The zero-axiom zone contains the route

$$
\text{distinguishability}
\longrightarrow
\text{finite local saturation}
\longrightarrow
\text{emergent carry}
\longrightarrow
\text{hierarchical decomposition}
\longrightarrow
\text{mass}
\longrightarrow
\text{quadratic amplitude}
\longrightarrow
\boxed{\theta=\tfrac12}.
$$

### II. `analysis/` — analytic and operator realization

After the foundational capstone, Mathlib is introduced explicitly and pinned.
The permitted logical surface is audited and restricted to the standard Lean/Mathlib proof principles used by the project.

The intended route is

$$
\text{real carry geometry}
\to
\text{Green reconstruction}
\to
\text{positive Gram structure}
\to
\text{Hilbert realization}
\to
\text{moments}
\to
\text{Hankel/Jacobi}
\to
\text{real self-adjoint operator}.
$$

No theorem in the foundational zone may silently cross this boundary.

---

## Repository architecture

```text
.
├── foundation/          # standalone Lean project; no external dependencies
├── analysis/            # Lean + pinned Mathlib; depends locally on foundation
├── paper/               # journal manuscript source
├── blueprint/           # LeanBlueprint formalization companion
├── docs/                # theorem index, standards, reproducibility
├── scripts/             # build and axiom audits
└── .github/workflows/   # reproducible CI
```

The repository is self-contained by design. The formal paper should be auditable from this repository alone.

---

## Canonical theorem map

Every major mathematical statement receives a stable paper identifier and a canonical Lean declaration.

| ID | Mathematical role | Lean declaration | Trust zone |
|---|---|---|---|
| `FND-001` | finite local capacity forces recurrence | planned | zero axioms |
| `FND-002` | emergence of a least local return | planned | zero axioms |
| `FND-003` | emergent cycle/residual decomposition | planned | zero axioms |
| `FND-004` | saturation transports one unit upward | planned | zero axioms |
| `FND-005` | depth mass $\mu_{b,k}=b^{-k}$ | planned | zero axioms |
| `FND-006` | quadratic amplitude law | planned | zero axioms |
| `FND-007` | uniqueness of $\theta=\tfrac12$ | planned | zero axioms |
| `FND-008` | base-change invariance of the half-scaling law | planned | zero axioms |
| `GEO-001` | real geometric state and transport | planned | audited Mathlib |
| `GEO-002` | exact Green reconstruction | planned | audited Mathlib |
| `HIL-001` | positive Gram/Hilbert carrier | planned | audited Mathlib |
| `SPC-001` | canonical Hankel/Jacobi realization | planned | audited Mathlib |
| `OPR-001` | real maximal self-adjoint realization | planned | audited Mathlib |

The complete live map is maintained in [`THEOREM_INDEX.md`](THEOREM_INDEX.md).

---

## Paper ↔ Lean correspondence

The journal paper and the formalization are linked in two complementary ways:

1. **Stable theorem IDs** (`FND-007`, `OPR-001`, …) are used in the manuscript and theorem index.
2. **LeanBlueprint** records the exact Lean declaration for each formalized statement with `\lean{...}`, proof completion with `\leanok`, and mathematical dependencies with `\uses{...}`.

This separates human-readable theorem numbering from implementation names while keeping the correspondence machine-checkable.

---

## Reproducibility contract

A release intended for citation must satisfy all of the following:

- both Lean projects build from clean checkout;
- the foundational axiom audit is empty;
- the analytic axiom audit contains only the explicit allowlist;
- no `sorry`, `admit`, or custom `axiom` declaration occurs in the proof spine;
- LeanBlueprint declaration checks pass;
- the theorem index matches the manuscript and source declarations;
- CI runs independent checking with Lean's checker and `nanoda` where supported;
- toolchain and dependencies are pinned for the release.

See [`docs/FORMALIZATION_STANDARD.md`](docs/FORMALIZATION_STANDARD.md) and [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md).

---

## Terminology

**Carry** is retained for the discrete saturation event: a local coordinate exhausts its capacity and transports one unit to the next level.

**Transport** is used for the broader geometric law that moves conserved quantity across levels or representations.

This distinction keeps the familiar computational meaning of carry while giving the later geometry a representation-independent language.

---

## Project status

The repository structure and publication standard are fixed first. Mathematical results are migrated only after they are restated in the new representation-invariant language and re-audited inside this repository.

The first milestone is the zero-axiom foundational capstone ending at

$$
\boxed{\theta=\frac12}.
$$

The second milestone is the real self-adjoint realization constructed entirely downstream of the geometry.

---

## License

Lean source and repository infrastructure are released under the Apache License 2.0. Manuscript licensing can be specified separately at submission/release time.
