# PROJECT-STATE.md

## Estado del template

```yaml
project: agentic-web-template
version: 2.0
phase: interactive-demo-discovery
status: in-progress
```

## Objetivo actual

Construir y validar un template GitHub agnóstico para desarrollo agentico de aplicaciones web nuevas y existentes.

## Completado

- Repositorio GitHub creado.
- SPEC v2.0 incorporada.
- AGENTS.md incorporado.
- PROJECT-POLICY.md incorporado.
- Contrato del Project Assistant incorporado.
- Skill del Project Assistant incorporada.
- Agent del Project Assistant incorporado.
- Research Agent incorporado.
- Flujo conversacional piloto iniciado con Eventos Sociales.

## Validación piloto — Eventos Sociales

```yaml
project_type: greenfield
objective: "Administración integral de eventos"
platforms:
  - mobile
  - tablet
  - desktop
users:
  - organizers
  - clients
  - providers
authorization:
  model: "roles and permissions"
  mvp_roles: "predefined"
  future: "custom roles and permissions"
mvp_direction: "integral basic management"
```

### Alcance funcional preliminar

```text
Evento
 + Cliente
 + Servicios
 + Proveedores
 + Agenda
 + Costos básicos
```

Este alcance es una dirección inicial y todavía debe convertirse en requisitos y criterios de aceptación detallados.

## Decisiones registradas durante la conversación

- Se eligió organización integral de eventos en lugar de únicamente contratación o directorio.
- Participarán organizadores, clientes y proveedores.
- El MVP utilizará roles predefinidos.
- La solución debe quedar preparada para roles personalizados posteriormente.
- Se recomienda comenzar con un MVP integral pequeño y una Demo temprana.

## Decisiones pendientes

- Requisitos funcionales concretos del MVP.
- Criterios de aceptación.
- Arquitectura.
- Tecnología, salvo que aparezcan restricciones.
- Estrategia de autenticación.
- Estrategia de Demo.
- Nivel de autonomía para la implementación.
- Ambientes y despliegue.

## Siguiente paso

Definir el primer conjunto mínimo de casos de uso del MVP y convertirlos en requisitos verificables.
