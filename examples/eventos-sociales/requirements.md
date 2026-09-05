# Requisitos iniciales — Eventos Sociales

## Estado

Baseline inicial del MVP. Estos requisitos deben refinarse antes de implementación productiva.

## MVP-001 — Gestión básica de un evento

### Objetivo

Permitir que un organizador gestione el núcleo de un evento desde su creación hasta la asignación de servicios y proveedores.

### Flujo principal

1. Crear evento.
2. Asignar cliente.
3. Agregar servicios requeridos.
4. Asignar proveedor a cada servicio.
5. Consultar el resumen del evento.

## Requisitos funcionales

- **RF-001**: Un organizador puede crear un evento.
- **RF-002**: Un evento puede asociarse a un cliente existente.
- **RF-003**: Un evento puede contener uno o más servicios.
- **RF-004**: Cada servicio puede asociarse a un proveedor.
- **RF-005**: El sistema permite consultar el resumen del evento con cliente, servicios y proveedores.
- **RF-006**: La interfaz es responsive y usable en móvil, tablet y escritorio.

## Criterios de aceptación

- **CA-001**: Al crear un evento válido, se genera un identificador único y el evento puede consultarse.
- **CA-002**: Un evento puede asociarse a un cliente existente.
- **CA-003**: Un evento puede tener múltiples servicios.
- **CA-004**: Un servicio puede tener un proveedor asignado.
- **CA-005**: La consulta del evento muestra correctamente cliente, servicios y proveedores.
- **CA-006**: El flujo puede ejecutarse mediante la interfaz sin requerir manipulación manual de datos internos.

## Reglas iniciales

- Los roles del MVP son predefinidos.
- La autorización se modelará mediante roles y permisos.
- El diseño debe permitir posteriormente roles y permisos personalizados.
- La autenticación no debe quedar acoplada al dominio funcional.

## Pendientes

- Datos obligatorios y validaciones de Evento, Cliente, Servicio y Proveedor.
- Estados del evento y del servicio.
- Costos básicos y reglas de cálculo.
- Agenda y conflictos de fechas/horarios.
- Permisos exactos por rol.
- Autenticación definitiva para el MVP productivo.
- Arquitectura y tecnología.
- Estrategia de Demo.

## Decisión de autenticación recomendada

### Estrategia por fases

Para la **Demo inicial**, no incorporar autenticación real si esta retrasa la validación del flujo funcional. La Demo puede ejecutarse con un usuario/rol simulado y datos controlados.

Para el **MVP productivo**, incorporar autenticación real mediante un proveedor de identidad estándar y mantenerla desacoplada de la lógica de negocio.

### Recomendación

No elegir todavía entre Google, correo/contraseña u otro proveedor como decisión arquitectónica irreversible. Primero validar el flujo MVP-001. Cuando se requiera seguridad real, seleccionar el proveedor considerando:

- experiencia de usuario para los tres tipos de usuario;
- soporte para roles y permisos;
- seguridad y recuperación de cuenta;
- facilidad de integración;
- costo y límites;
- posibilidad de cambiar de proveedor mediante un adaptador.

**Decisión provisional:** Demo sin autenticación real; arquitectura preparada para autenticación posterior.

## Próximo paso

Definir los datos mínimos de un Evento y Cliente y sus validaciones. Después, el Project Assistant propondrá la arquitectura más sencilla que permita ejecutar la Demo sin instalación local.
