# Minimum Viable Harness Contract

El Harness es el enforcement layer del workflow; no es un agente de negocio.

## Required stages

1. `load_context` — cargar sólo artefactos relevantes.
2. `classify` — determinar tipo/riesgo de trabajo.
3. `authorize` — resolver permisos y Human Gates.
4. `route` — seleccionar Agent y Skills.
5. `plan` — establecer pasos y criterios.
6. `execute` — realizar acciones autorizadas.
7. `verify` — ejecutar tests/evals aplicables.
8. `review` — revisión cuando riesgo/policy lo requiera.
9. `evidence` — producir evidencia estructurada.
10. `update_state` — reflejar resultado real.

## Invariants

- `execute` MUST NOT occur while a required Human Gate is unresolved.
- `done` MUST NOT occur without required Evidence.
- Policy cannot be expanded implicitly.
- Failure cannot be converted to success by changing acceptance criteria.
- Every transition must be auditable.
