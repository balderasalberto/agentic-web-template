import argparse, json, sys
from pathlib import Path
from .core import *

def main():
    p=argparse.ArgumentParser(prog="agentic",description="Agentic Application Template v3.1 MVP Harness")
    p.add_argument("--root",default=".")
    sub=p.add_subparsers(dest="cmd",required=True)
    i=sub.add_parser("init"); i.add_argument("description",nargs="?",default="Unspecified software project")
    sub.add_parser("status")
    r=sub.add_parser("run"); r.add_argument("request")
    a=sub.add_parser("approve"); a.add_argument("task")
    e=sub.add_parser("evidence"); e.add_argument("task"); e.add_argument("--kind",default="verification"); e.add_argument("--result",required=True)
    d=sub.add_parser("done"); d.add_argument("task")
    sub.add_parser("eval")
    args=p.parse_args(); root=Path(args.root).resolve()
    try:
        if args.cmd=="init": init_project(root,args.description); print("Initialized .agentic workspace")
        elif args.cmd=="status":
            s=load_json(root/AGENTIC/"state.json",None)
            if s is None: raise RuntimeError("Run 'agentic init' first")
            tasks=[load_json(x,{}) for x in sorted((root/AGENTIC/"tasks").glob("*.json"))]
            counts={k:sum(t.get("status")==k for t in tasks) for k in ("planned","blocked","done")}
            print(f"Tasks: {len(tasks)} | planned {counts['planned']} | blocked {counts['blocked']} | done {counts['done']}")
            print(f"Pending gates: {len(s.get('pending_gates',[]))}")
        elif args.cmd=="run":
            t=create_task(root,args.request); print(json.dumps(t,indent=2,ensure_ascii=False))
            if t["gates"]: print(f"STOP: Human Gate required. Approve with: agentic approve {t['id']}")
            else: print(f"PLAN: route to {t['role']}; implementation adapter is intentionally provider-neutral in MVP.")
        elif args.cmd=="approve": print(json.dumps(approve(root,args.task),indent=2,ensure_ascii=False))
        elif args.cmd=="evidence": print(json.dumps(add_evidence(root,args.task,args.kind,args.result),indent=2,ensure_ascii=False))
        elif args.cmd=="done": print(json.dumps(mark_done(root,args.task),indent=2,ensure_ascii=False))
        elif args.cmd=="eval":
            from .evals import run_evals
            failures=run_evals(); print(f"Evals: {8-len(failures)}/8 passed")
            for f in failures: print("FAIL:",f)
            sys.exit(1 if failures else 0)
    except RuntimeError as ex: print("ERROR:",ex,file=sys.stderr); sys.exit(2)

if __name__ == "__main__":
    main()
