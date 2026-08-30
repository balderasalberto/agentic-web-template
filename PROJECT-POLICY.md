# PROJECT-POLICY.md

## Propósito

Política configurable que determina cómo los agentes pueden interactuar, ejecutar cambios y solicitar autorización en un proyecto derivado del Agentic Web Template.

## Principio

La autonomía debe maximizar el trabajo seguro y verificable sin eliminar los puntos de decisión humana.

## Configuración inicial

```yaml
interaction_mode: collaborator
explanation_level: brief
autonomy_level: L2

permissions:
  code_changes: true
  tests: true
  documentation: true
  commit: true
  pull_request: true
  demo_deploy: false
  staging_deploy: false
  production_deploy: false

human_gates:
  architecture: true
  requirements_change: true
  critical_data_change: true
  security_change: true
  production: true
  significant_cost_change: true
  public_contract_change: true
```

## Modos de interacción

- `tutor`: explica y pregunta con frecuencia.
- `collaborator`: ejecuta tareas rutinarias y consulta decisiones importantes.
- `supervisor`: ejecuta la mayoría de tareas y consulta excepciones.
- `autonomous`: ejecuta ciclos completos dentro de los límites definidos.
- `custom`: política específica.

## Niveles de autonomía

- `L0`: solo propone.
- `L1`: implementa; Git importante es manual.
- `L2`: puede crear commits y PRs.
- `L3`: puede ejecutar CI y desplegar Demo/Staging.
- `L4`: puede corregir iterativamente hasta satisfacer validaciones.
- `L5`: automatización avanzada, siempre limitada por política y Human Gates.

## Regla de preguntas

Preguntar cuando:
- exista ambigüedad relevante;
- haya una decisión arquitectónica significativa;
- cambien requisitos;
- exista riesgo de seguridad;
- una acción esté fuera de permisos;
- se requiera un Human Gate;
- no exista información crítica.

No preguntar por acciones rutinarias ya autorizadas.

## Producción

Por defecto, producción requiere aprobación humana explícita.

## Cambios de política

Una modificación de esta política debe ser explícita y quedar registrada en el historial del proyecto.
