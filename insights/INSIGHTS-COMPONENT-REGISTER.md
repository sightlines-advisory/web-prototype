# Insights Component Register
Status: authoritative staging implementation standard, 26 November 2026. Owner: Sightlines Advisory.
Use with INSIGHTS-PAGE-RULES.md. Approved content and design decisions take precedence over legacy code. Unresolved conflicts require owner approval. Shared insights.css is the implementation; reference HTML below is the reuse pattern, not permission to invent variants.

## Components
| Component | Canonical classes / reference | Required behaviour |
|---|---|---|
| Insight cover | tile-art tile-art--insight; index.html | Copper #B66A3C, white main title, Amber #E28A3A half-rule; shared min-height 215px (190px at <=650px), headline clamp(32px,3.6vw,45px); AASB S2 kicker where relevant; white-kicker variant only when approved |
| Explainer cover | tile-art tile-art--fact; index.html | Existing light evidence treatment; same shared height and headline scale |
| Featured Method | featured-method, featured-method-cover, featured-method-sequence; index.html | Deep Navy; five separated 3px lines, last Green Copper; responsive stack |
| Library card | insight-card, insight-card-body, insight-card-meta; index.html | h3 link, type, standfirst, semantic dl/dt/dd, decorative cover aria-hidden, descriptive link |
| Article header | article-hero, lede, article-meta; governance article | eyebrow, h1, standfirst, byline, time, reading time, maturity; noindex while staging |
| Reading layout | article-content; governance article | 760px reading column, wide evidence extends right, responsive reflow |
| Checklist B | sightlines-checklist, sightlines-checklist-item, sightlines-checklist-index, sightlines-checklist-check, sightlines-checklist-content; global-warming-projections-business.html | Native labelled checkbox, 44px target, progress status, temporary selection, number above box; headings match hierarchy |
| Illustrative company | illustrative-company, illustrative-company-header, illustrative-company-kicker, illustrative-company-rule; where-is-business-value-in-climate-action.html | Unbordered, fictional status, Green Copper rule, Deep Navy name, preserve narrative |
| Evidence figure | evidence-figure, evidence-figure-head, evidence-compare, evidence-number; where-is-business-value-in-climate-action.html | Visible numbers, named figure and source caption, decorative bars, approved colours, source qualifications |
| Table | article-table-scroll or table-scroll, risk-table; global-warming-projections-business.html | Named focusable scroll region, caption, scoped headers, top-left alignment, no automatic hyphenation, narrow viewport scrolling |
| Lens list | lens-list; what-support-is-available-for-transition.html | Icon-led questions, labels and source note; not a table |
| Quote | attributed-quote | Semantic figure/blockquote/figcaption, Copper rule, source attribution |
| Closing question | article-callout | One final callout, exact approved wording |
| Related reading | article-back article-related, related-articles, related-article | Two genuine related articles with reasons, return link |
| TOC | article-toc | Named navigation, valid section IDs, responsive one-column layout |
| Share / search | article-share, insights-discovery, insights-filters | Native controls, visible focus, live search status |

## Reusable HTML patterns
Insight cover (inside existing card):
```html
<div class="tile-art tile-art--insight" aria-hidden="true">
  <p>AASB S2: STRATEGY</p><strong>Short<br>headline</strong><i class="insight-rule"></i>
</div>
```
Use tile-art--white-kicker only for an explicitly approved white kicker; it changes colour only. Never add a cover aspect ratio or local font size.
Checklist B:
```html
<div class="sightlines-checklist" role="group" aria-label="Board checklist">
  <p class="checklist-progress" role="status" aria-live="polite">0 of 1 steps selected</p>
  <div class="sightlines-checklist-item">
    <div class="sightlines-checklist-index"><span class="sightlines-checklist-number" aria-hidden="true">1</span>
      <label class="sightlines-checklist-check"><input type="checkbox" aria-labelledby="question-1"><span class="sightlines-checklist-box" aria-hidden="true"></span></label>
    </div><div class="sightlines-checklist-content"><h3 id="question-1">Question</h3><p>Supporting text.</p></div>
  </div>
</div>
```
Include visible temporary-selection instructions and aria-describedby as in reference.
Illustration:
```html
<section class="illustrative-company" aria-label="Illustrative company: Name"><div class="illustrative-company-header"><span class="illustrative-company-kicker">ILLUSTRATIVE COMPANY</span><h3>Name</h3><span class="illustrative-company-rule" aria-hidden="true"></span></div><p>Fictional enterprise narrative.</p></section>
```
For other components copy the full current reference markup, including accessibility attributes; do not reconstruct from appearance alone.

## Mandatory gate
Run python3 insights/check_components.py from repository root before staging and after changes. Check source results, compare against reference, verify 360/768/desktop browser, keyboard, 200% text, 400% zoom, screen reader and contrast. Record exceptions and owner approval. No substantive copy edits during design remediation.

## Held conflicts
Small white/pale kicker on Copper fails normal-text AA (white 4.10:1); approved palette retained pending decision. Existing pale Explainer kicker also needs contrast review. Source-note 12px Steel Blue documentation conflicts with P1 14px muted #40586A implementation; retain current rendering pending approval of accessible companion. Filter single-line desktop versus mobile wrapping: retain responsive accessibility behaviour. Legacy CSS outside the canonical Insight cover requires cascade-aware browser regression before removing overrides. Checklist A is not confirmed as a distinct approved reusable implementation; do not invent it.
