# Universal Agent Rules

Este archivo define reglas comunes a todos los agentes. Los contratos en `agents/` sólo especializan responsabilidades.

1. Cargar únicamente el contexto necesario para la tarea.
2. Respetar la Policy efectiva antes de cualquier acción.
3. No inventar requisitos, permisos, credenciales, restricciones ni resultados.
4. Representar incertidumbre material como `PENDING` o supuesto explícito y reversible.
5. Ejecutar tareas rutinarias autorizadas sin confirmaciones repetitivas.
6. No atravesar un Human Gate sin aprobación válida.
7. Preferir cambios pequeños, cohesivos, reversibles y trazables.
8. Usar la solución y patrón más simples que satisfagan los requisitos.
9. Verificar antes de declarar éxito.
10. Registrar evidencia y actualizar estado cuando corresponda.
11. Escalar cuando falte autoridad, información crítica o exista riesgo no cubierto.
12. No introducir conocimiento de un dominio, framework o proveedor en el Core; encapsularlo en Project, Skill, Adapter o Tool.

## Bootstrap universal

13. Si `PROJECT-SPEC.md` no existe, seguir `.agentic-template/BOOTSTRAP.md` antes de implementar.
14. La intención inicial debe materializarse en el repositorio real; registrar estado no equivale a crear la aplicación.
15. Detectar greenfield/brownfield por evidencia del repositorio, no por suposiciones.
16. El coding agent es intercambiable; ningún adapter puede redefinir Policy, Gates o criterios de Done.

## v3.3 Knowledge and execution rules

17. Distinguish requirements, constraints, preferences and assumptions during intake; never silently promote one category into another.
18. Derive architecture from requirements, constraints, environment and operational needs; record material alternatives/trade-offs and obtain a new gate before materially replacing approved architecture.
19. Classify changes when classification affects authority, verification or knowledge impact. Routine UI/refactor work must not be escalated as architecture change without material architectural impact.
20. `IMPLEMENTED` requires real implementation artifacts; `VERIFIED` requires executed verification; `DONE` requires sufficient Evidence and assessment/update of impacted Project Knowledge.
21. Maintain useful Project Knowledge for generated/evolved applications: purpose, actors, requirements, use cases, business rules, architecture/ADRs, operations and other context when applicable.
22. Mermaid diagrams are first-class Project Knowledge. Keep diagrams for architecture, persistent data models, critical flows, states, integrations or deployment when they materially improve understanding.
23. Documentation must be progressive and non-redundant: overview first, detail on demand. Context resolution should prefer the knowledge index and load only task-relevant knowledge plus necessary code.
24. Behavior, architecture, data-model or critical-flow changes must assess corresponding documentation and diagram impact before `DONE`.
