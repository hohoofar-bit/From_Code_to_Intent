# Supplement S4 — The adaptive-acquisition record

Every entry in the LLM or the Agentic column of the matrix (Table 4 and Supplementary Table 7) carries the adaptive-acquisition flag (Section 4.4 and Supplementary Appendix B.2). There are 57 such entries: 38 LLM and 19 agentic. The flag records whether the model decides for itself what evidence to acquire. Its values:
- **yes:** the model selects a tool, sets the schedule, and the requested result re-enters the model;
- **no:** tools, if any, run where the framework places them;
- **unverified:** neither the method text nor released code could be read.

**File.** `S4_adaptive_acquisition.csv` has one row per entry. Each row gives:
- the work's short name and identifier, and its year;
- its level, its column (the type it presents), its secondary type and its marking;
- the flag, and what was read: the full text, or the abstract where the full text could not be obtained;
- the evidence that decided the flag, strongest first (Supplementary Appendix B.2): released code, a trace or log, an ablation of the acquisition step, or the method text only;
- for released code, the release or commit read, the one nearest the paper (Supplementary Appendix B.2);
- the five fields that decide the flag:
  - the tool set;
  - who selects the tool;
  - who sets the schedule;
  - whether a requested result re-enters the model;
  - whether the model stage is terminal;
- the basis, which is the column justification from the placement sheet.

**Reading the tool set.**
- "Before the model" and "after the model" name a tool that the framework runs at a fixed point of the pipeline.
- "— (no tool)" means the model works from its prompt alone.

**Counts.**

| Column | yes | no | unverified |
|---|---|---|---|
| LLM | 1 | 37 | 0 |
| Agentic | 8 | 11 | 0 |

**Evidence basis.**

| Flag | released code | trace or log | ablation | method text only |
|---|---|---|---|---|
| yes | 3 | 5 | 0 | 1 |
| no | 11 | 0 | 0 | 37 |

**The agentic column.**
- Of its 13 counted systems, 11 carry "no" and two, RugKeeper and FOMOCheck, "yes". Of the "no"s, three rest on released code (LLM-SmartAudit, ACTaint, VeriRAG-Agent) and the others on the method text. RugKeeper's flag rests on its method text alone (evidence basis "method text only", marked ⊙ in Table 4): its agents write sub-questions when they find information missing, and a planner assigns them to on-chain information-acquisition agents (its Algorithm 1), but the paper names no tool and reports no trace. FOMOCheck's rests on its released code (marked ⊕ in Table 4), for the mode in which a free-text query reaches an agent that can call the Solana Agent Kit's tools; its evaluation, a backtest on 30 tokens, runs a fixed pipeline in which the model reads a report that fixed code builds, so its five fields record both.
- The other six agentic entries with "yes" are shown and not counted: offensive, post-incident, or benchmark works.
- The one LLM entry with "yes" is also shown and not counted: a penetration-testing system outside DeFi, marked offensive.
