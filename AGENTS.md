# AGENTS.md — Agentic Web Template

## Propósito

Este archivo define las reglas operativas comunes para los agentes que trabajan sobre cualquier proyecto creado a partir de este template.

## Regla principal

Antes de modificar código, el agente debe conocer la tarea, consultar la SPEC y respetar PROJECT-POLICY y PROJECT-STATE cuando existan.

## Comportamiento esperado

1. Entender la intención del usuario.
2. Revisar el contexto mínimo necesario.
3. Determinar si puede ejecutar directamente o debe preguntar.
4. Proponer una opción cuando existan varias alternativas razonables.
5. Implementar cambios pequeños y verificables.
6. Ejecutar las validaciones aplicables.
7. Informar evidencia y estado.
8. Escalar al humano cuando exista un Human Gate o bloqueo relevante.

## No asumir

El agente no debe inventar:
- requisitos;
- credenciales;
- contratos;
- decisiones arquitectónicas críticas;
- datos de producción;
- permisos no otorgados.

Las suposiciones de bajo riesgo deben documentarse.

## Arquitectura

El agente debe respetar la arquitectura definida en el proyecto. Si detecta que la arquitectura existente impide cumplir un requisito, debe presentar alternativas antes de realizar un cambio arquitectónico significativo.

No imponer microservicios, patrones, frameworks o tecnologías sin justificación.

## Design Patterns

Aplicar el patrón más simple que resuelva correctamente el problema. No introducir patrones únicamente por cumplir una regla.

## Código existente

En proyectos brownfield, preservar el comportamiento existente salvo que el requisito indique lo contrario. Preferir refactorizaciones pequeñas, tests de caracterización y cambios reversibles.

## Testing

Todo cambio funcional debe incluir o actualizar las pruebas correspondientes. Un cambio no se considera terminado solo porque compile.

## GitHub

Los commits y Pull Requests deben seguir la PROJECT-POLICY. Si la política permite automatización, el agente puede realizar las acciones autorizadas. Las acciones productivas requieren el Human Gate definido por el proyecto.

## Fallos

Ante un fallo:

```text
Diagnose → Correct → Retest → Validate
```

Si el problema se repite o requiere una decisión no definida, detenerse y preguntar.

## Comunicación

La interacción debe ser clara, breve y orientada a decisiones. No preguntar por tareas rutinarias que estén dentro de la política autorizada.

Cuando deba preguntar, explicar:
- qué decisión falta;
- por qué importa;
- opción recomendada;
- alternativas principales.

## Definition of Done

Antes de declarar una tarea terminada, verificar requisitos, criterios de aceptación, tests, Evals relevantes, revisión, documentación y CI según aplique.
