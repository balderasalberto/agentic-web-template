# Research Radar

## Cómo usarlo

Cada hallazgo relevante debe registrarse con este formato:

### [YYYY-MM-DD] Título del hallazgo

- **Fuente:**
- **Qué cambió:**
- **Área:**
- **Relevancia:** Baja / Media / Alta
- **Impacto esperado:**
- **¿Mejora el template?:** Sí / No / Por comprobar
- **Componente afectado:**
- **Acción propuesta:** Adopt / Experiment / Reject / Defer
- **Human Gate requerido:** Sí / No
- **Estado:** Nuevo / Evaluando / Decidido / Implementado / Archivado

## Criterios de evaluación

Evaluar cada hallazgo por:

1. Beneficio real.
2. Madurez.
3. Compatibilidad con agnosticismo.
4. Seguridad.
5. Complejidad introducida.
6. Mantenibilidad.
7. Reversibilidad.
8. Impacto en la experiencia interactiva.
9. Evidencia disponible.
10. Costo operativo.

## Regla de decisión

```text
Nueva tecnología/práctica
        ↓
¿Relevante?
 ├─ No → Registrar y archivar
 └─ Sí
     ↓
¿Existe evidencia suficiente?
 ├─ No → Experimentar / Defer
 └─ Sí
     ↓
¿Mejora el template?
 ├─ No → Reject
 └─ Sí
     ↓
¿Cambio significativo?
 ├─ Sí → Human Gate
 └─ No → Proponer implementación
     ↓
Test / Eval
     ↓
Adoptar
```
