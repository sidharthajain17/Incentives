# Incentives Brain: Operating Rulebook

This repository is Sid's private library and thinking engine for investment incentives in India. Every session that opens this repository follows these rules. Read this file fully before doing any work here.

---

## 1. Purpose

Help an investor decide **where and how to invest so that the incentive is eligible, maximised, negotiated well and actually paid.**

The test of success is simple: the CFO is confident the money will come. Reading a policy is the starting point, not the job. The job is to find what others miss: cross-state ideas, structuring options, gaps in the policy, and the right ask.

Built for Sid's own use. When a mandate comes in, Sid uses this to understand what each policy says and does not say, without rediscovering anything or missing anything.

**In scope**
- Choosing the state for a project
- Designing and negotiating the package (investor side)
- Engineering eligibility and structuring the investment
- Valuing the incentive in real terms (ROI)
- Securing sanction and protecting the money after sanction
- Policy advocacy where no sectoral policy exists yet

**Out of scope**
- Advising state governments on designing their own packages (separate skill, not built here)
- Anything that is not an incentive: customs and trade schemes, countervailing duty risk, accounting treatment, general tax advice

### Incentive universe (check all five layers on every mandate)

| Layer | What it covers |
|---|---|
| Central sectoral | Policies, missions and schemes announced by sectoral ministries: Steel, Mines, Coal, New and Renewable Energy, Power, Heavy Industries, Electronics and IT, Petroleum and Natural Gas, Atomic Energy, Ports and Shipping; Textiles, Pharma, Food Processing, Defence, Civil Aviation on demand |
| Regional | Central schemes for specific regions, such as North East (UNNATI) and hill-state or J&K schemes, where the project location qualifies |
| State generic | Industrial policy, GRs, guidelines |
| State sectoral | Electronics, EV, renewables, mining, data centre, textiles and others |
| State tourism | Where the project is tourism |

Then the stacking check: how the layers combine, what is mutually exclusive, overall caps.

---

## 2. Repository layout

```
CLAUDE.md          this rulebook
README.md          dashboard: coverage and last refresh dates
CHANGELOG.md       dated log of every change

framework/         how we think
  decode-template.md        common format for every policy
  instrument-library.md     standard list of incentive instruments
  idea-levers.md            the thinking moves run on every mandate
  intake-questions.md       questions to ask at the start of a mandate
  value-bridge-method.md    headline to real yield method
  state-selection-criteria.md

central/           organised by ministry, e.g. central/steel/, central/power/, central/heavy-industries/
  <ministry>/<policy>-<year>.md   decoded in the same template as state policies
regional/          North East (UNNATI) and other region-specific central schemes
states/
  _coverage.md     state x policy status grid
  <state>/
    profile.md               institutions, people (dated), track record, land, power
    industrial-policy-<year>.md
    sectoral/<sector>-<year>.md
    tourism-<year>.md
    sources.md               every government link with date accessed
sectors/<sector>.md          full incentive map for the sector across all five layers; value chain,
                             capacity unit, instruments that matter, relevant states
comparisons/                 instrument x state master matrix and theme comparisons
deals/deals.csv              deal database
deals/notes.md
plays/                       the brain: trigger, move, precedent, risk
evidence/                    CAG findings, court rulings, IPO document disclosures
watch/pipeline.md            announced but not notified policies, drafts, sunset dates, expected GRs
                             (central, regional and state); advocacy openings
learnings/                   anonymised lessons from mandates
outputs/                     library HTML outputs (decode one-pagers, comparisons, briefs, explainers)
                             never client mandate reports
```

**Ownership:** Claude creates, maintains and indexes every folder and file. Sid never edits the repository. README.md is the index Claude reads at the start of every chat to know what exists and where.

**Naming:** lowercase, hyphens, year in file names for policies (e.g. `states/odisha/industrial-policy-2022.md`).

**Fixed formats:** every decode uses the decode template headings. Every play uses the play fields. Every deal uses the deal columns. Do not invent new structures inside a file type. If a format needs to change, change the template and record it in CHANGELOG.md.

---

## 3. The client journey (nine stages)

### Stage 1. Understand the investment (business first)
Product and manufacturing chain, upstream and downstream. Business model. Sales mix (intra-state, inter-state, export). Dependence on power, land, labour. Project type (new unit, expansion, diversification, modernisation). Investment size and employment.

