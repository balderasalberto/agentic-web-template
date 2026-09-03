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
- Primer flujo end-to-end del MVP seleccionado.

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
primary_flow: "crear evento -> asignar cliente -> agregar servicios -> asignar proveedores"
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

### Flujo principal MVP-001

```text
1. Crear evento
2. Asignar cliente
3. Agregar servicios requeridos
4. Asignar proveedor a cada servicio
5. Consultar el evento con sus servicios y proveedores
```

### Requisitos iniciales derivados

- RF-001: Un organizador puede crear un evento.
- RF-002: Un evento debe poder asociarse a un cliente.
- RF-003: Un evento debe permitir registrar uno o más servicios.
- RF-004: Cada servicio puede asociarse a un proveedor.
- RF-005: El sistema debe permitir consultar el resumen del evento, incluyendo cliente, servicios y proveedores asignados.
- RF-006: La información debe poder consultarse desde móvil, tablet y escritorio mediante una interfaz responsive.

### Criterios de aceptación iniciales

- CA-001: Al crear un evento válido, el sistema genera un identificador único y permite consultarlo.
- CA-002: Un evento puede asociarse a un cliente existente.
- CA-003: Un evento puede tener múltiples servicios.
- CA-004: Un servicio puede tener un proveedor asignado.
- CA-005: La consulta del evento muestra correctamente cliente, servicios y proveedores.
- CA-006: El flujo principal puede ejecutarse sin depender de una resolución manual del código o de datos internos.

Estos requisitos son una primera baseline y deberán refinarse antes de considerar el MVP listo para implementación.

## Decisiones registradas durante la conversación

- Se eligió organización integral de eventos en lugar de únicamente contratación o directorio.
- Participarán organizadores, clientes y proveedores.
- El MVP utilizará roles predefinidos.
- La solución debe quedar preparada para roles personalizados posteriormente.
- Se recomienda comenzar con un MVP integral pequeño y una Demo temprana.
- El primer flujo end-to-end será crear evento → asignar cliente → agregar servicios → asignar proveedores.

## Decisiones pendientes

- Requisitos funcionales concretos restantes del MVP.
- Criterios de aceptación detallados.
- Arquitectura.
- Tecnología, salvo que aparezcan restricciones.
- Estrategia de autenticación.
- Estrategia de Demo.
- Nivel de autonomía para la implementación.
- Ambientes y despliegue.

## Siguiente paso

Refinar los requisitos del flujo MVP-001 y después decidir la estrategia de autenticación, arquitectura y Demo con preguntas mínimas y recomendaciones del Project Assistant.
