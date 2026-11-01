# Supplement S3 — The incidents behind Table 1

**Source.** Chaliasos et al. (ICSE 2024) analyze the DeFi incidents of Zhou et al. (S&P 2023) and release them with their causes and reported losses (github.com/StefanosChaliasos/sc-defi-security). We used the paper's own selection: incidents with at least one cause in the smart-contract or protocol category. It gives 127 incidents and $2,331.9M in reported losses, February 2020 – July 2022 (the full database of the release runs from July 2018 to November 2022).

**Coding.** Each incident is coded by what it violated, as read from the source's description and causes, with the rules of Supplementary Appendix B.1:
- **Execution-semantics level:** the incident violates any execution-semantics property.
- **Protocol-mechanism level:** it violates a mechanism invariant and no execution-semantics property.
- **Description-mismatch level:** the property it violates can be stated from nothing but a named description.
- **Outside the taxonomy:** the decisive step was a key compromise or an off-chain component.
- **No level:** a majority, bought or amassed at low turnout, executed its own proposal within the mechanism's rules. Supplementary Appendix B.1 places only a flash-loaned or instantaneous majority at the protocol-mechanism level.

A **judgment call** is an incident whose description admits another reading: for twenty-five incidents the other of the two lower levels, for five the trust boundary in one direction or the other, and for the two bought majorities the protocol-mechanism level. Its alternative is recorded, and the column "Judgment calls moved" of Table 11 (Supplementary Appendix E) moves every such incident to its alternative.

**File.** `S3_incidents.csv` has one row per incident. It gives:
- the source's identifier, title, date, averaged reported loss, causes and layers;
- our level and the rule applied;
- whether it is a judgment call, the alternative level, and the direction of that other reading (the other lower level, the trust boundary, or a bought majority read as economic);
- a note.

The incidents are sorted by loss.

**Rules applied.**

| Level | Rule | Incidents |
|---|---|---|
| Execution-semantics | generic missing or wrong access, owner, initializer or visibility check | 19 |
| Execution-semantics | reentrancy, including token callbacks | 12 |
| Execution-semantics | arbitrary call or delegatecall to an attacker-chosen target | 8 |
| Execution-semantics | arithmetic or precision error | 4 |
| Execution-semantics | unchecked return value or silently succeeding call | 2 |
| Execution-semantics | language-semantics pitfall (msg.value reused in a loop) | 1 |
| Protocol-mechanism | on-chain price or oracle manipulation | 26 |
| Protocol-mechanism | accounting, share or reward invariant broken (double counting, shares not burned, inflated rewards) | 21 |
| Protocol-mechanism | AMM invariant, liquidity-share or slippage manipulation | 13 |
| Protocol-mechanism | non-standard token behavior (fee-on-transfer, rebase) breaking protocol accounting | 7 |
| Protocol-mechanism | a bridge releases or mints what was never locked | 5 |
| Protocol-mechanism | an unregistered token or contract accepted where the mechanism requires a registered one | 2 |
| Protocol-mechanism | flash-loaned or instantaneous governance majority | 1 |
| Protocol-mechanism | scam or camouflaged token | 1 |
| no level | no level: a majority bought or amassed at low turnout executed its proposal within the mechanism | 2 |
| outside the taxonomy | trust boundary: key compromise or off-chain component | 3 |

**Four corrected records.** Table 11's corrected figures (the column "Share, four records corrected" and the figures in parentheses) replace four recorded losses that the source's own description, or a contemporaneous report, contradicts. The other figures keep the source's.

| Incident | Recorded | Corrected | Report |
|---|---|---|---|
| 20211102_VesperFinance_S (2021-11-02) | $300.0M | $3.5M | Fairyproof, "Preliminary analysis of attack on Vesper Lend beta" (2 Nov 2021): "At least 660 ETHs valued at 3.5 million USD were exploited" — https://fairyproof.substack.com/p/preliminary-analysis-of-attack-on-vesper-lend-beta-31844b6c274c |
| 20211029_AutoSharkFinance_S (2021-10-29) | $200.0M | $2.3M | AutoShark Finance, "Post mortem review on economic attack" (29 Oct 2021): "The attacker made off with 4348.5 BNB"; valued at the October 2021 average BNB price ($524.36) — https://medium.com/autosharkfin/post-mortem-review-on-economic-attack-af27e76b746e |
| 20210204_YearnFinance_CSR (2021-02-04) | $35.0M | $11.0M | the source dataset's own description of the incident: "$11 million was lost from the vault" — Chaliasos et al. dataset, incident description |
| 20210408_UraniumFinance_S (2021-04-08) | $13.0M | $1.3M | the source dataset's own description of the incident: "$1.3Mil" — Chaliasos et al. dataset, incident description |

