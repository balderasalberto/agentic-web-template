# Critical Flows

Document only flows whose sequence, branching, state or integration behavior materially improves understanding. Replace this example with the real flow.

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant Service
    User->>UI: Action
    UI->>Service: Request
    Service-->>UI: Result
    UI-->>User: Feedback
```
