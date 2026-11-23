# Changelog

## 23 Nov 2026 (evening) — Maharashtra added; family cards reworked

- **West Bengal family cards reworked at Sid's request.** Each family now shows its founder, current head, the next generation and what each person runs, a background, a milestone timeline, a parent-to-child family tree with spouses, and marriage clues (daughters' married surnames from promoter filings). An at-a-glance table opens the Families tab. 39 Kolkata groups are covered, including six new ones (Beekay, KIC, Bengal Energy, Rungta Sons, Cosmic CRF, Supershakti). The Cosmic CRF promoter is flagged as unrelated to the Aditya Birla Group.
- **Maharashtra added:** 58 companies (38 listed, 11 of them adjacent; 20 unlisted), 46 promoter groups and 45 family links, including 11 marriage links.
  - The Jindal daughters' married surnames are verified from JSW Steel's promoter-group list.
  - Kirloskar, Lloyds and Kalyani details are corrected against filings.
  - Vedanta and its two demerged companies are carried over to Delhi, where their filings point for decisions.
- **Takeaways now sit inside each state's panel.** For states with many links, the family-links view shows grouped cards instead of the network diagram.
- **Per-state Excel built by `outputs/data/metals-mining-hq/make_xlsx.py`:** `metals-mining-hq-maharashtra.xlsx`.
- **New evidence:** `evidence/maharashtra-disbursement.md` records SRJ Peety, Jalna: ₹278 crore of Industrial Promotion Subsidy received against ₹545 crore invested (CARE, Nov 2025).
- **Network:** the request to add press sites was rejected by the environment service, so Sid is adding them manually. Press-based points remain tagged "reported".

## 23 Nov 2026 (later) — Head-office map: West Bengal first

- **Method changed at Sid's direction.** Companies are now placed by **decision office** (corporate or head office), not by plant. The list starts from every BSE/NSE listed company in metals and mining, then adds unlisted companies, with a revenue floor of ₹500 crore. Every promoter group is mapped: family members by generation, links between families, splits and disputes, and each group's chain from mine to finished product, by state.
- **New output:** `outputs/metals-mining-hq-map.html`, with a clickable India map on the left and the state panel on the right (Companies, Families, Family links, Value chain), and `outputs/metals-mining-hq-west-bengal.xlsx`. State boundaries follow the official map of India.
- **West Bengal done:** 45 companies (26 listed, 19 unlisted), 33 promoter groups and 15 family links.
  - Listed companies are checked against screener.in and BSE annual reports.
  - Unlisted companies are checked against India Ratings, CRISIL, CARE and Acuité releases; six remain "reported".
  - No marriage links across families could be sourced from filings.
- **Data kept for later states:** `outputs/data/metals-mining-hq/` holds the source JSON, the map paths and the build script.
- **New network environment:** "Incentives research" lets sessions reach BSE, Screener, the rating agencies, the company registry (MCA) and the Ministry of Steel site. NSE blocks automated access; ICRA could not be reached.
- **Version 1 (`metals-mining-market-map-2026`) is superseded** by this head-office map. It is kept for its plant-site layer.

## 23 Nov 2026 — Metals and mining market map, version 1

- **New library output: `outputs/metals-mining-market-map-2026.html` and `.xlsx`.** It maps 62 companies (23 Tier A, 39 Tier B) and 165 plant and mine site clusters across 20 states and union territories. Coverage runs from mining (coal, lignite, iron ore, manganese, bauxite, mineral sands) through primary metals (steel, aluminium, copper, zinc), specialty, stainless and ferro-alloys, rare earths and critical minerals, to downstream products (pipes, forgings, castings, wire, coated steel).
- **Design agreed with Sid:** tiers set by revenue (Tier A above ₹10,000 crore; Tier B ₹1,000 to 10,000 crore); every ownership type covered (private Indian, central and state public sector, MNC and joint venture, unlisted); all metals and mining states; delivered as an HTML map plus an Excel file.
- **Each company has three locations:** registered office, decision office and plant sites. Announced expansions are logged as market view, so they can later be linked to the state policy each would fall under.
- **Certainty:** every row is inferred, compiled from public disclosures up to mid-2026, and is to be checked against FY26 annual reports. Restructurings are tagged evolving: the Vedanta demerger, the Jindal Steel renaming, the Vizag Steel revival and the Thoothukudi copper closure. Mid-sized Tier B units are deliberately under-counted.
- The Excel file carries blank coverage-planning columns. These are for Sid's local copy only; no client or engagement data enters the repository.

## 13 Nov 2026 (later) — Gujarat decode verified against the Government Resolutions

