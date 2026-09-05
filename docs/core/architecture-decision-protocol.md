# Architecture Decision Protocol

Architecture is derived from requirements and constraints; it is not a template default.

```mermaid
flowchart TD
  R[Requirements] --> C[Constraints]
  C --> E[Environment]
  E --> N[Operational needs / complexity]
  N --> A[Candidate architectures]
  A --> X[Trade-offs]
  X --> REC[Recommendation]
  REC --> G{Significant / irreversible?}
  G -->|yes| H[Human Gate]
  G -->|no| I[Implement]
  H -->|approved| I
```

Distinguish explicitly: **Requirement != Constraint != Preference != Assumption**.

A recommendation records drivers, alternatives, trade-offs, reversibility and gate status. Approved architecture must not be silently replaced; a material replacement opens a new gate.
