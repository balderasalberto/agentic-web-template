# AGENTIC WEB TEMPLATE — SPECIFICATION v2.0

**Estado:** Base para implementación y validación  
**Propósito:** Template GitHub agnóstico para construir, evolucionar, refactorizar y modernizar aplicaciones web mediante ingeniería asistida por agentes de IA.

## 1. Propósito

El Agentic Web Template proporciona una base reutilizable para proyectos web nuevos y existentes.

Debe permitir:
- Crear aplicaciones desde cero.
- Evolucionar aplicaciones existentes.
- Refactorizar código de forma incremental.
- Modernizar tecnologías y arquitectura.
- Trabajar con distintos lenguajes, frameworks, proveedores de IA e infraestructuras.
- Utilizar Demo, MVP, Staging y Producción.
- Automatizar progresivamente commits, PRs, CI/CD y despliegues.
- Mantener al humano en control de decisiones críticas.
- Incorporar continuamente mejoras provenientes de investigación.

El template representa una metodología y sistema operativo de desarrollo agentico, no una arquitectura tecnológica concreta.

## 2. Principios

1. SPEC antes de implementación.
2. La arquitectura se decide con base en requisitos.
3. La tecnología es intercambiable.
4. La complejidad debe estar justificada.
5. Demo temprana y verificable.
6. Tests desde el desarrollo.
7. Evals para comportamiento agentico.
8. Agents, Skills, Prompts, Instructions y Hooks tienen responsabilidades distintas.
9. El contexto debe ser el mínimo suficiente.
10. Las reglas críticas deben automatizarse cuando sea posible.
11. El agente debe preguntar ante ambigüedad o riesgo relevante.
12. Las decisiones importantes deben quedar registradas.
13. La IA no debe inventar requisitos ni decisiones críticas.
14. El código debe aplicar los patrones de diseño y arquitectura apropiados.
15. No se deben introducir patrones ni abstracciones innecesarias.
16. Los cambios deben ser trazables hasta requisitos.
17. El comportamiento existente debe preservarse durante refactorizaciones salvo cambio explícito.
18. Toda tarea terminada debe tener evidencia verificable.
19. El sistema debe poder detenerse y escalar a un humano.
20. El template debe evolucionar mediante investigación y validación real.

## 3. Alcance

### Greenfield
IDEA → SPEC → ARCHITECTURE → DEMO → DEVELOPMENT → TEST → REVIEW → CI/CD → VALIDATION → RELEASE

### Brownfield
AUDIT → BASELINE → TECHNICAL DEBT → REFACTOR/MODERNIZATION PLAN → INCREMENTAL CHANGE → TEST → REVIEW → CI/CD → VALIDATION

Ambos caminos utilizan el mismo núcleo agentico.

## 4. Agnosticismo

El template no impone lenguaje, framework, frontend, backend, base de datos, proveedor de IA, hosting, cloud, autenticación o arquitectura.

Arquitecturas soportadas conceptualmente:
- Monolito.
- Monolito modular.
- Microservicios.
- Serverless.
- Híbrida.

La arquitectura se selecciona mediante análisis de requisitos y se registra cuando sea significativa.

## 5. Agentic Core

Componentes:
- SPEC
- Project Instructions
- Agents
- Skills
- Prompts
- Harness
- Hooks
- Tests
- Evals
- Playbooks
- Human Gates
- GitHub/CI

Definiciones:
- **Instruction:** regla general y persistente.
- **Prompt:** solicitud reutilizable para una tarea.
- **Agent:** entidad especializada con responsabilidad y límites definidos.
- **Skill:** conocimiento, procedimiento, recursos o herramientas reutilizables.
- **Hook:** acción o control determinista ejecutado en un punto definido.
- **Harness:** coordinación de contexto, workflow, validación, permisos, checkpoints, recuperación y auditoría.
- **Eval:** evaluación del comportamiento del agente o sistema agentico.
- **Playbook:** procedimiento operativo para un escenario concreto.

## 6. Estructura de referencia

