"""Recompute the agreement figures of Supplementary Appendix B.7 and Section 1.1 from S6_agreement_codes.csv.

Each row of the CSV holds one field of one coded item: the first coder's and the second coder's codes before
discussion, both after discussion, and the first coder's code as S2 or S3 now holds it (first_final). The script
reports, for each round, percent agreement and Cohen's kappa on the fields the appendix reports, with a percentile
bootstrap interval over items (5,000 resamples) for the row, the column, and the incident level, seeded as the
rounds were (round 1: 20261027; round 2 and both rounds together: 20261029), and the agreement after discussion.
Python 3, standard library only.  Usage: python3 S6_agreement.py [S6_agreement_codes.csv]"""
import csv, os, random, sys
from collections import Counter, defaultdict

PATH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                           "S6_agreement_codes.csv")
ROWS, COLS = ["ES", "PM", "DM"], ["Rule-based", "ML", "LLM", "Agentic"]
LEVELS = ["ES", "PM", "DM", "no level", "outside"]


def kappa(pairs, cats):
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum(ca[c] * cb[c] for c in cats) / n / n
    return po, ((po - pe) / (1 - pe) if pe < 1 else float("nan"))


def boot(pairs, cats, seed, reps=5000):
    rnd = random.Random(seed)
    ks = []
    for _ in range(reps):
        s = [pairs[rnd.randrange(len(pairs))] for _ in pairs]
        k = kappa(s, cats)[1]
        if k == k:
            ks.append(k)
    ks.sort()
    return ks[int(0.025 * len(ks))], ks[int(0.975 * len(ks)) - 1]


def fmt(x):
    return "n/a" if x != x else f"{x:.2f}"


def line(name, pairs, cats, seed=None):
    cats = [c for c in cats if any(c in p for p in pairs)] or cats
    po, k = kappa(pairs, cats)
    s = f"{name}: {sum(a == b for a, b in pairs)} of {len(pairs)} ({po:.1%}), kappa {fmt(k)}"
    if seed is not None:
        lo, hi = boot(pairs, cats, seed)
        s += f" (95 % bootstrap interval {fmt(lo)}-{fmt(hi)})"
    return s


def agree(name, pairs):
    return f"{name}: {sum(a == b for a, b in pairs)} of {len(pairs)}"


items = defaultdict(dict)  # (round, id) -> field -> row
meta = {}
for r in csv.DictReader(open(PATH, encoding="utf-8", newline="")):
    items[(r["round"], r["id"])][r["field"]] = r
    meta[(r["round"], r["id"])] = (r["kind"], r["item"], r["group"])


def ids(rnd, kind):
    return sorted(k[1] for k in items if k[0] == rnd and meta[k][0] == kind)


def pairs(rnd, kind, field, a="first_before", b="second_before", only=None, norm=lambda v: v):
    out = []
    for i in ids(rnd, kind):
        f = items[(rnd, i)][field]
        if only is None or only(rnd, i):
            out.append((norm(f[a]), norm(f[b])))
    return out


def gloss(v):
    return "yes" if v.startswith("yes") else "no"


def both_llm(rnd, i, a="first_before", b="second_before"):
    c = items[(rnd, i)]["column"]
    return c[a] in ("LLM", "Agentic") and c[b] in ("LLM", "Agentic")


out = ["Round 1: 40 systems, 30 incidents (coded on the codebook of 28 October 2026)", ""]
S1 = 20261027
r1row = pairs("1", "system", "row")
r1col = pairs("1", "system", "column")
out.append(line("Row, before discussion", r1row, ROWS, S1))
out.append(line("Column, before discussion", r1col, COLS, S1))
out.append(line("Glossary decided the row, before discussion", pairs("1", "system", "glossary", norm=gloss), ["yes", "no"]))
fl = pairs("1", "system", "flag", only=both_llm)
out.append(agree(f"Flag, where both coders put the system in the LLM or agentic column", fl))
out.append(line("Incident level, before discussion", pairs("1", "incident", "level"), LEVELS, S1))
for p in "ABC":
    pp = pairs("1", "incident", "level", only=lambda rnd, i: meta[(rnd, i)][2] == f"panel {p}")
    out.append("  " + agree(f"panel {p}", pp))
out.append(line("Another reading, before discussion",
                pairs("1", "incident", "other_reading", norm=lambda v: "yes" if v.startswith("yes") else "no"),
                ["yes", "no"]))
out.append(agree("Row, after discussion", pairs("1", "system", "row", "first_after", "second_after")))
out.append(agree("Column, after discussion", pairs("1", "system", "column", "first_after", "second_after")))
out.append(agree("Incident level, after discussion", pairs("1", "incident", "level", "first_after", "second_after")))
out.append(agree("Row, the first coder's codes now", pairs("1", "system", "row", "first_final", "second_after")))
out.append(agree("Column, the first coder's codes now", pairs("1", "system", "column", "first_final", "second_after")))
out.append(agree("Incident level, the first coder's codes now",
                 pairs("1", "incident", "level", "first_final", "second_after")))

out += ["", "Round 2: 24 works (coded on the codebook as revised after the reviews)", ""]
S2 = 20261029
out.append(line("Scope and marking, before discussion", pairs("2", "work", "marking"),
                 ["counted", "offensive", "post-incident", "study", "benchmark", "adjacent", "non-DeFi", "not an entry"]))
placed = lambda rnd, i: items[(rnd, i)]["marking"]["second_before"] != "not an entry"
r2row = pairs("2", "work", "row", only=placed)
r2col = pairs("2", "work", "column", only=placed)
out.append(line("Row, before discussion", r2row, ROWS, S2))
out.append(line("Column, before discussion", r2col, COLS, S2))
out.append(agree("Glossary decided the row, before discussion", pairs("2", "work", "glossary", norm=gloss)))
fl2 = pairs("2", "work", "flag", only=both_llm)
out.append(line(f"Flag, where both coders put the work in the LLM or agentic column", fl2, ["yes", "no", "unverified"]))
for fld in ("marking", "row", "column", "flag"):
    out.append(agree(f"{fld.capitalize()}, after discussion", pairs("2", "work", fld, "first_after", "second_after")))

out += ["", "Both rounds, each coded independently, before discussion", ""]
out.append(line(f"Row ({len(r1row)} + {len(r2row)} works)", r1row + r2row, ROWS, S2))
out.append(line(f"Column ({len(r1col)} + {len(r2col)} works)", r1col + r2col, COLS, S2))
print("\n".join(out))
