# Insights editorial implementation register

Established 12 November 2026. Repository: `sightlines-advisory/web-prototype`; default branch `main`. **Baseline identifiers below are Git blob SHAs, not commit IDs.** They identify the exact HTML file versions fetched at register creation. No article copy was edited in establishing this register.

## Controls

- Article workflow: **Baselined → Gap assessed → Changes proposed → Amend / Approved / Held → Implemented in staging → Staging verified**. Publication approval is separate.
- Approval: reviewer explicitly approves the **proposed changes** before an article HTML update. Never infer approval from the committee decision or the gap assessment.
- Three structural tests: **Opening** identifies audience, question and decision relevance; **Body** provides evidence, interpretation, business implications and a suitable illustration; **Closing** gives management action, uncertainty/limitations and two complementary readings.
- Pass = meets test; Partial = some components present; Pending = not audited. Track change type Add / Change / Delete and reason, plus author approval, source/IP conditions and link checks.
- No unapproved rewrites of existing facts, source attributions or fictional company details. Record every implementation commit and staging verification outcome here.
- Staging base: https://sightlines-advisory.github.io/web-prototype/insights/ . Staging is not production approval.

## Article baseline and decision register

| ID | Batch | Article (staging path) | Baseline HTML blob SHA | Editorial decision | Byline (current or to confirm) | Opening | Body | Closing | Approval | Implementation |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | Batch 1 | [five-steps-confident-start-climate-reporting](https://sightlines-advisory.github.io/web-prototype/insights/five-steps-confident-start-climate-reporting.html) | `dcf7af55667f021720b72649df752ee6b1a7f321` | Keep and elevate: outputs, ownership and next actions; retain Sean voice | Sean Rugers | Partial | Partial | Partial | Approved with amendments (12 Nov 2026) | Implemented; staging verification pending |
| 02 | Batch 1 | [how-climate-risks-affect-company-value](https://sightlines-advisory.github.io/web-prototype/insights/how-climate-risks-affect-company-value.html) | `42ab5eee62a33da76e176f0d143806fe3bf29739` | Add worked risk to financial consequence illustration; link future Method | Susan McHattie (current byline; approval to confirm) | Partial | Partial | Partial | Approved (12 Nov 2026) | Implemented; staging visual verification pending |
| 03 | Batch 1 | [global-warming-projections-business](https://sightlines-advisory.github.io/web-prototype/insights/global-warming-projections-business.html) | `7fb306014ae77b21705b51afef05a773b7bbc9a4` | Preserve deep Explainer; leadership guide and checklist B; Verdant Grid addition; closing question | Susan McHattie | Partial | Pass | Partial | Approved as amended (12 Nov 2026) | Implemented; browser/source verification pending |
| 04 | Batch 2 | [how-climate-scenarios-are-useful](https://sightlines-advisory.github.io/web-prototype/insights/how-climate-scenarios-are-useful.html) | `8ee65e7a83536e7a6e4881104c754fe50fc28e18` | Decision-focused scenario analysis; preserve five SSPs and Junction Freight; checklist B | Susan McHattie | Partial | Pass | Pass | Approved with amendments (12 Nov 2026) | Implemented; visual/source verification pending |
| 05 | Batch 2 | [where-is-business-value-in-climate-action](https://sightlines-advisory.github.io/web-prototype/insights/where-is-business-value-in-climate-action.html) | `d14d923004a3cab80adae5f5bc835a01ae5063f4` | Feature for CEOs; investment decision; reduce repetition; cover asset outstanding | Susan McHattie | Pending | Pending | Pending | Not requested | Not started |
| 06 | Batch 2 | [shape-competitive-future-through-transition](https://sightlines-advisory.github.io/web-prototype/insights/shape-competitive-future-through-transition.html) | `26a448351710f5dee5d6854429a1d682a22528fb` | Develop signature Insight; competitive choices and tradeoffs; link future value Method | Confirm | Pending | Pending | Pending | Not requested | Not started |
| 07 | Batch 3 | [investors-climate-enterprise-value](https://sightlines-advisory.github.io/web-prototype/insights/investors-climate-enterprise-value.html) | `a547ca20e771814feeb07e68ec287f178f1e43f9` | Add evidence CFO/board could present to capital providers | Susan McHattie | Pending | Pending | Pending | Not requested | Not started |
| 08 | Batch 3 | [customers-environmental-claims-value](https://sightlines-advisory.github.io/web-prototype/insights/customers-environmental-claims-value.html) | `330b753e8baa38f3299a3b2fc615c343c3f21331` | Add procurement/renewal example; distinguish business customers from consumers | Susan McHattie | Pending | Pending | Pending | Not requested | Not started |
| 09 | Batch 3 | [employees-climate-credible-action](https://sightlines-advisory.github.io/web-prototype/insights/employees-climate-credible-action.html) | `fd352b1eb4545d9e074143d0525ad6527814db68` | Lower prominence; connect workforce capability to delivery and performance | Susan McHattie | Pending | Pending | Pending | Not requested | Not started |
| 10 | Batch 3 | [which-stakeholder-expectations-affect-your-business](https://sightlines-advisory.github.io/web-prototype/insights/which-stakeholder-expectations-affect-your-business.html) | `330e12049b5f84cdf742c7bc191bd09b2c45891f` | Stakeholder behaviours, enterprise value materiality test, Fieldwork and Mallee examples | Susan McHattie | Pass | Pass | Pass | Approved with amendments (12 Nov 2026) | Implemented; browser/source verification pending |
| 11 | Batch 4 | [suppliers-climate-delivery](https://sightlines-advisory.github.io/web-prototype/insights/suppliers-climate-delivery.html) | `147eedf06e4a2584c88784815f4f573d6e6efe41` | Keep contextual; separate practical supplier Guide to commission | Susan McHattie | Pending | Pending | Pending | Not requested | Not started |
| 12 | Batch 4 | [what-support-is-available-for-transition](https://sightlines-advisory.github.io/web-prototype/insights/what-support-is-available-for-transition.html) | `96a8e44578621bcf0c39f3aced731af91f541e5c` | Clarify/retitle transition enablers; retain fictional companies | Confirm | Pending | Pending | Pending | Not requested | Not started |

## Batch 1 gap assessment (12 November 2026)

### 01 Five steps to a confident start on climate reporting
- **Opening — Partial:** Identifies finance/reporting teams, Group 2 and Group 3, and the first reporting task. The management decision and expected outcome are not summarised up front.
- **Body — Partial:** Five practical steps and existing information sources are clear. Ownership, tangible outputs and handoffs are implied rather than mapped; no concise illustrative owner/output/next action sequence.
- **Closing — Partial:** 'What you can do this month' and support choices are practical, and two related readings appear. Uncertainty is covered in a general regulatory caveat but not specifically in terms of evidence gaps, estimates or unresolved management judgements.
- **Propose (not approved):** Add a short five-row Step / Initial output / Management owner / Next action table after the steps; add one sentence near the opening about the decision it supports; explicitly distinguish verified information from assumptions and items to resolve in the closing. Keep Sean's voice and the guide as the deeper resource. Verify guide approval and current reporting statements before publication.

### 02 How do climate risks affect company value?
- **Opening — Partial:** Manufacturing example and question of business consequences work well, but the target decision maker and the choice enabled are not explicit.
- **Body — Partial:** Substantial physical/transition tables, enterprise risk register fields, and evidence caveats. Existing flood distribution centre example traces qualitative effects, but not a worked numerical/financial translation with assumptions, period, uncertainty and management response comparison.
- **Closing — Partial:** Invites readers to bring a risk and asks a relevant investment question, and provides two readings. Limitations are stated throughout, but a concise closing on what cannot yet be concluded is missing.
- **Propose (not approved):** Add a labelled **illustrative** flood interruption bridge: operational disruption → sales at risk and extra cost categories → assumptions and illustrative arithmetic → uncertainty → decision options. Use clearly fictional inputs only, with no implied prediction. Link to a deeper Method article only when that article exists; do not create a dead link. Add a concise action/uncertainty close.

### 03 What can a global warming projection tell your business?
- **Opening — Partial:** Investment and disclosure decisions are explicit, but the audience and main selection criteria are buried in several paragraphs. A short executive summary and decision checklist are missing at the top.
- **Body — Pass (subject to source verification):** Strong scientific definitions, source comparison, IPCC panel explanations, UNEP cases and business applications. The IPCC figure is linked rather than embedded. Check technical claims and UNEP values against original publications separately; copyright clearance remains on hold.
- **Closing — Partial:** Has a detailed scenario/timeframe checklist and management meeting action, plus two related readings. Uncertainties are discussed in the body but not explicitly recapped as limits on site or company forecasts.
- **Propose (not approved):** Add a brief executive summary and three-item decision checklist before the technical sections; clarify that global projections alone cannot establish site impacts or financial outcomes. Retain original source links and existing deep technical detail. Flag an apparent grammatical error in the two fictional company examples for correction during the edit.

## Batch plan
- **Batch 1:** Five Steps; Climate Risks and Company Value; Global Warming Projections.
- **Batch 2:** Climate Scenarios; Business Value in Climate Action; Competitive Future.
- **Batch 3:** Investors; Customers; Employees; **Stakeholder Expectations** (four articles by agreement).
- **Batch 4:** Suppliers; Transition Enablers.

## Implementation log
No article implementation commits or approvals yet. Initial register commit is recorded in the GitHub file history.

### Article 01 implementation — 12 November 2026
- Approved four proposed changes with ownership amendments: Step 2 **Finance, with Risk, Sustainability and Operations**; Step 4 **Finance, with Operations, Sustainability and Procurement**.
- Article HTML commit: `73aabaf19703763b8977c99d5211c319fccaf16e`; resulting blob SHA: `8fbc373b6a203f13cfb204b2f27c29385b612ce5`.
- Implemented opening, outputs/ownership table, evidence status definitions and management close. Original five steps, download section and two related readings retained.
- Content replacement checks passed. Browser visual/mobile, external PDF link and publication source checks remain pending; **not publication approved**.

## Cross-article illustrative company distribution task — added 12 November 2026
**Status: Open; assess during each article's editorial review; no article substitutions pre-approved.**
- Use the editorial suite's illustrative company and leadership register as the controlled source, including proposed C5 scaleup **Verdant Grid Technologies Pty Ltd** (fictional).
- Inventory company mentions across all 12 articles; track each company's appearances, sector, persona fit, decision relevance and executive voice. Aim for an **even, purposeful spread**, not an artificial equal quota.
- Identify articles where Verdant Grid's opportunity-led scaleup, energy storage, investor readiness, growth constraints or reporting applicability genuinely strengthen the illustration. Propose displacing a less apt existing company where appropriate; preserve evidence, narrative continuity and explicit fictional status.
- Show **Before / Proposed / Reason** for every substitution, including Verdant Grid executive name, role and question; obtain editorial approval before staging edits.
- Prioritise evaluation in the scenario, warming projections, value creation, investor and transition enabler articles; do not change examples merely to equalise counts.
- Maintain a distribution matrix and revisit after all four batches.

### Article 02 implementation — 12 November 2026
- All six proposed edits explicitly approved: opening; enterprise-value questions; fictional Junction Freight flood-financial bridge; risk-register example; response/value comparison; action/uncertainty close.
- Article HTML commit: `a2d2e99e733c47ba970844b347af36a97929c617`; resulting blob SHA: `731f85c92bb606780f5be58d77e7a4500976bcb5`.
- Illustrative calculation checked: ($120,000 × 4 × 50% × 30%) + $55,000 + $20,000 = $147,000. Not an annual expected loss, scenario projection or valuation.
- Existing technical risk tables, register fields and two related readings retained. No future Method dead link introduced.
- Repository content verification complete; live browser/mobile visual rendering, external links, source and author/publication checks pending. **Not publication approved.**

### Closing-question formatting standard — 12 November 2026
- Article 2's closing-question HTML pattern is the reference: `<div class="article-callout"><strong>…?</strong></div>` immediately before source notes/related readings.
- Article 1 updated to match: commit `37ea1f0f53a544b747839924f6dcda983ed0ea79`, blob `9b9db8fe03b80e598a319b5c2991c3f773fd75de`.
- Future articles: apply this treatment when an approved substantive closing question exists; do not manufacture a question, add one-off CSS, or modify unapproved wording. Verify visual/mobile treatment in staging.

### Article 03 implementation — 12 November 2026
- Seven editorial edits approved as amended, including national and local projections, Susan's **leaders** voice, Harbourstay/Southern Cross/Verdant Grid illustrations and closing-question callout.
- Article commit `5aa300e4e6c9596b60cbc723122a228b40cd4c1c`, blob `436a9b17f039fcf14f7330b917e5e01f52135f02`; CSS commit `8f76ef6e7640762d5dd6e60fd4ffd1e00dc5ba55`.
- Approved checklist B implemented twice, with Steel Blue on white, open checkbox below number, accessible native inputs and print CSS. Six checkbox inputs present.
- IPCC source figure link and two related readings retained. **Outstanding:** verify AASB S2 scenario wording, WMO and UNEP figures, IPCC source, rights and mobile/browser rendering; publication not approved.

### Article 03 checklist refinement — 12 November 2026
- Opening 'Three things leaders need' changed to ordinary text bullets, preserving approved wording. Article commit `7825ae172f723943c190b610746c576a1292e82a`.
- Closing checklist remains the sole numbered, tickable component; numbers now match heading font size (18–23px responsive). CSS commit `50b418cbdad8b8ac06f4e3ade56898cff0d01e0a`.
- Design standard updated: summaries use bullets; actionable checklists use reusable component. Live visual verification remains pending.

### Article 03 checklist alignment refinement — 12 November 2026
- Checklist number aligned with the first heading line, matching font size and line-height; checkbox centred horizontally in number column beneath it. CSS commit `f256cdc6060c0a8ea62c47c3b2d73c043877ddcc`.
- Reusable design rules updated. CSS/code checks complete; browser visual review pending.

### Article 03 table legibility and source type — 12 November 2026
- UNEP table assigned dedicated class and wider minimum columns, allowing horizontal scrolling rather than hyphenating or splitting words. Article commit `60a8bca88cd0b33a6316d91b53bea0b3b896459e`.
- Global Insights table rule now disables automatic hyphenation and midword breaks. UNEP source paragraph uses standard 12px source typography. CSS commit `0c27fc1930d653830bcf457b67138aa41c3318d4`.
- Words remain intact; line breaks between complete words remain allowed. Browser/mobile verification pending.

### Article 04 implementation — 12 November 2026
- Seven edits approved with amendments. Opening now says: “The question for leaders is which business decisions remain valuable across different futures.”
- Junction Freight example uses “Shared Socioeconomic Pathway”; source table spells out NGFS, IEA, CSIRO/Bureau of Meteorology and UNEP. The five SSP narratives and executive questions remain.
- Added fleet replacement decision bridge, five-step tickable Checklist B, 12px table source notes, no-hyphenation table design through shared CSS, and final closing question callout.
- Article commit `2f986a7d1185db0bb801741d14b276df117295d4`, HTML blob `90efc8531d481aa0f78be2c24a2ca01e325771d9`.
- Code checks: five checkbox inputs, three table source notes, Junction Freight executive names, and two related readings. **Outstanding:** visual/mobile checks; verify AASB S2 paragraphs, IPCC SSP descriptions and source editions/links before publication. No publication approval.

### Article 10 stakeholder perspectives implementation — 12 November 2026
- Six edits approved with exact user amendments to opening question, Fieldwork and Mallee leadership questions, and concluding sentence.
- Added relevance/consequence/evidence materiality test, revised stakeholder comparison and AASB S2 questions, company illustration styling, and closing question callout. Removed duplicate introductory investor link and source note.
- Commit `46f0a380b18e5c5136263aa1db28f9b862a7c3b7`; blob `287e94049b5a1489cc572fed3eae60ef14a195a7`.
- Structural checks: two illustrative company blocks, one source note, one closing callout and one table source note. Shared CSS carries no automatic table hyphenation and standard source type. Browser/mobile verification and original source checks outstanding; no publication approval.

### Cross-article illustrative company consistency pass — 12 November 2026
- Applied existing shared Green Copper illustrative company component to Article 2 Junction Freight (commit `c54c3984ecca0a5ccee9095298e90a6b52ee60f6`) and Article 3 Harbourstay, Southern Cross Commercial Finance and Verdant Grid (commit `5e29ee091be8784e8b94d4ad8b832481d9ca9476`).
- Updated Article 4 Junction Freight opening to avoid repeating the heading (commit `fd540785456f86618493510472a38b671cd42f1c`), and stakeholder overview Fieldwork/Mallee openings likewise (commit `60c2d75d231deef84f746d08477b7965e50890bd`). Preserved approved leadership questions and substantive data.
- Formalised the three narrative modes — enterprise illustration, integrated narrative highlight, executive perspectives — and editorial/verification gate in page rules (commit `cace18723b6a4d20fd375cfe195c12dc696f5fc6`). Apply to Article 5 and all subsequent articles in this editing process.
- **Outstanding:** browser/mobile visual inspection and semantic markup checks before publication. Changes are staging-only; no publication approval.

### Article 5 — Where is the business value in climate action? — approved implementation 12 November 2026
- User approved all seven proposed edits, with exact amendments to Edit 1 standfirst, CEO/MD paragraph and portfolio leadership question; Edit 2 South Pole interpretation; Edit 5 five-question introduction; Edit 7 final portfolio question.
- Staging HTML commit `f1e5b2daafbb6d9430fff3ee24d4457ef0ad74dd`; blob `d3aa20a2d56459d6415ba10377fd7e192a55e5bd`.
- Retained three South Pole evidence figures and source qualifications, four Advanced criteria distinct from four implementation building blocks, five CVF method questions, and original report-cover placeholder. Added Verdant Grid executive-perspectives illustration, enterprise investment test, single approved closing callout and secondary contact link.
- Structural check: three evidence figures, one illustrative company component, one closing callout, five method questions. **Outstanding:** browser checks at 360px/768px/desktop, accessibility, report source figure/definitions verification, cover image rights and upload. Staging only, not approved for publication.

### Illustrative company narrative flow — 12 November 2026
- Article 5: inserted user-approved transition before Verdant Grid; combined short opening paragraphs; retained separate paragraph after Daniel's leadership question; combined final synthesis into one paragraph (commit `f3e2883fd1b24549c65e6c38334b84c9b075dfcc`).
- Applied same paragraph-flow principle to Article 2 Junction Freight, Article 3 Verdant Grid and Article 4 Junction Freight; preserved distinct executive questions and substantive content. Repaired incomplete introductory sentences left by earlier heading edits. Stakeholder examples already follow the continuous introduction plus separate question pattern.
- Recorded reusable rule in page rules (`9dd3458a6f909615b2c7ba7775f17b1ea066b702`), updated shared CSS spacing (`34a0b2a9d9c861ee67150b451c87c74e9ecdf6bf`), and refreshed CSS cache keys across five affected articles.
- Staging only; browser visual checks remain outstanding.

### Article 6 — Investors want to understand how your business will create value — approved implementation 12 November 2026
- All seven editorial edits approved and implemented in staging. User amendments retained verbatim for Edit 1 (boards and management; investment-case question), Edit 4 (two-paragraph investor confidence introduction), Edit 6 (single CVF paragraph) and Edit 7 (final leadership statement). Edit 3 uses Rebecca Chen (CEO) and Thomas Murray (CFO) in the approved executive-perspectives format.
- HTML commit `76bf41a240072389ddaaa5389169d10fb03c584e`.
- Preserved IGCC four-measure evidence figure, Rebecca Mikula-Wright quotation, source note and two related readings. Added Southern Cross illustration, five-question investor test, distinction between disclosure and investor engagement, and one closing-question callout.
- Structural checks: one evidence figure, one illustrative company, one callout, two related articles. **Outstanding:** verify IGCC source survey definitions and figures and quotation against original publication, confirm illustrative executive names against controlled company register, browser/mobile/accessibility and link checks. Staging only; not publication approved.

### Article 7 — Customers need to see the value in your environmental claims — approved implementation 12 November 2026
- Implemented all seven proposed editorial revisions with approved amendments. Exact revised standfirst, continuous opening with brand/customer promise, five-question commercial test headed by Customer behaviour, approved concluding value sentence, and closing two-part customer promise question.
- Retained all four original CPRC infographic measures including 84% and its wording, as explicitly directed; retained Marianne Campbell quotation. Added distinct discussion of stated consumer information needs versus observed commercial procurement and contracts, and greenwashing guidance linking ACCC environmental claims and emissions claims resources.
- Added fictional Junction Freight Services contract-renewal example using established executives Priya Bennett (Managing Director) and Daniel Tran (CFO), one unbordered executive-perspectives block with brand/customer promise synthesis. CVF description is one paragraph.
- HTML commit `33527378e603e16767074540fb763d77f42a1c64`. Structural checks: one evidence figure, one illustrative company, one closing callout, original noindex preserved.
- **Outstanding publication checks:** verify original CPRC and Telstra data, quote and source interpretation, ACCC links, visual/mobile/accessibility and external-link checks. Staging only; no publication approval.

### Article 8 — Employees want credible action and a future they can work towards — approved implementation 12 November 2026
- Implemented four connected propositions: people move with their values; people influence enterprise performance; transition changes workforce capabilities; engaged and capable people make transition deliverable. Use people and workforce naturally; employees in employment-specific contexts.
- Consolidated standard Sightlines evidence figure with six 2025 Australian Deloitte figures (73%, 71%, 45%, 55%, 46%, 38%) and 2026 Australian values-misalignment indicator (over 40%). Prose interprets without repeating measures, distinguishes self-reported survey findings from recruitment/retention or productivity outcomes, and flags source verification.
- Added Fieldwork Technical & Digital illustrative-company story with established Founder and CEO Alex Morgan and exact approved leadership question about attracting, retaining and developing people for a low carbon, resilient economy. Five-question workforce capability test, CVF paragraph and closing question updated.
- HTML commit `07c161def6d9864a600faa9d5b07d9f99dba0558`. Structural checks: one evidence figure, one illustrative company, one closing callout, noindex preserved.
- **Outstanding publication checks:** verify Deloitte 2025/2026 primary Australian report figures, precise denominator and wording, ACTU quote and source link, replace general Deloitte press-room link with direct source links; verify visual/mobile/accessibility and external links. Staging only, not publication approved.

### Supplier article — approved revisions implemented 12 November 2026
- Updated standfirst and opening with user-approved language: bilateral commercial value, prioritisation of material supplier relationships and feasible pathways to ongoing benefit.
- Retained Energy Consumers Australia evidence figure; revised interpretation and survey limitations, including user's wording and correction of 'the might' to 'that might'.
- Expanded publicly observed Telstra FY2025 supplier example (environmental disclosures, contract provisions, eco-design), without claiming outcomes.
- Added fictional Mallee Harvest Foods illustration, retaining established Managing Director Helen Russo, new proposed leadership question and user-approved concluding synthesis.
- Added five strategic leadership questions, continuous CVF paragraph and standard closing-question callout; retained Explainer designation and two related articles; updated customer cross-link title.
- HTML commit `a79db9d46ac412e2ba8dceb340e379460dfc17a8`. One evidence figure, one illustrative company, one callout; staging noindex preserved.
- **Publication gates:** independently verify Energy Consumers Australia question wording/denominators, ACCI quote, Telstra FY2025 primary source and precise description; add direct Telstra source link, confirm visual/mobile/accessibility and reading-time estimate. Supplier Guide not linked because not ready.