```text
agentic-web-template/
├── README.md
├── SPEC.md
├── AGENTS.md
├── PROJECT-STATE.md
├── PROJECT-POLICY.md
├── CHANGELOG.md
├── docs/
│   ├── 00-getting-started.md
│   ├── 01-manual-paso-a-paso.md
│   ├── 02-metodologia.md
│   ├── 03-arquitectura.md
│   ├── 04-testing.md
│   ├── 05-agentes.md
│   ├── 06-skills.md
│   ├── 07-harness.md
│   ├── 08-demo.md
│   ├── 09-github.md
│   ├── 10-seguridad.md
│   ├── 11-deployment.md
│   ├── 12-troubleshooting.md
│   ├── glossary/GLOSSARY.md
│   ├── scenarios/
│   └── adr/
├── .github/
│   ├── copilot-instructions.md
│   ├── agents/
│   ├── prompts/
│   ├── skills/
│   ├── hooks/
│   ├── workflows/
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
├── agents/
├── skills/
├── prompts/
├── harness/
├── playbooks/
├── capabilities/
│   └── existing-project/
│       ├── audit/
│       ├── refactoring/
│       ├── modernization/
│       └── migration/
├── demo/
├── contracts/
├── adapters/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── evals/
│   ├── agents/
│   ├── requirements/
│   └── quality/
└── research/
    ├── README.md
    ├── radar.md
    ├── decisions.md
    └── archive/
```

Las ubicaciones concretas pueden adaptarse al proveedor de agentes, conservando el modelo conceptual.

## 7. Interacción

La interacción debe ser eficaz, amigable, progresiva, breve cuando sea posible, explicativa cuando sea necesario y orientada a decisiones.

### Progressive Disclosure
1. Obtener información mínima.
2. Proponer.
3. Detectar información faltante.
4. Preguntar solamente lo necesario.
5. Continuar.

### Preguntas inteligentes
La IA debe recomendar una opción cuando pueda.

### Respuestas rápidas
Cuando la interfaz lo permita:
- Sí, continuar.
- Modificar.
- Explicar.
- Volver.
- Detener.

El usuario siempre puede responder en lenguaje natural.

### Nivel de explicación
- Directo.
- Breve.
- Detallado.
- Experto.

## 8. Interaction Policy

```text
IF routine_task
    → EXECUTE

IF ambiguity
    → ASK

IF architectural_decision
    → PROPOSE + ASK

IF security_risk
    → BLOCK + HUMAN GATE

IF production_change
    → HUMAN GATE

IF test_failure
    → DIAGNOSE → FIX → RETEST

IF repeated_failure
    → ASK HUMAN

IF missing_critical_information
    → ASK

IF assumption_is_low_risk
    → ASSUME + DOCUMENT
```

## 9. Project Policy

Debe configurarse al comenzar:
- modo de interacción;
- nivel de autonomía;
- ambientes permitidos;
- acciones autorizadas;
- Human Gates;
- nivel de explicación;
- reglas de seguridad;
- reglas de despliegue.

La política se almacena para evitar repetir decisiones.

## 10. Modos de interacción

- **Tutor:** explica y pregunta frecuentemente.
- **Colaborador:** ejecuta tareas rutinarias y consulta decisiones importantes.
- **Supervisor:** ejecuta la mayoría de tareas y consulta excepciones.
- **Autónomo:** ejecuta ciclos completos dentro de límites y Human Gates.
- **Personalizado:** política específica.

El modo puede cambiar temporalmente durante una tarea.

## 11. Niveles de autonomía

Autonomía e interacción son dimensiones independientes.

- **L0:** solo propone.
- **L1:** implementa, pero Git importante es manual.
- **L2:** puede crear commits y PRs.
- **L3:** puede ejecutar CI y desplegar Demo/Staging.
- **L4:** puede corregir iterativamente hasta satisfacer validaciones.
- **L5:** automatización avanzada, limitada por políticas y Human Gates.

## 12. Human Gates

Intervención humana mínima para:
- cambios arquitectónicos significativos;
- cambios de requisitos;
- cambios críticos de datos;
- seguridad;
- acciones productivas;
- incremento relevante de costos;
- cambios de contratos públicos;
- situaciones no contempladas con riesgo significativo.

## 13. Agents

Agentes iniciales:
- Architect
- Developer
- Tester
- Reviewer
- Documentation
- Refactoring/Audit

Cada agente define responsabilidad, límites, inputs, outputs, herramientas permitidas, Skills requeridas y condiciones de escalamiento.

## 14. Skills

