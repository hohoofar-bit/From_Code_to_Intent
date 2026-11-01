# Supplement S6 — The agreement study

Supplementary Appendix B.7 reports an agreement study in two rounds, and Section 1.1 its main figures. `S6_agreement_codes.csv` gives both coders' codes, and `S6_agreement.py` recomputes every figure that B.7 and Section 1.1 report from them. The first coder's codes are ours. The second coder is one of the authors and took no other part in the study, and consented on 31 October 2026 to the release of both coders' codes, before and after discussion. The coders' free-text entries (the governing set, the rule cited, notes) are not included.

**The two rounds.**
- *Round 1* (27–29 October 2026), on the codebook as it stood on 28 October 2026:
  - 40 counted systems (R01–R40), drawn from the 136 counted entries that S2 then held, ordered by reference number, with Python's `random.Random(20261027).sample`;
  - 30 incidents of Table 1 (I01–I30), ten drawn from each panel (seeds 20261028 to 20261030), leaving out Beanstalk, The DAO, and Tornado Cash, whose levels the codebook names.
- *Round 2* (29–31 October 2026), on the codebook as revised after the reviews and blinded in the same way: the 24 works on which the gap claims rest and which the first round had not coded (T01–T24). They are every counted system at the description-mismatch level (9) or in the agentic column (12) that the first round had not coded, and the level's three studies. They were chosen, not drawn, and listed in an order shuffled with seed 20261029.

**Columns of `S6_agreement_codes.csv`.** One row per coded item and field.
- `round`, `id`, `kind` (system, incident, or work), `item` (a work's short name as in S2; an incident as in S3, with its date), `group` (the panel of Table 1, for incidents), `reference` (the number Table 4 or Supplementary Table 7 prints, [n] in the article's list or [Sn] in the supplement's; for incidents, Table 1 and S3).
- `field`:
  - `marking` (round 2 only): counted, or the marking of B.3;
  - `row`: ES, PM, or DM;
  - `glossary`: whether the glossary of B.1 decided the row (the second coder's form names the line);
  - `column`: Rule-based, ML, LLM, or Agentic;
  - `flag`: the adaptive-acquisition flag (yes, no, unverified), n/a where the coder did not put the work in the LLM or agentic column;
  - `flag_evidence`: the evidence that decided the flag (B.2);
  - `level` (incidents): ES, PM, DM, no level, or outside;
  - `other_reading` (incidents): no, or yes with the other reading the coder recorded.
- `first_before`, `second_before`: each coder's codes, given independently.
- `first_after`, `second_after`: the codes after discussion.
- `first_final`: the code S2 or S3 holds now. It differs from `first_after` only for Curio (I18), which we recoded under the revised codebook (B.7).
- `note`: what changed in discussion, and the codes that remain in dispute.

Values are as each coder entered them (the second coder wrote "method text" where we write "method text only").

**Recomputing.** `python3 S6_agreement.py` (Python 3, standard library) prints, for each round, the agreement and Cohen's κ, with 95 % percentile bootstrap intervals over items (5,000 resamples) for the row, the column, and the incident level. The bootstrap is seeded as the rounds were: 20261027 for round 1, and 20261029 for round 2 and for both rounds together. It also prints the agreement after discussion. Its output:

| Round | Field | Agreement before discussion | Cohen's κ (95 % interval) | After discussion |
|---|---|---|---|---|
| 1 | Row (40 systems) | 37 | 0.86 (0.67–1.00) | 40 |
| 1 | Column | 39 | 0.95 (0.83–1.00) | 39 (SSR) |
| 1 | Glossary decided the row | 32 | 0.46 | |
| 1 | Flag (both in the LLM or agentic column) | 8 of 8 | | |
| 1 | Incident level (30 incidents) | 28 (panels A 9, B 10, C 9) | 0.91 (0.77–1.00) | 29 (BarnBridge); 28 with Curio recoded |
| 1 | Another reading | 18 | 0.12 | |
| 2 | Scope and marking (24 works) | 24 | 1.00 | 24 |
| 2 | Row | 24 | 1.00 | 24 |
| 2 | Column | 23 | 0.94 (0.79–1.00) | 24 |
| 2 | Glossary decided the row | 22 | | |
| 2 | Flag (16 works both in the LLM or agentic column) | 15 | 0.64 | 24 of 24 works |
| 1 and 2 | Row (64 works) | 61 | 0.92 (0.82–1.00) | |
| 1 and 2 | Column (64 works) | 62 | 0.95 (0.88–1.00) | |
