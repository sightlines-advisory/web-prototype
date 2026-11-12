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
| 04 | Batch 2 | [how-climate-scenarios-are-useful](https://sightlines-advisory.github.io/web-prototype/insights/how-climate-scenarios-are-useful.html) | `8ee65e7a83536e7a6e4881104c754fe50fc28e18` | Make scenario selection, consequences and decisions explicit | Susan McHattie | Pending | Pending | Pending | Not requested | Not started |
| 05 | Batch 2 | [where-is-business-value-in-climate-action](https://sightlines-advisory.github.io/web-prototype/insights/where-is-business-value-in-climate-action.html) | `d14d923004a3cab80adae5f5bc835a01ae5063f4` | Feature for CEOs; investment decision; reduce repetition; cover asset outstanding | Susan McHattie | Pending | Pending | Pending | Not requested | Not started |
| 06 | Batch 2 | [shape-competitive-future-through-transition](https://sightlines-advisory.github.io/web-prototype/insights/shape-competitive-future-through-transition.html) | `26a448351710f5dee5d6854429a1d682a22528fb` | Develop signature Insight; competitive choices and tradeoffs; link future value Method | Confirm | Pending | Pending | Pending | Not requested | Not started |
| 07 | Batch 3 | [investors-climate-enterprise-value](https://sightlines-advisory.github.io/web-prototype/insights/investors-climate-enterprise-value.html) | `a547ca20e771814feeb07e68ec287f178f1e43f9` | Add evidence CFO/board could present to capital providers | Susan McHattie | Pending | Pending | Pending | Not requested | Not started |
| 08 | Batch 3 | [customers-environmental-claims-value](https://sightlines-advisory.github.io/web-prototype/insights/customers-environmental-claims-value.html) | `330b753e8baa38f3299a3b2fc615c343c3f21331` | Add procurement/renewal example; distinguish business customers from consumers | Susan McHattie | Pending | Pending | Pending | Not requested | Not started |
| 09 | Batch 3 | [employees-climate-credible-action](https://sightlines-advisory.github.io/web-prototype/insights/employees-climate-credible-action.html) | `fd352b1eb4545d9e074143d0525ad6527814db68` | Lower prominence; connect workforce capability to delivery and performance | Susan McHattie | Pending | Pending | Pending | Not requested | Not started |
| 10 | Batch 3 | [which-stakeholder-expectations-affect-your-business](https://sightlines-advisory.github.io/web-prototype/insights/which-stakeholder-expectations-affect-your-business.html) | `330e12049b5f84cdf742c7bc191bd09b2c45891f` | Keep navigation article; add enterprise value materiality test | Confirm | Pending | Pending | Pending | Not requested | Not started |
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