Las Skills contienen conocimiento especializado reutilizable y se cargan selectivamente.

Ejemplos:
- architecture
- development
- testing
- security
- documentation
- refactoring
- migration
- github
- deployment

## 15. Design Patterns Policy

La programación debe apegarse a los patrones de diseño y arquitectura que apliquen al problema.

> **Use the simplest appropriate pattern.**

El agente debe identificar patrones candidatos, justificar su uso, comprobar que agregan valor, evitar sobreingeniería y priorizar cohesión, bajo acoplamiento, mantenibilidad y testabilidad.

Podrán utilizarse, cuando corresponda, SOLID, GoF, Repository, Factory, Strategy, Adapter, Observer, Dependency Injection, MVC/MVVM, Hexagonal, Clean Architecture, CQRS, Event-driven y patrones de integración.

## 16. SPEC

La SPEC es la fuente de verdad del proyecto.

Debe contener, cuando corresponda:
- objetivo;
- alcance;
- usuarios;
- requisitos funcionales;
- requisitos no funcionales;
- restricciones;
- criterios de aceptación;
- riesgos;
- decisiones pendientes.

Trazabilidad:

```text
Requirement
→ Acceptance Criteria
→ Test/Eval
→ Implementation
→ Evidence
```

## 17. ADR

Las decisiones significativas deben registrar contexto, alternativas, decisión, razones, consecuencias y estado.

## 18. Demo

La Demo es obligatoria para el MVP cuando técnicamente sea viable. Debe servir para validar requisitos, mostrar progreso, ejecutar E2E y obtener feedback temprano.

## 19. Microservicios

Los microservicios no son requisito. El Architect Agent debe considerar límites de dominio, escalabilidad, independencia de despliegue, complejidad operativa, consistencia de datos, observabilidad, costo y madurez del proyecto.

Una aplicación pequeña no debe convertirse en microservicios sin razón demostrable.

## 20. Contracts y Adapters

Permiten separar Demo, servicios reales o tecnologías alternativas y sustituir infraestructura sin reescribir innecesariamente la lógica.

## 21. Testing

Mínimo:
- Unit tests.
- Integration tests cuando correspondan.
- E2E para flujos relevantes.

## 22. Evals

Verifican comportamiento agentico: respeto a SPEC, preguntas ante decisiones críticas, uso correcto de Skills, límites del agente, cambios mínimos, tests, patrones, arquitectura, documentación y escalamiento.

## 23. Harness

Coordina Context, Workflow, Permissions, Hooks, Checkpoints, Validation, Recovery, Audit y Human Gates.

```text
Task → Context → Plan → Checkpoint → Execute → Validate → Review → Done
```

En fallo:

```text
Failure → Diagnose → Correct → Retest → Validate
```

## 24. Hooks

Controles automáticos para tests, permisos, formato, bloqueo de producción, registro de eventos y condiciones de despliegue.

## 25. GitHub Workflow

```text
Task → Branch → Implementation → Tests → Commit → Pull Request → CI → Review → Merge → Deploy → Validation
```

La automatización depende de PROJECT-POLICY.

## 26. Loop hasta satisfacción

```text
SPEC
 ↓
Implement
 ↓
Test
 ↓
Commit
 ↓
PR
 ↓
CI
 ↓
Deploy Demo/Staging
 ↓
E2E/Eval
 ↓
Acceptance Criteria
 ↓
¿Cumple?
 ├── NO → Diagnose → Fix → Retest
 └── YES → VERIFIED
```

La condición de finalización es evidencia.

## 27. Definition of Done

Una tarea termina cuando el requisito y criterios de aceptación están satisfechos, tests y Evals relevantes aprobados, revisión realizada, documentación actualizada, CI aprobada, sin bloqueadores conocidos y con evidencia disponible.

## 28. Project State

`PROJECT-STATE.md` conserva proyecto, versión, fase, arquitectura, feature, tarea, completado, bloqueadores, decisiones pendientes, última validación y siguiente paso.

## 29. Playbooks

Procedimientos para requirements, architecture, development, testing, demo, GitHub, deployment e incidents.

Formato:

```text
Detect → Diagnose → Classify → Propose → Act → Validate → Recover/Escalate
```

## 30. Existing Project Modernization

