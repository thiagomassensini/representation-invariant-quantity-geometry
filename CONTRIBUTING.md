# Contributing

This project is theorem-index driven.

A pull request changing mathematical content should:

1. identify the affected theorem IDs;
2. state whether it changes assumptions, statement, proof, or only implementation;
3. add/update Lean declarations;
4. update the theorem index;
5. update the blueprint mapping;
6. preserve the appropriate axiom policy;
7. pass `--wfail` builds and axiom audits.

No release theorem is accepted with `sorry`, `admit`, or an undocumented custom axiom.
