# Template Policy Defaults

Defaults seguros para proyectos derivados. Un proyecto puede sobrescribirlos explícitamente en su propia Policy.

```yaml
interaction_mode: collaborator
explanation_level: brief
autonomy_level: L1

permissions:
  source_changes: true
  tests: true
  documentation: true
  local_commands: true
  commit: false
  pull_request: false
  demo_deploy: false
  staging_deploy: false
  production_deploy: false

human_gates:
  significant_architecture_change: true
  requirements_change: true
  critical_data_change: true
  security_change: true
  production_change: true
  significant_cost_change: true
  public_contract_change: true
  permission_expansion: true
```

## Semántica

- Una acción no declarada como permitida se considera no autorizada.
- La autonomía nunca amplía permisos.
- Un Human Gate prevalece sobre cualquier permiso o nivel de autonomía.
- Cambios de Policy deben ser explícitos, trazables y no retroactivos.
- Producción permanece bloqueada por defecto.

## Gate classification guidance (v3.3)

- Significant architecture replacement/commitment -> `significant_architecture_change`.
- Authentication/authorization/trust-boundary changes -> `security_change` when material.
- Destructive or critical data-model/migration changes -> `critical_data_change`.
- Production actions -> `production_change`.
- Significant recurring/new cost -> `significant_cost_change`.
- Breaking public API/contract -> `public_contract_change`.
- Expanding agent permissions -> `permission_expansion`.
- Routine UI, documentation, tests, bug fixes and internal refactors do **not** require an architecture gate unless their actual impact crosses a gate above.