### Audit
Analizar tecnología, arquitectura, dependencias, código, tests, seguridad, CI/CD, deuda y documentación.

### Baseline
Determinar comportamiento actual antes de modificar.

### Refactoring
Debe ser incremental:

```text
Existing behavior
 ↓
Characterization tests
 ↓
Small refactor
 ↓
Tests
 ↓
Review
 ↓
Commit
```

### Modernization
Puede incluir lenguaje, framework, dependencias, arquitectura, base de datos, infraestructura y APIs.

### Migration
Debe utilizar fases, validaciones y rollback cuando sea necesario.

> **Preservar comportamiento antes de mejorar implementación, salvo cambio explícito de requisitos.**

## 31. Refactoring Policy

No se refactoriza por estética. Antes de refactorizar se identifica problema, impacto, riesgo, beneficio, comportamiento a preservar, tests existentes, tests faltantes y alcance.

Se prefieren cambios pequeños, verificables y reversibles.

## 32. Security

Baseline de seguridad. No exponer secretos, introducir credenciales en código, realizar acciones productivas no autorizadas, ignorar vulnerabilidades conocidas ni saltarse controles. Los cambios críticos activan Human Gates.

## 33. Context Management

Orden recomendado:

```text
Project Policy
 ↓
Project State
 ↓
SPEC
 ↓
Relevant ADR
 ↓
Task
 ↓
Relevant Skill
 ↓
Relevant Code
```

## 34. Research / Radar

```text
Research
 ↓
Finding
 ↓
Evaluation
 ↓
Adopt / Test / Reject
 ↓
Decision
 ↓
Template Update
```

Las tecnologías nuevas no se incorporan automáticamente.

## 35. Glosario

Glosario vivo con definición, propósito, cuándo utilizarlo, ejemplo y qué NO significa.

Términos iniciales: Agent, Skill, Prompt, Instruction, Hook, Harness, Tool, Workflow, Eval, MCP, Agentic Engineering, Human Gate, ADR, SPEC, Playbook, Adapter, Contract, Refactoring, Technical Debt.

## 36. Manual paso a paso

### Aplicación nueva
1. Crear proyecto.
2. Configurar interacción.
3. Definir SPEC.
4. Analizar arquitectura.
5. Registrar decisiones.
6. Crear Demo.
7. Crear primera feature.
8. Crear tests.
9. Implementar.
10. Revisar.
11. Commit/PR.
12. CI.
13. Deploy.
14. E2E/Eval.
15. Verificar.
16. Repetir.

### Aplicación existente
1. Registrar proyecto.
2. Audit.
3. Baseline.
4. Identificar deuda.
5. Priorizar.
6. Crear plan.
7. Human Gate.
8. Refactorizar/migrar.
9. Testear.
10. Revisar.
11. Commit/PR.
12. CI.
13. Deploy.
14. Validar.
15. Repetir.

## 37. Métricas

Medir cuando sea posible: tiempo por tarea, iteraciones, fallos, correcciones, intervención humana, cobertura, requisitos verificados, Evals, tiempo de PR, tiempo de CI y costo de IA.

## 38. Madurez

- Level 1: SPEC + GitHub + Tests.
- Level 2: Agents + Skills.
- Level 3: Harness + Hooks + Evals.
- Level 4: Multi-agent + MCP.
- Level 5: Automatización avanzada.

No activar capacidades solo porque existan.

## 39. Criterios de aceptación del Template

Debe demostrar creación de proyecto nuevo, configuración conversacional, SPEC, arquitectura agnóstica, Demo, feature con agentes, tests, commit/PR, CI, Demo/Staging, E2E/Evals, corrección iterativa, preguntas ante decisiones críticas, PROJECT-STATE, ADRs, contingencias, auditoría de proyectos existentes, refactoring incremental, trazabilidad y evolución mediante Research/Radar.

## 40. Regla maestra

> **La IA debe maximizar el trabajo que puede realizar de forma segura y verificable, minimizando las preguntas innecesarias, pero nunca debe ocultar ambigüedades, riesgos o decisiones críticas.**

## 41. Validación

La especificación debe probarse con **Eventos Sociales**. La experiencia real determinará qué debe simplificarse, modificarse o agregarse.

**Versión:** 2.0  
**Estado:** Base para implementación y validación.