- **Primary documents obtained and committed.** Sid downloaded the policy document and the two Government Resolutions of 8 September 2026 and supplied them directly. They are held at `states/gujarat/source-documents/`. The Large, Mega and Ultra Mega scheme Resolution and the taluka classification Resolution have both been read in full; the 44-page policy document is held but not yet read.
- **Rulebook change recorded.** The rulebook says to store decoded policies and keep only links, fetching the source when a clause needs checking. Gujarat shows that this does not hold: the Industries and Mines Department's own Government Resolutions page still lists 2015-era entries, the Investor Facilitation Portal does not carry the 2026 policy, and both government sites block automated access. **Source documents are now stored in the repository wherever the government host is unreliable.**
- **Every slab verified.** The inferred rate tables carried in the first draft proved correct in all seven tiers. They are now marked fact.
- **Siting analysis completed from the official Annexure-A.** Every established industrial destination in Gujarat is Category B on the lower band — Dahej (Vagra), Ankleshwar, Jhagadia, Sanand, Mundra, Anjar, Gandhidham, Morbi, Halol, Hazira (Chorasi), Vapi, Savli, Padra and all four major cities. **Only Dholera and Becharaji are Category A.** The Mandal-Becharaji Special Investment Region straddles the boundary, so plot selection within one region changes the band.
- **New findings of substance:** the thrust sub-sector list is indicative, not exhaustive, with a residual clause letting the Industries Commissioner's committee add sectors and HSN code as the tiebreaker on disputes; cement, metals, wires and cables and electrolysers are all inside thrust sectors; captive power consumption earns no power tariff subsidy while renewable open access does; modernisation, renovation, rehabilitation and rationalisation are expressly ineligible; Gujarat's own sectoral schemes are mutually exclusive with this one while central schemes stack up to eligible investment; recovery on breach is as an arrear of land revenue with 18% interest from first availment; the EPF test requires employees with no prior Universal Account Number; the budget line is Demand No. 49, Major head 2852, Minor head 800, Sub head 36.
- **Three live deadlines identified:** registration by 8 December 2026 for units already in production; approximately 8 March 2027 to elect the previous scheme, final and irrevocable; 4 October 2027 as the backstop for commencing production under the previous scheme.
- Five candidate plays drafted in the decode, up from three.

## 13 Nov 2026 — Gujarat added as the first state

- **Gujarat decoded as the first state in the library.** Three files created: `states/gujarat/industrial-policy-2026.md` (full-tier decode of the Viksit Gujarat Industrial Policy 2026), `states/gujarat/profile.md` (institutions, people, payment record, land and power) and `states/gujarat/sources.md` (source register with the sourcing position stated openly).
- **The policy decoded is new.** The Viksit Gujarat Industrial Policy 2026 was announced on 15 June 2026 and is operative from 1 June 2026 to 31 May 2031. It replaces the Gujarat Industrial Policy 2020 and the Aatmanirbhar Gujarat Schemes 2022. The money rules sit in three Government Resolutions of the Industries and Mines Department: the Large, Mega and Ultra Mega scheme and the taluka classification, both of 8 September 2026, and the MSME scheme of 25 September 2026.
- **Sourcing position recorded honestly.** The Industries Commissionerate site blocks automated access and still lists the 2020 policy; the Investor Facilitation Portal does not carry the 2026 policy at all. Two government sources were reached and are recorded: a Press Information Bureau release, and **iNDEXTb (indextb.com), the Gujarat government's Industrial Extension Bureau, which hosts all three Government Resolutions.** iNDEXTb is recorded as the route for verification.
- **Three findings verified against government sources:** the policy identifies 21 sectors in total, being 16 thrust and 5 selected thrust; the taluka classification splits 268 talukas into Category A (130, higher slab) and Category B (138); and the local employment condition is 85% of the overall workforce and 60% of managerial and supervisory staff.
- **Principal commercial finding — siting.** Category A is the less industrially developed set and carries the higher slab, with the result that almost every established industrial destination in Gujarat sits in Category B on the lower band: Dahej, Ankleshwar, Jhagadia, Sanand, Mundra, Anjar, Gandhidham, Morbi and the four major cities. Dholera is the one major destination on the top band. The differential is worth 5 to 10 percentage points of eligible fixed capital investment.
- **Second commercial finding — the annual ceiling.** Each tier carries both a percentage and an absolute annual cap, with no carry-forward of unused entitlement. On an Ultra Mega project, the absolute cap begins to bind above roughly ₹35,700 crore of eligible investment, reducing a 40% headline entitlement to an effective 30%.
- **Open item carried forward.** The incentive rate tables remain unverified and are marked inferred cell by cell. Two reproductions of the Government Resolution agree on ceilings and annual caps but diverge on component sub-caps. To be closed from the iNDEXTb copy before any client use.
- Library outputs added: `outputs/gujarat-vgip-2026-one-pager.html` and `outputs/gujarat-profile-and-siting.html`.

## 13 Nov 2026
- Framework folder completed. Added the outward format (output-templates.md: policy one-pager, state comparison matrix, value bridge sheet, nine-page mandate report, brief, explainer), the instrument library (five instrument families, mechanics only, no rates so it does not go stale), the value bridge method (six-step bridge from headline entitlement to effective yield on total project cost), intake questions (five rounds, business first), state selection criteria (compared on effective yield against certainty of payment, never a single composite score) and idea levers (fourteen moves plus the four-chair test).
- Rulebook layout updated to list output-templates.md alongside decode-template.md, and to label the two as the inward and outward formats.
- Preparatory work complete. The library is ready for its first decodes.

- Decode template (framework/decode-template.md) agreed section by section with Sid and saved. YAML front matter plus ten fixed sections, three depth tiers (full, short, basic), the location test and the customised package route marked state only, and a mapping back to the sixteen eligibility lenses. Section 7 narrowed to GST on the incentive, the state GST pool and stacking, with customs, foreign trade policy and accounting treatment reduced to a flag-and-refer line, in line with the rulebook's out-of-scope list. Open for Sid's review.
- Rulebook (CLAUDE.md) version 1: scope, five-layer incentive universe, nine stages, eligibility lenses, sector overlays, brain, research rules, routines, working style, output formats
- Folder skeleton created with a README in each folder
- Index (README.md) created