With the four corrections, the total is $1,802.0M.

**Duplicate.** The source records the Origin Dollar incident of November 2020 twice (incidents 57 and 166). Both rows are kept, as in the source. Removing the duplicate moves no share by more than 0.22 points.

## S3.2 Panel B of Table 1: the DAO incidents of Feichtinger et al.

**Why.** Panel A holds no description-mismatch incident. A level that no incident satisfies would be a definition of nothing. Panel B codes, by the same rules, an incident list that others drew up for another purpose.

**Frame.** The frame was fixed before any incident was coded. It is the 28 rows of the group "Incidents & attacks" in Table 1 of Feichtinger et al., *SoK: Attacks on DAOs* (AFT 2024, doi:10.4230/LIPIcs.AFT.2024.28). The source lists audit findings and research results as separate groups; those are not part of the frame. The list is the source's own: no incident was added or removed.

**Rules.** The rules are those of Supplementary Appendix B.1, as used for Table 1: the smallest-context rule, and the Governance and Scams clauses. Each incident is coded by what its decisive step violated. The facts come from post-mortems, security-firm analyses and the proposals themselves on chain, and each row of `S3_dao_probe.csv` gives its sources.

Two outcomes are recorded for incidents that fit no level:
- **No level:** the mechanism executed, for a majority it recognized, a proposal that was stated openly or not at all.
- **Outside:** a custodial, off-chain or social event.

Losses are the source's figures. Where primary sources disagree, the row says so.

**Test.** The test was fixed before coding. The definition fails its own paradigm case in either of two events:
- no incident reaches the description-mismatch level;
- incidents whose proposal text contradicts the payload are placed elsewhere for a reason that is not a stated rule.

**Result.**