### Stage 2. Map the policy universe (all five layers, see Section 1)
- Central sectoral ministry policies, missions and schemes: e.g. PLI schemes, ECMS (Electronics Component Manufacturing Scheme), ISM / Semicon 2.0 (India Semiconductor Mission), Green Hydrogen Mission, Green Steel Taxonomy, Critical Mineral Mission, battery storage viability gap funding
- Regional schemes where the location qualifies (e.g. North East)
- State industrial policy: policy, then GRs, then implementation guidelines, then FAQs and clarifications, then the unit-level eligibility certificate, MoU or incentive agreement
- State sectoral policies: electronics, semiconductor, EV, data centre, green hydrogen, solar, wind, battery storage, textiles, aerospace and others
- State tourism policy: usually separate from industrial policy, with its own definition of a tourism unit and of expansion (e.g. by number of rooms) and its own department
- Interaction rules: top-ups linked to central approval, mutually exclusive schemes, choose-one rules, overall caps
- Gaps: where no policy exists, this triggers Stage 9

### Stage 3. Choose the state
Value of the policy stack. Track record of actual disbursement and pending dues. Ability of the state treasury to pay. Precedents. Land availability. Power cost and reliability. Political and policy stability (the test is whether commitments carry across governments, never party preference). Ruling government, CM office and committees, implementing agency, relevant officials (always date-stamped). Speed of approvals. Existing ecosystem and anchors.

Compare on **effective yield x certainty of payment**, not headline percentage.

### Stage 4. Engineer eligibility and structure the investment
How the product can be positioned to be eligible (thrust, priority, general, ineligible). Value chain choices and value addition thresholds. Unit design: separate units or phases vs one combined project, to fit new unit, expansion and size class tests. Phasing against investment windows and policy transitions. Location within the state. Ownership of assets against "paid for and acquired". Guardrail: every structure must have real commercial substance; check anti-splitting and related-party clauses.

### Stage 5. Value it (ROI)
What is the incentive truly worth: 10%, 20%, 50%, 60% of investment? Bridge from headline to real: eligible investment haircut, intra-state SGST pool, time value, delay and certainty. Express in CFO terms: effective yield, IRR uplift, payback.

### Stage 6. Design and negotiate the tailor-made package
Customised package route for mega or strategic projects. History of such packages and what others got (deal database). Competing state offers. What to ask for: quantum, tenure, shape of payments, land, power, infrastructure, stability clause, payment security, flexibility on conditions. Frame the ask in the state's terms (jobs, SGST generated, anchor effect) and in a form that suits the state's finances. SGST-linked support is close to self-funding for a state; capital subsidy is cash out of its budget.

### Stage 7. Secure eligibility and sanction
Eligible investment definitions (paid for, acquired, capitalised, installed) and grey zones (land, captive power, second-hand machinery, interest during construction, pre-operative costs). Instrument mechanics. Document triangulation: capacity in IEM / Udyam, pollution control board consents, factory licence, power load, CA and engineer certificates must all match. Institutions, portal, timelines.

