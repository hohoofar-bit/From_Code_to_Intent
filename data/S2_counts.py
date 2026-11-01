"""Recompute, from the placement sheet (S2_placement_sheet.csv), the counts the article and its appendices print:
the counted systems by level and column (Table 4 and Fig. 1), the marks, Table 9 (the description-mismatch level
under five definitions), Table 10 (counted systems by year of first public release), the adaptive-acquisition
flags of the LLM and agentic columns, the deployment points, and the alternative readings of Supplementary
Appendix B.5 that the sheet's fields decide.

Python 3, standard library only.  Usage:  python3 S2_counts.py [S2_placement_sheet.csv]

Fields used: row, row_flag, secondary_rows, column (1 rule-based, 2 ML, 3 LLM, 4 agentic), secondary_type,
marking (empty = counted), venue_type (short = short or companion paper), access, reads_description,
description_scope, adaptive_acquisition, evidence_basis, deployment_point, first_release, and the texts
row_justification, column_justification and type_evidence, which name the glossary line and the step of B.2 that
decided.
B.5's reading of front-end, documentation and whitepaper texts as complete rests on how each case is tied to a
text, which the row justifications state but no field records, so it is not recomputed here."""
import csv, os, re, statistics, sys
from collections import Counter

path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                          "S2_placement_sheet.csv")
rows = list(csv.DictReader(open(path, encoding="utf-8")))
counted = [r for r in rows if r["marking"] == ""]
LEVELS = ["ES", "PM", "DM"]
TYPES = {"1": "Rule-based", "2": "ML", "3": "LLM", "4": "Agentic"}
ORDER = {"Rule-based": 1, "ML": 2, "LLM": 3, "Agentic": 4}

def grid(entries, col=lambda r: TYPES[r["column"]], row=lambda r: r["row"]):
    c = Counter((row(r), col(r)) for r in entries)
    return {lvl: [c[(lvl, t)] for t in TYPES.values()] for lvl in LEVELS}

def show(title, g):
    print(title)
    print("  %-4s %s   total" % ("", "  ".join("%10s" % t for t in TYPES.values())))
    for lvl in LEVELS:
        print("  %-4s %s   %5d" % (lvl, "  ".join("%10d" % x for x in g[lvl]), sum(g[lvl])))
    print("  %-4s %s   %5d" % ("all", "  ".join("%10d" % sum(g[l][i] for l in LEVELS) for i in range(4)),
                                sum(sum(v) for v in g.values())))
    print()

print(f"{len(rows)} entries in the sheet, {len(counted)} counted; shown and not counted by marking: "
      + ", ".join(f"{k} {v}" for k, v in sorted(Counter(r['marking'] for r in rows if r['marking']).items())))
print()
show("Counted systems by level and column (Table 4, Fig. 1):", grid(counted))
print("Marks among the counted: ‡ (row by stated target or by rule)", sum(r["row_flag"] == "‡" for r in counted),
      "| ◊ short or companion papers", sum(r["venue_type"] == "short" for r in counted),
      "| placed on the abstract alone", sum(r["access"] == "abstract" for r in counted))
print()

# ---- Table 9: the description-mismatch level under five definitions (counted systems, by column)
def dm_by(pred):
    c = Counter(TYPES[r["column"]] for r in counted if pred(r))
    v = [c[t] for t in TYPES.values()]
    return "  ".join("%3d" % x for x in v) + "   = %d" % sum(v)
sec = lambda r: [s.strip() for s in r["secondary_rows"].split(",") if s.strip()]
print("Table 9 (rule-based, ML, LLM, agentic = total):")
print("  a property a named description states (printed rule)   ", dm_by(lambda r: r["row"] == "DM"))
print("  the detector reads a named description                  ", dm_by(lambda r: r["reads_description"] == "yes"))
print("  a project-specific description only                     ",
      dm_by(lambda r: r["row"] == "DM" and r["description_scope"] == "project-specific"))
print("  DM as row or secondary row                              ", dm_by(lambda r: r["row"] == "DM" or "DM" in sec(r)))
print("  printed rule, entries read in full only                 ",
      dm_by(lambda r: r["row"] == "DM" and r["access"] == "full"))
