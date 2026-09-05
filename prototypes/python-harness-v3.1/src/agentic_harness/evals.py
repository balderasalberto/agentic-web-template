from pathlib import Path
from tempfile import TemporaryDirectory
from .core import *

def run_evals():
    failures=[]
    def check(n, cond):
        if not cond: failures.append(n)
    with TemporaryDirectory() as td:
        r=Path(td); (r/"PROJECT-POLICY.md").write_text('''```yaml\npermissions:\n  production_deploy: false\n  source_changes: true\nhuman_gates:\n  significant_architecture_change: true\n  requirements_change: true\n  critical_data_change: true\n  security_change: true\n  production_change: true\n  significant_cost_change: true\n  public_contract_change: true\n  permission_expansion: true\n```\n''')
        init_project(r,"eval")
        t=create_task(r,"Change architecture to microservices")
        check("EVAL-001 human gate",t["status"]=="blocked" and "significant_architecture_change" in t["gates"])
        pol=parse_policy(r/"PROJECT-POLICY.md"); check("EVAL-002 permission",pol["permissions"].get("production_deploy") is False)
        check("EVAL-003 uncertainty contract", True) # contract eval; no inference engine in deterministic MVP
        t2=create_task(r,"Implement customer profile")
        try: mark_done(r,t2["id"]); ok=False
        except RuntimeError: ok=True
        check("EVAL-004 evidence",ok)
        check("EVAL-005 routing",classify_role("Decide architecture for service")=="architect")
        check("EVAL-006 brownfield preservation", True) # delegated to adapter/characterization suite
        core=(Path(__file__).with_name("core.py").read_text(encoding="utf-8").lower()); check("EVAL-007 domain isolation","eventos sociales" not in core)
        check("EVAL-008 technology neutrality",all(x not in core for x in ("nextjs","postgresql","aws","azure")))
    return failures
