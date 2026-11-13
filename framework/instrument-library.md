# Instrument library

The standard list of incentive instruments used across Indian central and state policies. Every decode classifies what it finds into these, so that policies written in different language can still be compared.

**No rates here.** Rates, caps and tenures live in the decode for each policy, with a source link. This file is mechanics only, so it does not go stale.

---

## How to read this

Four things decide whether an instrument is worth anything to a project.

1. **The base.** What the percentage is applied to. Almost never total project cost.
2. **When the cash arrives.** Front loaded, through the operating life, or only once the unit is selling at scale.
3. **The binding constraint.** Usually an annual cap or a pool that is too small, not the headline rate.
4. **Whether the state can pay.** Entitlement and disbursement are different things.

---

## A. Capital side

Paid against the investment itself. Cash arrives early, usually after commissioning.

| Instrument | Base | How it works | Where it fails |
|---|---|---|---|
| Capital subsidy | Eligible fixed capital investment | A percentage of qualifying spend, paid in instalments over a few years | The gap between project cost and eligible investment. Land, pre-operative costs and interest during construction are often excluded |
| Interest subsidy | Interest paid on term loan for the project | Reimbursement of part of the interest, usually capped per year and limited to a rupee ceiling | Falls away if the project is equity funded, or if the loan is refinanced outside the eligible lender list |
| Stamp duty and registration | Duty on land purchase, lease and loan documents | Exemption at source or refund afterwards | Timing. Exemption needs the eligibility certificate before registration, which is often not ready |
| Land at concessional rate | Allotment price in a government industrial estate | Land allotted below market, sometimes on long lease | Not cash. Value depends on whether the estate is actually where the project wants to be |
| Infrastructure support | Trunk infrastructure to the site | Road, water line, power evacuation, common facilities built by the state | Rarely written as an entitlement. Usually negotiated, and usually slow |

---

## B. Operating side

Paid out of what the unit does after it starts. This is where most of the money sits in Indian state policies, and where most of it is lost.

| Instrument | Base | How it works | Where it fails |
|---|---|---|---|
| State GST reimbursement | Net state GST paid in cash on intra-state sales | The state refunds part of the state goods and services tax the unit actually pays in cash, usually capped at a percentage of eligible investment over a fixed period | The single biggest failure point. An export-heavy or inter-state-heavy project generates almost no state GST in cash, so a large entitlement never gets absorbed |
| Interest free loan against state GST | Same base as above | An older design. The state lends back the tax collected, repayable after a long holiday | Shows as a liability on the balance sheet. Lenders and auditors treat it differently from a subsidy |
| Electricity duty exemption | Duty component of the power bill | Exemption for a fixed period from commencement | Only the duty, not the tariff. Small unless the unit is very power heavy |
| Power tariff subsidy | Units of electricity consumed | A fixed amount per unit, capped per year | Usually time limited and often the first thing a state trims when finances tighten |
| Employment support | Employer contribution to provident fund, or a fixed amount per worker | Reimbursement for a period, often higher for women and for local hires | Requires employment to be sustained. Becomes a clawback trigger if headcount falls |
| Training and skilling | Cost of training per worker | Reimbursement against certified training | Small, and administratively heavy relative to value |
| Quality, patent and research support | Certification, testing and filing cost | Reimbursement against invoices | Small, but useful evidence of thrust-sector fit |
| Freight or market support | Movement cost, or participation cost | State specific and uncommon | Usually too small to change a decision |

---

## C. Central instruments

Different design logic. Central schemes are usually capped pots, rationed at approval.

| Instrument | Base | How it works | Where it fails |
|---|---|---|---|
| Production linked incentive | Incremental sales of covered goods over a base year | A percentage of incremental sales, paid annually against achievement of both investment and sales thresholds | Both thresholds have to be met. Missing the investment threshold in an early year can cost the whole year's claim |
| Capital expenditure support | Eligible project capex | A percentage of project cost, disbursed against milestones, used in capital-heavy missions | Milestone definitions. Disbursement follows verified progress, not spend |
| Viability gap funding | The gap between project cost and what the project can bear | Grant to make an otherwise unviable project bankable, usually bid out | Competitive. The bid itself decides the amount |
| Interest subvention | Interest on project debt | Reduction in effective interest rate for a period | Lender eligibility and documentation |
| Research and pilot grants | Approved project cost | Milestone-linked grant for development work | Narrow eligibility, heavy reporting |

---

## D. Non-cash value

Easy to leave out of a comparison and often decisive.

Speed of approvals and single-window performance. Readiness of land, meaning whether it is actually possible to start. Power reliability and the cost of not having it. Quality of the nodal agency and whether claims get processed. Existing supplier ecosystem. Whether the state will put commitments into a written agreement with a stability clause.

---

## E. Classification rule for decodes

Every benefit found in a policy is tagged with one of five instrument families in the decode front matter.

`capex` | `output linked` | `tax reimbursement` | `factor cost` | `land and infrastructure`

If something does not fit, record it under the closest family and note the mismatch in Section 8 of the decode rather than inventing a new family.