print()

# ---- Table 10: counted systems by cell and year of first public release
def first_year(r):
    m = re.match(r"\s*cited version,\s*(\d{4})", r["first_release"]) or re.search(r"\((\d{4})-\d{2}\)", r["first_release"])
    return int(m.group(1))
print("Table 10 (cell: n, first, median, 2016-20, 2021-23, 2024, 2025-26):")
for lvl in LEVELS:
    for t in TYPES.values():
        ys = [first_year(r) for r in counted if r["row"] == lvl and TYPES[r["column"]] == t]
        if not ys:
            print(f"  {lvl} x {t}: 0"); continue
        bins = [sum(a <= y <= b for y in ys) for a, b in ((2016, 2020), (2021, 2023), (2024, 2024), (2025, 2026))]
        med = statistics.median(ys)
        print(f"  {lvl} x {t}: {len(ys)}, {min(ys)}, {med:g}, " + ", ".join(map(str, bins)))
print()

# ---- the adaptive-acquisition flag (counted LLM and agentic entries)
la = [r for r in counted if r["column"] in ("3", "4")]
print("Flag, counted LLM and agentic entries:", dict(Counter(r["adaptive_acquisition"] for r in la)),
      "| resting on the method text alone:", sum(r["evidence_basis"] == "method text only" for r in la), "of", len(la))
print()

# ---- deployment point (Supplementary Appendix B, the field list): counted systems by level, and the counted
# systems that read a project's own description
POINTS = ["static", "pre-execution", "runtime", "post-hoc"]
print("Deployment point of the counted systems (" + ", ".join(POINTS) + "):")
for lvl in LEVELS:
    c = Counter(r["deployment_point"] for r in counted if r["row"] == lvl)
    print(f"  {lvl}: " + ", ".join(str(c[p]) for p in POINTS) + f"   = {sum(c[p] for p in POINTS)}")
c = Counter(r["deployment_point"] for r in counted)
print("  all: " + ", ".join(str(c[p]) for p in POINTS) + f"   = {sum(c[p] for p in POINTS)}")
own = [r for r in counted if r["reads_description"] == "yes" and r["description_scope"] == "project-specific"]
print(f"Counted systems that read a project's own description ({len(own)}), by deployment point:",
      dict(Counter(r["deployment_point"] for r in own)))
print()

# ---- Supplementary Appendix B.5: alternative readings decided by the sheet's fields and texts
def gl(r):
    return set(re.findall(r"glossary(?: \(| )?line (\d)", r["row_justification"]))
line3 = [r for r in counted if r["row_flag"] == "‡" and "3" in gl(r) and "attacker-contract rule" not in r["row_justification"]]
line2 = [r for r in counted if r["row_flag"] == "‡" and "2" in gl(r)]
show(f"Glossary line 3 read as ES ({len(line3)} entries move: {', '.join(r['short_name'] for r in line3)}):",
     grid(counted, row=lambda r: "ES" if r in line3 else r["row"]))
show(f"Glossary line 2 read as PM ({len(line2)} entries move: {', '.join(r['short_name'] for r in line2)}):",
     grid(counted, row=lambda r: "PM" if r in line2 else r["row"]))
def decided_by_tie_break(r):
    t = r["type_evidence"] + " " + r["column_justification"]
    if not re.search(r"tie-break|step 5", t) or "not reached" in t:
        return False
    return not re.search(r"\(B\.2 step 4\); read as combined", t)   # decided at step 4, the tie-break only agrees
def older(r):
    types = [TYPES[r["column"]]] + [s.strip() for s in r["secondary_type"].split(",") if s.strip()]
    return min(types, key=ORDER.get)
tb = [r for r in counted if decided_by_tie_break(r) and older(r) != TYPES[r["column"]]]
show(f"The older type deciding the tie-break of B.2 step 5 ({len(tb)} entries change column):",
     grid(counted, col=lambda r: older(r) if r in tb else TYPES[r["column"]]))
show("Without short or companion papers:", grid([r for r in counted if r["venue_type"] != "short"]))
