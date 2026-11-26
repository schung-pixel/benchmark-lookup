import csv, json, sys, os
src = sys.argv[1]; out = sys.argv[2]
def load(n): return list(csv.DictReader(open(os.path.join(src, n), encoding="utf-8-sig")))
stats, srcs, mets = load("stats.csv"), load("sources.csv"), load("metrics.csv")
cols = ["stat_id","source_id","metric_id","stage","segment","stat_type","value","unit","as_published","n","population","period","indication","modality","location","nature","note"]
rows = [[r[c] for c in cols] for r in stats]
S = {s["source_id"]: {k: s[k] for k in ("authors","year","title","journal_or_publisher","doi","pmid")} for s in srcs}
M = {m["metric_id"]: {k: m[k] for k in ("family","name_ko","definition","unit","comparability_note")} for m in mets}
data = {"cols": cols, "rows": rows, "sources": S, "metrics": M, "built": "2026-11-27"}
open(out, "w", encoding="utf-8").write("window.DB=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n")
print(len(rows), "rows", os.path.getsize(out), "bytes")
