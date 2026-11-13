# Decode template

The fixed format for decoding any policy or scheme in this library, at any of the five layers: central sectoral, regional, state generic, state sectoral, state tourism.

Ten sections, always in this order. Copy this file, fill it in, do not reorder or rename the sections. Where something does not apply, write `not applicable` rather than deleting the heading.

Two parts are marked **state only**: the location or zone test in Section 3, and the customised package route in Section 9. Leave the headings in place for central schemes.

Certainty tags throughout are the rulebook's four: **fact / interpretation / market view / evolving**.

---

## Front matter

Every decode opens with this block, fields in this fixed order. Where something is not known, write `unknown`. Do not guess and do not drop the field. This is what lets comparison matrices be generated from the library rather than hand built.

```yaml
# --- Identity ---
name:                  # Official name
common_name:           # What people actually call it
layer:                 # central sectoral | regional | state generic |
                       # state sectoral | state tourism
state:                 # State name, or null for central
authority:             # Ministry, department or nodal agency
instrument:            # gazette notification | government resolution |
                       # scheme guidelines | policy document | cabinet decision
document_ladder:       # announcement | cabinet | notification | guidelines |
                       # portal live | amended
tier:                  # full | short | basic

# --- The three clocks ---
policy_valid_from:
policy_valid_to:
application_window:    # Deadline to register or apply, including any
                       # trigger such as days from commencement of
                       # commercial production
benefit_tenure:        # How long the benefit runs, and from what date

# --- Money envelope ---
outlay:                # Amount, or "no cap" for open ended entitlement
rationing:             # allocation at approval | budget at payout | both
utilisation:           # Where known, with date

# --- Classification ---
instruments:           # capex | output linked | tax reimbursement |
                       # factor cost | land and infrastructure (one or more)
project_types:         # new unit | expansion | diversification |
                       # modernisation | revival
size_classes:          # MSME | large | mega | ultra mega
sectors:               # Sectors this is relevant to
status:                # live | closing | closed to new applicants |
                       # announced not notified | superseded | lapsed

# --- Provenance ---
sources:               # Primary government URLs, each with date accessed
last_amended:          # Date and what changed
last_reviewed:         # Date this decode was last checked
certainty:             # fact | interpretation | market view | evolving
```

**Depth tiers.** Full is all ten sections, for policies in a live mandate or a core sector. Short is the front matter plus Sections 1, 3, 4 and 9, for policies worth knowing but not yet live. Basic is the front matter alone, so the coverage grid stays complete. A decode can be upgraded later. Never delete front matter when upgrading.

**Relationship to the eligibility lenses.** The sixteen lenses in Section 4 of the rulebook are the checklist. This template is where the answers are written down. Sections 3 to 7 below carry lenses 1 to 16 between them.

---

## Section 1. The fact card

Three blocks. Every fact carries a source link and a tag.

**A. What it is and where it came from.** Official name and the name people use. Which ministry, department or agency issued it. What kind of document it is, because a gazette notification is much harder for a government to walk back than a set of guidelines. Where it sits on the document ladder. Last amendment and what it changed. Whether it replaces an earlier policy, and whether a unit may elect to stay on the old one.

**B. The three clocks.** Kept as three separate fields because they are routinely conflated.

| Clock | What it means |
|---|---|
| Policy validity | The period the policy itself is in force |
| Application window | The deadline to register or apply, often a fixed number of days from commencement of commercial production |
| Benefit tenure | How many years the benefit runs, and from which date it starts |

A policy valid to 2029 is of no use to a unit that missed a registration deadline running 180 days from a date already past.

**C. Where the money comes from and how it runs out.** Central schemes usually have a fixed pot and can close on exhaustion even where a claimant qualifies. State policies usually create open ended entitlement but ration at payout through the annual budget line. Different risks, so two separate fields: the outlay, and the rationing mechanism.

---

## Section 2. Why the scheme exists

**A. The problem being solved.** Who dominates this business globally and why. Where India actually stands. Where in the value chain the gap sits. For a state policy, the same question asked against competing states rather than against the world.

**B. What behaviour is being bought.** Once the gap is clear the design follows, and it shows which part of a project qualifies and which part does not.

**C. Who owns it in government and how strong the backing is.** Which ministry or department runs it, whether it came from a Cabinet decision or a departmental order, and whether it sits inside a larger national or state push. A reasonable guide to whether it gets extended, expanded or quietly allowed to lapse.

**D. What this tells us in practice.** Where wording is unclear, officers read it in line with the purpose, so the purpose helps predict the reading. It also shows which arguments would work in a representation, and whether a project is a natural fit or is being squeezed into something not built for it.

---

## Section 3. Who qualifies

**Entity.** What kind of entity can claim. Whether an Indian company is required and whether a fresh special purpose vehicle is needed. This decides whether a project claims through the existing company or a new one.

**Product or activity.** Usually an annexure list with tariff codes, often split into thrust, priority, general and negative categories. Record whether the list is exhaustive or illustrative, and whether the test applies at unit level or product level. Most disputes start here, where a unit makes something close to a listed product but not exactly it.

**Project character.** New unit, expansion, diversification, modernisation or revival, and the threshold test for each. For tourism, expansion is usually tested on rooms added rather than gross block.

