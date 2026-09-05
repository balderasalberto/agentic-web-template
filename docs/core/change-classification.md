# Change Classification

Classify work before execution when classification affects gates, verification or knowledge impact.

Types: `FEATURE`, `BUGFIX`, `REFACTOR`, `UI_CHANGE`, `ARCHITECTURE_CHANGE`, `SECURITY_CHANGE`, `DATA_CHANGE`, `INFRASTRUCTURE_CHANGE`, `DOCUMENTATION`.

Routine UI/refactor/test/documentation work normally does not require an architecture gate. Significant architecture, security, destructive/critical data, production, cost, public contract and permission-expansion changes follow Policy gates.

Every change assesses: business behavior impact, architecture impact, security/data impact, verification required, and knowledge/docs impacted.