| Level | Incidents | Losses (source's figures) | Incidents |
|---|---|---|---|
| Execution-semantics | 5 | $59.0M | The DAO, Genesis Alpha, ForceDAO, Audius, Temple DAO |
| Protocol-mechanism | 5 | $231.0M | Mango Markets, Beanstalk, Tornado Cash, Maker DAO B, Curve B (Mochi) |
| **Description-mismatch** | **5** | **—** | Yam Finance, BigCap DAO, Indexed Finance, Kleros, Tally |
| No level | 10 | $17.0M | Build Finance, Yuan Finance, True Seigniorage Dollar, Synthetify, Curio, Venus, Compound, Maker DAO C, Curve A, Paladin Lending |
| Outside | 3 | — | Steemit, Binance, Wonderland DAO |

**What the result shows.**
- **The test is passed.** Five incidents reach the description-mismatch level, and in three of them the proposal text and the payload are confirmed on chain: Yam Finance, BigCap DAO and Indexed Finance.
- **Two paradigm cases go to the protocol-mechanism level, each by a stated rule.** Beanstalk had a flash-loaned majority. Tornado Cash had its approved code replaced before execution. Their mismatch of text and payload is recorded as a *broad reading*. Under that reading, the description-mismatch level holds 8 incidents and about $184M.
- **Nine incidents are judgment calls.** Their alternatives move the description-mismatch level between 3 and 6 incidents.
- **Four of the five description-mismatch incidents never executed.** They are Yam Finance, BigCap DAO, Indexed Finance and Kleros. In each, someone read the payload against its text. The fifth, Tally, was an unintentional front-end bug that caused no loss.
- **Ten incidents fit no level.** In these, a majority acted within the mechanism's rules, and nothing was violated against which a level could be stated. Two of them, Build Finance and TSD, are also in the record behind Table 1, where they form the row "No level".

**Three further incidents (Ma et al.).** Ma et al. (IEEE TSE 2025, doi:10.1109/TSE.2025.3543280), Table IX, list 13 governance attacks. They collected them from security reports to test their detector, and ten of them are also in panel B. The other three are coded in `S3_dao_probe.csv` (frame "Ma et al.") and are not added to the panel:
- **Fortress Protocol** (May 2022): execution-semantics level. The Umbrella Network oracle's signer check had been commented out, so anyone could post the FTS price. The proposal, whose text stated its action accurately, was the precondition.
- **Swerve Finance** (March–April 2023): no level. A bought majority executed proposals whose texts stated nothing ("Bye Swerve"). Press reports called the attack failed, but on chain it took about $93K in admin fees.
- **Atlantis Loans** (June 2023): no level. Proposal 52 handed admin of the aToken contracts to an attacker contract; its text was not found.

Ma et al.'s detector flags eight of the thirteen for a description that states no intent. A text that states nothing cannot be contradicted, and the rules place such cases at no level.

**Who coded.** We coded each incident by the rules, from the sources given per row.

## S3.3 Panel C of Table 1: DAO governance incidents, January 2024 – September 2026

**Why.** Panel B ends in March 2024. We found no peer-reviewed incident list for DAO governance after it, so panel C codes what two public lists record.

**Frame.** The selection rule was written and frozen on 15 October 2026, before any incident of the panel was read or coded. Panel C is the union of:
1. **DefiLlama Hacks** (api.llama.fi/hacks, the copy retrieved on 16 October 2026, 1,303 records): every record with `classification` "Governance" dated 1 January 2024 – 30 September 2026 (10 records);
2. **DeFiHackLabs** (github.com/SunWeb3Sec/DeFiHackLabs, as of 15 October 2026): every entry in the same window whose root-cause line, the title text after the protocol name, matches `govern|proposal|\bvot(e|es|ing)\b|quorum|\bDAO\b` (case-insensitive); 4 of the 490 entries in the window.

The same incident in both lists is one record (TOPBPool, Term Finance), which gives 12 records. Nothing was added or removed by hand:
- DefiLlama records one Neutron proposal as two incidents, Astroport and Drop; both records are kept, as in the source.
- RetoSwap, which DefiLlama classifies as governance, is kept and coded outside the taxonomy.
- An incident outside the rule is not coded, however relevant it looks (for example DAOstack, September 2026, whose root-cause line names none of the terms).

**Rules.** The rules are those of Supplementary Appendix B.1, as for panels A and B. Facts come from the proposals, the transactions, project statements and security-firm analyses; each row of `S3_panelC_governance.csv` gives its sources. Losses are DefiLlama's figures, or DeFiHackLabs' where DefiLlama has no record (StrongBlock, Yam Finance); where primary sources give other figures, the row says so.

**Result.**

| Level | Records | Losses (source's figures) | Records |
|---|---|---|---|
| Execution-semantics | 0 | $0 | — |
| Protocol-mechanism | 2 | $0.31M | ZoomerCoin, FutureSwap |
| **Description-mismatch** | **6** | **$38.6M** | BonkDAO, BarnBridge, Panther Protocol, Term Finance (TermMax vaults), Drop (Neutron proposal 9), Astroport (Neutron proposal 9) |
| No level | 3 | $1.8M | Token of Power (TOPBPool), StrongBlock, Yam Finance |
| Outside | 1 | $2.7M | RetoSwap |

The total is $43.4M.

**What the result shows.**
- **Six records reach the description-mismatch level.** In five, from four incidents (BonkDAO, Term Finance, BarnBridge, and Neutron's proposal 9 for Astroport and Drop), the proposal's payload did what its text did not say. In the sixth, Panther Protocol, a governance module executed transactions that no approved decision called for.
- **In each of the four incidents the votes were bought**, for far less than the proposal then moved, and each proposal executed.
- **Seven records are judgment calls.** Their alternatives are recorded per row; moved to them, the description-mismatch level keeps two records and 65.7 % of the reported loss.
- **Three records fit no level.** A majority executed its own proposal within the rules, and the proposal stated nothing (StrongBlock: "1"; Yam Finance: an empty description) or its text was not found (TOPBPool).
- **ZoomerCoin is the one record in the three months that panels B and C share** (January – March 2024); panel B does not list it. DefiLlama records a flash-loan governance attack, but the transaction that DeFiHackLabs reproduces for Zoomer contains no governance step: it buys ZOOMER with flash-loaned WETH, calls an unverified contract that reads the pair's reserves, and sells, five times. The record is coded by that transaction, at the protocol-mechanism level (on-chain price manipulation), as a judgment call (alternative: execution-semantics level, DeFiHackLabs' business-logic flaw).

**Limits.** The two lists are public and not peer-reviewed, and they record what is reported to them. Twelve records, two of them from one proposal, set no trend.

**Who coded.** We coded each record by the rules, from the sources given per row.
