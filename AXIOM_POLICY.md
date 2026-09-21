# Axiom Policy

## Foundation boundary

All declarations through the half-scaling rigidity theorem are required to have an empty axiom surface.

The audit criterion is literal:

```text
'<declaration>' does not depend on any axioms
```

The foundational project has no external package dependency.

## Analysis boundary

After the foundational capstone, the analytic project may use pinned Mathlib.
The release allowlist is:

```text
propext
Classical.choice
Quot.sound
```

Any additional axiom dependency is a release blocker until explicitly investigated and documented.

## Prohibited trust escapes

```text
sorryAx
custom axiom declarations
untracked generated theorem certificates
```
