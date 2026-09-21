# Theorem Index

This file is the canonical crosswalk between the paper, Lean source, blueprint, and axiom audit.

## Status vocabulary

- **planned** — statement agreed, not yet implemented in this repository.
- **ported** — implementation exists but has not completed the release audit.
- **verified** — builds, axiom audit passes, theorem is linked in the blueprint.
- **paper-ready** — verified and synchronized with the manuscript statement.

## Foundation — zero-axiom spine

| ID | Short name | Mathematical statement | Lean declaration | Status | Axioms |
|---|---|---|---|---|---|
| FND-001 | Local recurrence | Finite local observation of faithful unit dynamics must recur | — | planned | must be empty |
| FND-002 | Least return | Information-preserving local dynamics has a canonical least positive return | — | planned | must be empty |
| FND-003 | Cycle decomposition | Every step count has unique cycle/residual coordinates relative to emergent capacity | — | planned | must be empty |
| FND-004 | Carry emergence | First saturation resets the residual and transports exactly one unit upward | — | planned | must be empty |
| FND-005 | Depth mass | Depth $k$ carries mass $\mu_{b,k}=b^{-k}$ | — | planned | must be empty |
| FND-006 | Quadratic amplitude | Squared amplitude equals depth mass | — | planned | must be empty |
| FND-007 | Half-scaling rigidity | Quadratic compatibility uniquely forces $\theta=1/2$ | — | planned | must be empty |
| FND-008 | Base-change invariance | The half-scaling law is independent of the chosen radix/camera | — | planned | must be empty |

## Geometry and analysis

| ID | Short name | Mathematical role | Lean declaration | Status | Axiom policy |
|---|---|---|---|---|---|
| GEO-001 | Real state | Real representation of the native geometric state | — | planned | standard allowlist |
| GEO-002 | Transport covariance | Coordinate change preserves the native quadratic quantity | — | planned | standard allowlist |
| GEO-003 | Green reconstruction | Exact reconstruction from curvature/boundary data | — | planned | standard allowlist |
| GEO-004 | Log-jet readout | Multiplicative variation gives the native logarithmic readout | — | planned | standard allowlist |
| HIL-001 | Gram carrier | Native moments are represented by a positive Gram kernel | — | planned | standard allowlist |
| HIL-002 | Hilbert completion | The invariant quadratic data admits a canonical Hilbert realization | — | planned | standard allowlist |
| SPC-001 | Hankel positivity | Even and shifted moment towers are positive | — | planned | standard allowlist |
| SPC-002 | Jacobi realization | The moment tower determines canonical Jacobi sections | — | planned | standard allowlist |
| OPR-001 | Energy operator | The operator is constructed from the geometric energy factor | — | planned | standard allowlist |
| OPR-002 | Real self-adjointness | The resulting real operator is maximal self-adjoint | — | planned | standard allowlist |

## Rule

No paper theorem may be marked `paper-ready` unless its row contains a concrete Lean declaration and the matching CI audit is green.
