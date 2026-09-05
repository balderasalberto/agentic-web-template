# Changelog

## v3.3
- Added structured Project Intake schema separating requirements, constraints, preferences, assumptions and unknowns.
- Added Architecture Decision Protocol and ADR schema.
- Added change classification and more precise Human Gate guidance.
- Defined Proposed -> Planned -> Implementing -> Implemented -> Verified -> Done lifecycle.
- Strengthened Evidence schema and no-fabricated-verification rule.
- Added Project Knowledge protocol and reusable application documentation templates.
- Added Mermaid architecture, lifecycle, traceability and progressive-context diagrams.
- Added knowledge index for minimal sufficient context.
- Added EVAL-009 through EVAL-018 for constraints, UI classification, real implementation, verification, architecture replacement, neutrality, knowledge/diagram consistency, progressive context and proportionality.
- Added Inventory E2E lessons without making the domain a Core dependency.

# Changelog

## 3.0.0 - Universal Core refactor

- Generalized the template from web applications to arbitrary software applications.
- Separated Core, Project artifacts and Examples conceptually.
- Removed Eventos Sociales knowledge from Core state and moved it to `examples/`.
- Added universal Architect, Developer, Tester and Reviewer contracts.
- Added Minimum Viable Harness contract.
- Added Task and Evidence schemas.
- Added initial behavioral Evals.
- Defined authoritative instruction hierarchy and extension rule.

## 3.1.0
- Added executable provider-neutral Python CLI (`agentic`).
- Added deterministic Policy/Human Gate enforcement.
- Added task routing and persistent `.agentic` state.
- Added Evidence-before-Done enforcement.
- Added executable behavioral eval runner.

## v3.2
- El Core deja de requerir Python o un CLI propio.
- El coding agent pasa a ser el ejecutor de la aplicación real.
- Se introduce contrato de Bootstrap greenfield/brownfield.
- Se añaden adapters iniciales para Codex y Claude Code.
- El Harness Python v3.1 se mueve a `prototypes/` y queda fuera del flujo normal.
- `init` ya no representa falsamente creación de una aplicación.