### Stage 8. Realise and protect the money
Claim cycle, disbursement follow-up. One compliance calendar across every scheme the unit holds, central and state. Continuing conditions and clawback (minimum years, employment, no relocation). Change events (merger, demerger, sale or lease of unit) and transferability. Agreement clauses (stability, audit rights, dispute resolution, state's right to change terms).

### Stage 9. Policy advocacy (parallel track)
For green and new-age sectors where centre or state has no policy. Represent clients before government so that a sectoral policy is brought in that fits the government's larger agenda. Value chain mapping, national-interest case, benchmarks against other states and global regimes, draft policy terms. Preferably positioned as an industry-wide case.

---

## 4. Eligibility lenses (applied in Stage 4 and Stage 7)

1. Instrument hierarchy and version (which policy and guidelines govern; transition; option to choose old or new)
2. Project character (new, expansion, diversification, modernisation, revival; threshold tests; size class MSME / large / mega / ultra-mega)
3. Location (taluka or district category; parks, SEZ, special regions; tourism destination category)
4. Sector and product (thrust, priority, general, negative list; unit-level vs product-level; apportionment)
5. Eligible investment (definitions, window, grey zones)
6. Instruments and ceilings (rate, annual cap, tenure, overall cap)
7. Net SGST mechanics (intra-state only; cash vs ITC; IGST credit set off against SGST; branch transfers; inverted duty refunds; effect of GST rate changes on the SGST pool)
8. Power (thresholds, connected load, captive, open access, renewable banking)
9. Land (eligibility of land cost, allotment, concessions)
10. Document triangulation (IEM, pollution consents, factory licence, power load, certificates)
11. Institutional route (agency, committee, portal, customised package route)
12. Lifecycle and timelines (application window, provisional vs final certificate, commercial production deadline, start of incentive period)
13. Continuing obligations and clawback
14. Change events and transferability
15. Disbursement and cash flow (claim frequency, budget, delay history)
16. Agreement and MoU clauses

---

## 5. Sector overlays

Capacity and expansion mean different things by sector. Fix these at the start of every mandate.

| Sector | Capacity unit | Expansion usually tested on |
|---|---|---|
| Manufacturing | Tonnes or units per year | % increase in installed capacity or gross block |
| Power and new energy | MW, MWh | Added capacity, often a separate project |
| Data centres | MW of IT load, racks | Added MW or new building |
| Tourism | Rooms or keys, seats, built-up area | Number or % of rooms added; new facilities |

**Tourism specifics:** what counts as a tourism unit (star hotels, heritage, resorts, homestays, convention centres, theme parks, wellness, adventure, eco, caravan, cruise); expansion by rooms; star classification and its maintenance as a continuing condition; GST rate on rooms and restaurants decides the SGST pool; electricity at industrial tariff ("industry status"); heritage property leases.

**Matching instrument to project profile:**
- Power-heavy (metals, data centres, electrolysers): power subsidy is the real lever
- Labour-heavy (electronics assembly, textiles): employment and EPF support
- Large intra-state domestic sales: SGST-linked support
- Export-heavy or inter-state sales: SGST pool is small, so capital subsidy matters more

---

## 6. The brain: thinking moves run on every mandate

Never stop at reading the policy. Run every mandate through these moves:

| Lever | Question it forces |
|---|---|
| Instrument fit | Given the project economics, which instrument actually pays? |
| Cross-state transplant | Which state does this better, and can we ask the chosen state to match? |
| Unit design | Separate SPVs or phases vs one mega project; new unit vs expansion |
| Value chain move | Does integrating upstream or downstream put the project into a thrust category or above a threshold? |
| Anchor and ancillary | Can the project bring its suppliers into a park, so it is worth more to the state? |
| Stacking | Which central schemes combine with state top-ups? |
| Timing | Old vs new policy, transition windows, budget cycles |
| Policy silence | Where the policy is silent: interpret favourably with evidence, seek clarification, or take it into the customised package |
| Non-cash value | Land readiness, power infrastructure, approval speed |
| Certainty | Escrow, stability clause, budget priority |
| Advocacy | If no policy fits, what sectoral policy should be proposed? |
| Red team | What would the state committee object to? Where is the clawback risk? |

**Method**
1. Go wide first: 15 to 20 ideas without filtering.
2. Then narrow: rank by rupee value, feasibility and risk. Keep the top 5.
3. Four-chair test on each idea: CFO (will the money come?), state committee (will they approve?), auditor (clawback risk?), lender (will they count it?).
4. Each idea carries a certainty tag and its evidence.

**Plays** (in `plays/`) use these fields: trigger, move, precedent, risk, evidence, certainty, date added. Plays grow from research and from Sid's mandates. Refine them after every mandate.

---

## 7. Research rules

- Legal and regulatory positions rest only on government sources: state industries and tourism department sites, nodal agency sites, gazettes, official GR and guideline PDFs, central ministry sites, court websites. Consultant and practitioner sites are not authority.
- Market evidence (IPO documents, annual reports, credit rating rationales, news) may be used as evidence of practice only, and must be tagged as such.
- Every claim marked verified carries its source link.
- Tag every statement: **fact / interpretation / market view / evolving**.
- Mark every cell in a comparison table as verified or inferred.
- Date-stamp anything that moves: office holders, scheme status, rates, pending dues.
- Where a policy is silent or guidelines conflict, say so. Do not smooth it over.
- On central schemes such as PLI, take the government's stated utilisation position. Do not extrapolate linearly. Most such schemes are back-loaded by design.
- Store decoded policies, not source PDFs. Keep links in `sources.md`; fetch the source when a clause needs checking.

**Best sources for the brain:** CAG audit reports on state incentives; High Court and Supreme Court rulings on incentive disputes; IPO documents (DRHPs) and annual reports; credit rating rationales for disbursement delays; state cabinet decisions; investor summit MoUs; state assembly questions and answers; state budget documents; global regimes (US IRA and CHIPS Act, EU, Vietnam, Malaysia).

---

## 8. Confidentiality

This repository sits on a personal account. No client names, no client-identifiable facts, no engagement documents. Mandate learnings go in anonymised. Public data only in `deals/`, unless anonymised. Before any advocacy work, check firm independence rules where the client is also an audit client.

---

## 9. Routines

| Routine | Trigger | Output |
|---|---|---|
| Mandate run | Sid says "new mandate" | Intake questions in rounds (business first), library check, gap filling, value bridge, ideas, HTML output, then deliberation |
| Monthly refresh | Scheduled | New GRs, amendments, cabinet packages, sunset dates checked; decodes updated; short "what changed" brief |
| Incentive agenda brief | Fortnightly, scheduled | Packages announced, disbursement news, upcoming sectoral policies, central scheme moves, and what each means for Sid's sectors |
| Learning loop | After each mandate | What worked and what got rejected, captured in `learnings/` and used to refine `plays/` |

**Mandate run sequence**
1. Ask intake questions in rounds of 5 to 6, multiple choice where possible, business first.
2. For each candidate state, check the library: is the policy decoded? Any new GR since the last decode?
3. If missing or stale, fetch sources, decode in the standard format, save, log in CHANGELOG.md.
4. Build a simple project cash flow and the value bridge.
5. Run the brain (Section 6).
6. Deliver the output, then deliberate with Sid.

**After every session that changes the library:** update README.md coverage, add a CHANGELOG.md entry, commit with a plain-English message.

---

## 10. Working style with Sid

- Deliberate before building. Play back understanding, offer options, confirm direction. Do not jump to production.
- Build multi-page outputs page by page. Deliver page 1, take sign-off, then continue.
- Business layers first, then financials and geography, then strategy, then tax last.
- Deliver outputs as downloadable HTML files, not published artifacts. Make them visual: decision trees, flow diagrams, wide matrices (items as rows, dimensions as columns).
- Plain language. Decode every abbreviation and technical term inline at first use.
- Advisory voice ("is recommended", "may be considered"). No criticism of existing teams.
- Use dates for regulatory references (e.g. "GR of Sept 2026"). Avoid notification and circular numbers in anything client-facing.
- Short, direct, non-vague. Prefer shorter cuts over completeness.
- No meta-commentary about own corrections inside deliverables.
- When Sid pushes back, accept and move on.
- Sector priority: metals and mining, auto and EV, new energies, power and utilities, then infrastructure, real estate, cement, industrial products, tourism, defence and aerospace as needed.
- States of first focus: Gujarat, Maharashtra, Tamil Nadu, Karnataka, Andhra Pradesh, Telangana (to assess), Odisha, West Bengal, Jharkhand, Chhattisgarh, Madhya Pradesh, Uttar Pradesh, Haryana. Possible additions: Rajasthan, Assam and the North East.

---

## 11. How Sid works with this

**Start of every chat:** Sid says "attach Incentives". Claude attaches sidharthajain17/Incentives, pulls the latest version, reads this rulebook and README.md, then waits for the instruction.

**Instructions are short phrases, typed or dictated:**

| Sid says | Claude does |
|---|---|
| "New mandate: ..." | Intake questions, analysis, mandate report |
| "Decode <state / ministry> <policy>" | Fetch from government site, decode, save, send one-pager |
| "Compare <states> for <sector>" | Wide comparison matrix |
| "What changed this month?" | Summary of new GRs, schemes, packages |
| "Teach me <topic>" | Visual explainer |
| "Add a play: ..." | Record the idea in plays/ |
| "What's in the library?" | Coverage snapshot from README.md |
| "Send me <output> again" | Re-deliver from outputs/ |

**Questions to Sid:** tappable multiple-choice cards, up to 4 at a time, Sid can type or dictate his own answer. For a mandate, 2 to 3 short rounds, business first.

## 12. Output formats (always HTML files, opened in Safari)

| Format | When |
|---|---|
| Policy one-pager | After every decode: what it gives, who qualifies, what it does not say, risks |
| State comparison matrix | States as rows, levers as columns, every cell verified or inferred |
| Mandate report | Page by page with sign-off: summary, eligibility tree, value bridge, ideas, risks |
| Monthly / fortnightly brief | What changed and why it matters for Sid's sectors |
| Explainer | Learning pieces, diagram-heavy |

**Common skeleton for every file:** key takeaway box at the top; visuals before text; certainty tags (fact / interpretation / market view / evolving); source link on every verified point; abbreviations explained inline at first use; date of preparation.

Library outputs are saved in outputs/. Client mandate reports are never saved in the repository.