**Investment threshold and what counts as investment.** The minimum spend, then the definition of eligible investment. Whether it covers land, building, plant and machinery, pre operative costs, second hand machinery, interest during construction and captive power. Whether the test is paid for, acquired, capitalised or installed. This definition decides the real money far more than the headline percentage does.

**Location. *State only.*** Taluka or district category, parks, special regions and tourism destination categories, and how the rate changes across them. Record which major industrial areas fall in which category. A site thirty kilometres away can be worth materially more.

**Size class.** The thresholds for MSME, large, mega and ultra mega, and what changes between them. Usually both the rate and the approval route.

**Timing.** Whether spend made before the policy date counts, the transition rule between the old policy and this one, and the deadline for commencement of commercial production.

---

## Section 4. What you get

**A. The instruments.** Classify before describing, because the instrument decides when cash actually arrives.

| Instrument | How it pays | When cash arrives |
|---|---|---|
| Capex linked | Percentage of eligible investment | Early, after commissioning |
| Output linked | Percentage of incremental sales or production | Only once selling at scale |
| Tax reimbursement | Refund of state tax actually paid in cash | Only once paying cash tax |
| Factor cost | Subsidy on power, interest or wages | Through the operating life |
| Land and infrastructure | Concessional land, trunk infrastructure | At the front end, often non cash |

**B. Each instrument on its own line.**

| Instrument | Base | Rate | Annual cap | Tenure | Start trigger | Certainty | Source |
|---|---|---|---|---|---|---|---|

**C. The overall ceiling.** Most state policies cap everything together at a percentage of eligible investment over a period. The individual instruments sit inside that cap, so adding them up gives the wrong answer.

**D. The annual ceiling.** Where there is a per year cap, record it. This is what stretches a ten year entitlement into fifteen years in practice, and it is the single biggest reason headline value and real value diverge.

**E. Power and land specifics.** Connected load thresholds, captive and open access treatment, renewable banking, and whether land cost is eligible or only concessionally allotted.

---

## Section 5. How the money actually reaches the claimant

**The trigger.** What event starts the clock. Usually commencement of commercial production, sometimes capex incurred, sometimes first sale.

**The state GST pool.** Where the benefit is linked to state tax paid, record the mechanics: intra-state sales only, cash versus input tax credit, set off of integrated GST credit against state GST, branch transfers, inverted duty refunds, and the effect of rate changes on the pool. For an export-heavy or inter-state-heavy project this pool can be small enough that the headline benefit never materialises.

**The process.** Registration, provisional and final eligibility certificate, annual claim, documents required, audit or verification.

**Document triangulation.** Capacity as stated in the industrial entrepreneur memorandum or Udyam registration, pollution control board consents, factory licence, sanctioned power load, and chartered accountant and engineer certificates all have to agree. Record where they typically do not.

**Who sanctions.** District level, a state level committee, or Cabinet. The higher the level, the slower the cycle.

**The reality.** Time from claim to cash, pending arrears, and whether the state has honoured past claims. Entitlement and actual payment are recorded as two separate things, with the evidence for each.

---

## Section 6. Conditions and clawback

Minimum period of operation. Employment to be maintained, and for tourism, star classification to be maintained. Restrictions on relocation and closure. What happens on a merger, demerger, slump sale or lease of the unit, and whether the benefit transfers with the business. Default, recovery and interest on recovery. Any stability clause or the state's reserved right to change terms.

The change-of-ownership point carries the most weight, because it decides whether an incentive survives a transaction.

---

## Section 7. Tax interaction

Scope note. The rulebook keeps customs and trade schemes, accounting treatment and general tax advice outside this library. This section covers only what changes the value or the eligibility of the incentive itself.

**GST on the incentive.** Whether it is a government subsidy sitting outside the value of supply, or consideration for something supplied to the government. Where the position is unclear, say so and tag it.

**State GST pool.** Cross reference to Section 5 rather than repeating it.

**Stacking across the five layers.** Whether this benefit can be claimed alongside a central scheme, a regional scheme or another state benefit. Top-ups linked to central approval, mutually exclusive schemes, choose-one rules and overall caps. Usually restricted and usually buried in a proviso.

**Flag and refer.** Where customs, foreign trade policy, special economic zone status, bonded manufacturing or accounting treatment would change the answer, note it in one line and refer it out. Do not analyse it here.

---

## Section 8. What the policy does not say

Where wording is unclear and why. Rulings, departmental practice and litigation. Where practice on the ground differs from the text. Where the policy is silent, and whether the opening is to interpret favourably with evidence, seek a clarification, or take it into the customised package. What is still moving and should be rechecked before relying on it.

---

## Section 9. The commercial read

What the entitlement is actually worth once the haircuts are applied, using the value bridge method rather than repeating it here. State the assumptions. Express it in CFO terms: effective yield on investment, and certainty of payment alongside it, because headline percentage on its own is misleading.

Which project profiles this suits. Power-heavy, labour-heavy, large intra-state domestic sales, export-heavy. What the policy does not cover.

**The customised package route. *State only.*** Whether the policy allows a bespoke package for mega or strategic projects, which committee approves it, and what is known about past packages. Where this route exists, the published policy is the floor and not the ceiling.

---

## Section 10. What we do with this

The questions to ask at intake to test fit against this policy. What has to be verified before relying on it. What to watch over the next few months, and whether it belongs in the watch list. Any candidate plays this decode suggests, written in the play fields and added to `plays/`.
