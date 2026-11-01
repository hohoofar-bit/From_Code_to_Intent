# From Code to Intent: A Survey of Attack and Anomaly Detection in Decentralized Finance — Data Files

The article and its supplementary appendices are in preparation for publication and will be posted here after acceptance. This repository holds the electronic supplement (S1–S6).

## Abstract

Decentralized-finance (DeFi) protocols lose funds to attacks that exploit no software defect: the attacker turns a protocol's own economic logic against it, or a governance action does something other than what its description says. This survey organizes DeFi attack and anomaly detection with a two-axis taxonomy. Rows give what an attack violates: the execution-semantics, protocol-mechanism, or description-mismatch level. Columns give the type of detector a work presents (rule-based, machine-learning, large-language-model, or agentic). Stated rules and a codebook place 190 works and count 150 of them, the peer-reviewed detection and defense systems. Only two counted detectors, both short papers, are recorded as choosing their own evidence, one on its method text alone and the other in a mode its evaluation does not run. No counted system scores behavior observed on chain against a project's own statement. The survey calls this the intent gap, states the unmet requirement as a property of the anomaly score, and argues that a benchmark with intent-consistent negative controls is the binding constraint.

## Contents

All files are in [`data/`](data/). [`data/README.md`](data/README.md) gives the full description of each part.

| Part | Files | What it holds |
|---|---|---|
| S1 — The search | `S1_search.md`, `S1_fig_prisma.png`, `S1_fig_prisma.svg`, `S1_stage1_query_log.csv`, `S1a_stage1_candidates.csv`, `S1_stage2_coverage.csv`, `S1_screened_candidates.csv`, `S1_surveys.csv`, `S1_cells.csv`, `S1_survey_query_log.csv`, `S1_other_sources.csv` | Both stages of the search, the flow diagram, every query and list, the first stage's candidate pool, every candidate of the later stages with scores, decision and reason, every peer-reviewed survey screened with its coding, and the works readers named, with decision and reason. For 32 of the surveys, it also holds how each built its taxonomy and how its categories map onto the cells of Table 4. |
| S2 — The placement sheet | `S2_placement_sheet.csv`, `S2_counts.py` | Every placed entry (190), as Table 4 and Supplementary Table 7 list them: level, column, markings, flags, deployment point, and a justification per axis. `S2_counts.py` recomputes the counts of Table 4 and Fig. 1, the marks, Tables 9 and 10, the flags, the deployment points, and the alternative readings of Supplementary Appendix B.5 that the sheet's fields decide. |
| S3 — The incidents behind Table 1 | `S3_incidents.md`, `S3_incidents.csv`, `S3_dao_probe.csv`, `S3_panelC_governance.csv` | Panel A: the 127 incidents, the level and rule for each, the judgment calls, and the reports for the four corrected records. Panel B: the 28 DAO incidents of Feichtinger et al., and three further incidents of Ma et al., each with its sources. Panel C: the 12 DAO governance incidents of January 2024 – September 2026 from DefiLlama and DeFiHackLabs, with the selection rule and the sources of each. |
| S4 — The adaptive-acquisition record | `S4_adaptive_acquisition.md`, `S4_adaptive_acquisition.csv` | The five fields behind the flag, the evidence that decided it, and, where that evidence is released code, the release or commit read, for each of the 57 LLM and agentic entries. |
| S5 — Extended cell notes | `S5_cell_notes.md`, `S5_comparisons.csv` | For each cell of Table 4, the longer reading of its occupants, with the figures their papers report, and what prior surveys say about the cell. `S5_comparisons.csv` covers the 55 systems of the three clusters of Supplementary Appendix G: what each verdict reads, its deployment point, its evaluation sets, the figures it reports on them, and whether its code is public. |
| S6 — The agreement study | `S6_agreement.md`, `S6_agreement_codes.csv`, `S6_agreement.py` | Both coders' codes, before and after discussion, for the two rounds of Supplementary Appendix B.7: the 40 systems and 30 incidents of the first round and the 24 works of the second. `S6_agreement.py` recomputes the agreement and Cohen's κ, with the bootstrap intervals, that Section 1.1 and B.7 report. |

## Reproducing the counts

Both scripts use Python 3 and the standard library only.

```
python3 data/S2_counts.py
```

Recomputes, from the placement sheet, the counts the article and its appendices print: the counted systems by level and column (Table 4 and Fig. 1), the marks, Tables 9 and 10, the adaptive-acquisition flags of the LLM and agentic columns, the deployment points, and the alternative readings of Supplementary Appendix B.5 that the sheet's fields decide.

```
python3 data/S6_agreement.py
```

Recomputes the agreement figures of Supplementary Appendix B.7 and Section 1.1 from the coders' codes: for each round, percent agreement and Cohen's κ with a percentile bootstrap interval, and the agreement after discussion.

## Identifiers and reference numbers

Every work in the files is named by its short name and identifier: a DOI, an arXiv id, a URL, or venue and year. The numbers in S2's `ref` column refer to the article's reference list and to the supplement's S-numbered list. Both lists will be posted with the publication version.

## Citation

A citation will be added on publication.

## Contact

[NAME], [EMAIL]
