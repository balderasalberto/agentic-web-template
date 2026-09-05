# TEMPLATE-STATE

```yaml
project: agentic-application-template
spec_version: 3.0
phase: universal-core-bootstrap
status: in-progress
```

## Objetivo actual

Convertir el repositorio en un Core agentico universal, sin dependencias de dominio, tipo de aplicación, stack o proveedor.

## Completado

- SPEC universal v3.0.
- Jerarquía autoritativa de instrucciones.
- Policy defaults segura.
- Contratos mínimos de Project Assistant, Architect, Developer, Tester y Reviewer.
- Contrato inicial del Harness.
- Schemas de Task y Evidence.
- Evals conductuales iniciales.
- Caso Eventos Sociales movido a `examples/`.

## Pendiente

- Implementación ejecutable del Harness.
- Hooks deterministas.
- Runner de Evals.
- Integración Git/CI independiente de proveedor.
- Segundo y tercer proyecto de aceptación de dominios distintos.
- Adapters/Tools concretos aislados del Core.

## Siguiente paso

Implementar un Minimum Viable Harness que pueda leer Task + Policy, detectar Human Gates, enrutar un rol y exigir Evidence antes de marcar Done.
