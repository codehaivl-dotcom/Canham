"""Run: python simulation/run_systems.py --seed 20261112."""
import argparse
import csv
import json
from pathlib import Path
try:
    from .systems import run_all
except ImportError:
    from systems import run_all


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed",type=int,default=20261112)
    parser.add_argument("--data",type=Path)
    parser.add_argument("--output",type=Path,default=Path(__file__).parent/"results")
    args=parser.parse_args();result=run_all(args.seed,args.data);args.output.mkdir(parents=True,exist_ok=True)
    (args.output/"systems.json").write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    with (args.output/"systems.csv").open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=["name","category","passed","actual"]);writer.writeheader()
        for row in result["scenarios"]:writer.writerow({**row,"actual":json.dumps(row["actual"],ensure_ascii=False)})
    lines=["# Noncombat systems simulation", "",f"Seed: {args.seed}",f"Summary: {result['summary']}",
           f"Data: {result['provenance']['mode']}","","| Scenario | Category | Result |","|---|---|---|"]
    lines += [f"| {r['name']} | {r['category']} | {'PASS' if r['passed'] else 'FAIL'} |" for r in result["scenarios"]]
    lines += ["","## Limits",""]+["- "+s for s in result["limitations"]]
    (args.output/"systems.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(json.dumps(result["summary"]))
    return 1 if result["summary"]["failed"] else 0


if __name__=="__main__":raise SystemExit(main())
