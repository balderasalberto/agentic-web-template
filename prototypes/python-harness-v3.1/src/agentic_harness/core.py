from __future__ import annotations
import json, re, uuid
from datetime import datetime, timezone
from pathlib import Path

AGENTIC = ".agentic"
GATE_KEYWORDS = {
    "significant_architecture_change": ("architecture", "arquitectura", "microservice", "microservicio", "database engine", "framework"),
    "requirements_change": ("requirement", "requisito", "scope", "alcance"),
    "critical_data_change": ("drop table", "truncate", "delete all", "migracion destructiva", "destructive migration"),
    "security_change": ("auth", "oauth", "security", "seguridad", "permission", "permiso", "secret", "credential"),
    "production_change": ("production", "produccion", "deploy prod", "release prod"),
    "significant_cost_change": ("cost", "costo", "billing", "facturacion"),
    "public_contract_change": ("public api", "api publica", "breaking change", "contrato publico"),
    "permission_expansion": ("enable deploy", "grant permission", "ampliar permiso", "habilitar deploy"),
}

def now(): return datetime.now(timezone.utc).isoformat()
def load_json(p: Path, default):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else default

def save_json(p: Path, obj):
    p.parent.mkdir(parents=True, exist_ok=True); p.write_text(json.dumps(obj, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")

def parse_policy(path: Path):
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    def section(name):
        m=re.search(rf"(?ms)^\s*{re.escape(name)}:\s*\n((?:\s{{2,}}[^\n]+\n?)*)", text)
        out={}
        if m:
            for k,v in re.findall(r"^\s+([\w_]+):\s*(true|false|[^\n#]+)",m.group(1),re.M|re.I):
                out[k]= v.lower()=="true" if v.lower() in ("true","false") else v.strip()
        return out
    return {"permissions":section("permissions"),"human_gates":section("human_gates")}

def discover_policy(root: Path):
    return root/"PROJECT-POLICY.md" if (root/"PROJECT-POLICY.md").exists() else None

def classify_role(request: str):
    q=request.lower()
    if any(x in q for x in ("test", "prueba", "coverage", "cobertura")): return "tester"
    if any(x in q for x in ("review", "revis", "audit", "audita")): return "reviewer"
    if any(x in q for x in ("architecture", "arquitectura", "design system", "diseña la solucion")): return "architect"
    return "developer"

def detect_gates(request: str, policy: dict):
    q=request.lower(); found=[]
    for gate, words in GATE_KEYWORDS.items():
        if policy.get("human_gates",{}).get(gate) is True and any(w in q for w in words): found.append(gate)
    return found

def init_project(root: Path, description: str):
    d=root/AGENTIC
    if d.exists(): raise RuntimeError("Project is already initialized")
    (d/"tasks").mkdir(parents=True); (d/"evidence").mkdir(); (d/"gates").mkdir()
    save_json(d/"project.json", {"description":description,"created_at":now(),"phase":"intake"})
    save_json(d/"state.json", {"status":"ready","tasks":[],"pending_gates":[]})

def create_task(root: Path, request: str):
    d=root/AGENTIC
    if not d.exists(): raise RuntimeError("Run 'agentic init' first")
    pp=discover_policy(root)
    if not pp: raise RuntimeError("PROJECT-POLICY.md not found")
    policy=parse_policy(pp); gates=detect_gates(request,policy)
    tid="TASK-"+uuid.uuid4().hex[:8].upper(); role=classify_role(request)
    task={"id":tid,"request":request,"role":role,"status":"blocked" if gates else "planned","gates":gates,"created_at":now(),"evidence":[]}
    save_json(d/"tasks"/(tid+".json"),task)
    state=load_json(d/"state.json",{}); state.setdefault("tasks",[]).append(tid)
    if gates: state.setdefault("pending_gates",[]).append({"task":tid,"gates":gates})
    save_json(d/"state.json",state); return task

def approve(root: Path, tid: str):
    p=root/AGENTIC/"tasks"/(tid+".json"); task=load_json(p,None)
    if not task: raise RuntimeError("Task not found")
    task["gates_approved_at"]=now(); task["status"]="planned"; save_json(p,task)
    s=load_json(root/AGENTIC/"state.json",{}); s["pending_gates"]=[x for x in s.get("pending_gates",[]) if x.get("task")!=tid]; save_json(root/AGENTIC/"state.json",s)
    return task

def add_evidence(root: Path, tid: str, kind: str, result: str):
    p=root/AGENTIC/"tasks"/(tid+".json"); task=load_json(p,None)
    if not task: raise RuntimeError("Task not found")
    ev={"id":"EV-"+uuid.uuid4().hex[:8].upper(),"task":tid,"kind":kind,"result":result,"created_at":now()}
    save_json(root/AGENTIC/"evidence"/(ev["id"]+".json"),ev); task.setdefault("evidence",[]).append(ev["id"]); save_json(p,task); return ev

def mark_done(root: Path, tid: str):
    p=root/AGENTIC/"tasks"/(tid+".json"); task=load_json(p,None)
    if not task: raise RuntimeError("Task not found")
    if task.get("status")=="blocked": raise RuntimeError("Human Gate unresolved")
    if not task.get("evidence"): raise RuntimeError("Evidence required before Done")
    task["status"]="done"; task["completed_at"]=now(); save_json(p,task); return task
