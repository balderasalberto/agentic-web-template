# AGENTIC APPLICATION TEMPLATE — SPECIFICATION v3.3.0

**Estado:** Base universal para implementación y validación  
**Propósito:** sistema operativo agentico, agnóstico de dominio y tecnología, para construir, evolucionar, refactorizar y modernizar software.

## 1. Misión

Transformar una intención humana o un sistema existente en trabajo de ingeniería seguro, trazable, verificable y progresivamente automatizable, manteniendo control humano sobre decisiones críticas.

El Core no contiene requisitos de negocio ni selecciona tecnologías por defecto. Define el proceso mediante el cual esas decisiones se descubren, evalúan, registran y validan.

## 2. Alcance universal

Tipos de producto soportados conceptualmente incluyen web, API, mobile, desktop, CLI, service, library, data pipeline, AI system, integration y soluciones híbridas. La lista no es cerrada.

### Greenfield
`INTENT → DISCOVERY → SPEC → ARCHITECTURE → PLAN → IMPLEMENT → VERIFY → REVIEW → EVIDENCE → RELEASE`

### Brownfield
`DISCOVERY → AUDIT → BASELINE → CHARACTERIZATION → PLAN → INCREMENTAL CHANGE → VERIFY → REVIEW → EVIDENCE`

## 3. Principios invariantes

1. El Core no conoce el dominio del proyecto.
2. La arquitectura deriva de requisitos y restricciones.
3. La tecnología es intercambiable salvo restricción explícita.
4. Usar la solución más simple que satisfaga el problema.
5. No inventar requisitos, permisos, restricciones ni hechos.
6. Mantener contexto mínimo suficiente.
7. Automatizar reglas críticas cuando sea posible.
8. Toda decisión significativa es trazable.
9. Toda tarea terminada requiere evidencia verificable.
10. Tests validan software; Evals validan comportamiento agentico.
11. Human Gates no pueden ser anulados por autonomía.
12. Brownfield preserva comportamiento salvo cambio explícito.
13. Los cambios deben ser reversibles cuando sea razonable.
14. El sistema debe poder detenerse y escalar a un humano.
15. Nuevas capacidades deben extender el Core sin contaminarlo con dominio o proveedor.

## 4. Capas

### Core
Contratos universales: SPEC, Agents, Skills, Harness, Policy model, Hooks, Evals, schemas y playbooks.

### Project
Artefactos generados/configurados para una aplicación: PROJECT-SPEC, PROJECT-POLICY, PROJECT-STATE, requirements, ADRs, tasks y evidence.

### Examples
Proyectos de aceptación que demuestran generalidad. No pueden ser requeridos por el Core.

## 5. Responsabilidades

- **Instruction:** regla persistente.
- **Agent:** rol con responsabilidad, límites, inputs y outputs.
- **Skill:** procedimiento/conocimiento especializado cargado bajo demanda.
- **Tool:** capacidad para observar o modificar sistemas externos.
- **Hook:** control determinista en un punto del workflow.
- **Harness:** orquesta contexto, routing, permisos, gates, checkpoints, recuperación y evidencia.
- **Eval:** verifica comportamiento del sistema agentico.
- **Playbook:** procedimiento operativo para escenarios conocidos.
- **Policy:** autoridad y límites configurados para un proyecto.
- **State:** estado mutable y resumido del proyecto.

## 6. Jerarquía autoritativa

```text
SPEC.md                         modelo universal
AGENTS.md                       reglas universales de agentes
PROJECT-POLICY.md               defaults del template
agents/<role>.md                contrato de cada rol
skills/<skill>/SKILL.md         procedimiento especializado
Project artifacts               verdad específica de la aplicación
PROJECT-STATE.md                estado del desarrollo del template
```

Una capa inferior no debe duplicar reglas de una capa superior; debe referenciarlas y especializarlas.

## 7. Agentic Core mínimo

- Project Assistant: intake, coordinación y progreso.
- Architect: decisiones técnicas y ADRs.
- Developer: implementación mínima y trazable.
- Tester: estrategia y ejecución de verificación.
- Reviewer: revisión independiente de calidad/riesgo.
- Research Agent: evaluación de capacidades externas.

Roles adicionales son extensiones, no requisitos del Core.

## 8. Harness contract

Todo trabajo ejecutable sigue, salvo excepción documentada:

```text
REQUEST
→ LOAD MINIMUM CONTEXT
→ CLASSIFY
→ CHECK POLICY
→ ROUTE AGENT/SKILLS
→ PLAN
→ HUMAN GATE (if required)
→ EXECUTE
→ VERIFY
→ REVIEW (when required)
→ COLLECT EVIDENCE
→ UPDATE STATE
```

Un fallo sigue `DIAGNOSE → FIX → RETEST`; fallos repetidos o autoridad insuficiente escalan al humano.

## 9. Project intake

El Project Assistant descubre progresivamente sólo lo necesario: objetivo, consumidores, alcance inicial, restricciones, contexto existente, riesgos, ambientes y autonomía. No debe preguntar por una tecnología si todavía no afecta una decisión segura.

## 10. Arquitectura y tecnología

El Core nunca contiene defaults como framework, base de datos, cloud o patrón arquitectónico. El Architect evalúa requisitos, restricciones, operación, seguridad, coste, mantenibilidad y capacidades del equipo. Una decisión significativa genera ADR y Human Gate cuando la Policy lo requiera.

## 11. Policy y Human Gates

Autonomía e interacción son dimensiones independientes. La Policy controla permisos, ambientes y gates. Producción, seguridad, cambios críticos de datos, contratos públicos, arquitectura significativa y costes relevantes requieren gate por defecto.

## 12. Trazabilidad

```text
Requirement
→ Acceptance Criterion
→ Task
→ Implementation
→ Test/Eval
→ Evidence
```

Los identificadores deben conservarse durante el ciclo para poder demostrar qué requisito satisface cada cambio.

## 13. Definition of Ready

Una tarea puede ejecutarse cuando tiene objetivo, alcance suficiente, criterios verificables, restricciones críticas conocidas, permisos y riesgos tratados. Lo desconocido no crítico puede registrarse como supuesto reversible.

## 14. Definition of Done

No basta con generar código. Debe existir evidencia proporcional: criterios satisfechos, tests/evals relevantes, revisión cuando aplique, documentación actualizada y estado consistente.

## 15. Extensibilidad

Preferir Skills, Tools, Adapters, Hooks, Policies y Playbooks para nuevas tecnologías o dominios. Una modificación del Core para soportar un tipo nuevo de aplicación requiere justificar por qué la abstracción existente es insuficiente.

## 16. Evals mínimos del template

El Core debe probar al menos: respeto de Human Gates, rechazo de acciones sin permiso, preservación de incertidumbre, no invención de requisitos, routing apropiado, evidencia antes de Done y ausencia de dependencias de dominio en el Core.

## 17. Criterio de aceptación de universalidad

El mismo Core debe poder gobernar, sin cambios de código/contenido específico de dominio, proyectos significativamente diferentes. Los ejemplos son pruebas de aceptación del template.


# v3.3 Protocol Addendum

The Core MUST preserve Project Knowledge as an operational artifact. Intake distinguishes requirements, constraints, preferences, assumptions and unknowns. Architecture decisions are driven by project context and material replacements require renewed gates. Work uses explicit lifecycle states: proposed, planned, implementing, implemented, verified, done. Mermaid diagrams are first-class knowledge where they improve comprehension. `Done` requires sufficient Evidence and knowledge-impact assessment. See `docs/core/` and `docs/knowledge/`.
