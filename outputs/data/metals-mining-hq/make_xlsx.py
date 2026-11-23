"""Build the per-state Excel: make_xlsx.py <code> <state name> <out.xlsx>"""
import json, sys, os, glob
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
code, state, out = sys.argv[1:4]
D = os.path.dirname(os.path.abspath(__file__)) + "/"
ld = lambda f: json.load(open(D + f)) if os.path.exists(D + f) else None
L = [x for x in ld(f"{code}_listed_v.json") or [] if "name" in x]
U = [x for x in ld(f"{code}_unlisted_v.json") or [] if "name" in x]
F = ld(f"{code}_families.json") or {"groups": [], "links": []}
if not F["groups"]:
    for p in "ABCD":
        z = ld(f"{code}_families_{p}.json")
        if z: F["groups"] += z["groups"]; F["links"] += z["links"]
for p in "ABC":
    for e in ld(f"{code}_fam_enrich_{p}.json") or []:
        i = e.get("index")
        if isinstance(i, int) and i < 100 and i < len(F["groups"]): F["groups"][i].update({k: v for k, v in e.items() if v})
        else: F["groups"].append(e)
pl = lambda v: "; ".join(f"{p.get('site')} ({p.get('state')})" for p in v) if isinstance(v, list) else (v or "")
nm = lambda x: x.get("name", "") if isinstance(x, dict) else (x or "")
st = lambda v: v if isinstance(v, (int, float)) or v is None else (v if isinstance(v, str) else json.dumps(v, ensure_ascii=False))
wb = Workbook(); H = Font(bold=True, color="FFFFFF"); HF = PatternFill("solid", fgColor="1F3A5F")
def sh(name, head, rows, w):
    ws = wb.create_sheet(name); ws.append(head)
    for r in rows: ws.append([st(v) for v in r])
    for c in ws[1]: c.font = H; c.fill = HF
    for i, x in enumerate(w, 1): ws.column_dimensions[get_column_letter(i)].width = x
    for row in ws.iter_rows():
        for c in row: c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "B2"; ws.auto_filter.ref = ws.dimensions
ws = wb.active; ws.title = "Read me"
for l in [f"Metals and mining head-office map: {state}. Placed by decision office (corporate / head office); registered office shown separately. Revenue floor ₹500 crore. Listed (BSE/NSE) and unlisted.",
          "Certainty: verified = read from screener/BSE filing, rating rationale or company document; reported = press or search summary; inferred = deduced.",
          "Coverage columns are for your local copy only."]: ws.append([l])
ws.column_dimensions["A"].width = 150
rows = [[c["name"], k, c.get("exchange"), c.get("category") or "core", c.get("segment"), c.get("revenue_inr_cr"), c.get("revenue_year"), c.get("decision_office"), c.get("reg_office"), pl(c.get("plants")), c.get("promoter_group"),
         "; ".join(f"{p.get('name')} ({p.get('role')})" for p in c.get("promoters") or []), c.get("certainty"), c.get("notes"), "; ".join(c.get("sources") or []), "", "", ""] for k, arr in (("Listed", L), ("Unlisted", U)) for c in arr]
rows.sort(key=lambda r: -(r[5] or 0))
sh("Companies", ["Company", "Listed/Unlisted", "Exchange", "Core/adjacent", "Segment", "Revenue ₹ cr", "Revenue year / basis", "Decision office", "Registered office", "Plants", "Promoter group", "Promoters", "Certainty", "Notes", "Sources", "Coverage status (your use)", "Services in place (your use)", "Relationship lead (your use)"], rows, [34, 10, 8, 10, 30, 11, 22, 30, 30, 50, 26, 40, 10, 40, 40, 16, 16, 16])
G = [g for g in F["groups"]]
sh("Family profiles", ["Family", "Group", "Founder", "Founded", "Head today", "Head's role", "Next generation (who runs what)", "Background", "Milestones", "Marriage clues", "Certainty"],
   [[g.get("display_name") or g.get("family"), g.get("group"), nm(g.get("founder")), (g.get("founder") or {}).get("year_founded") if isinstance(g.get("founder"), dict) else "", nm(g.get("head")), (g.get("head") or {}).get("role") if isinstance(g.get("head"), dict) else "",
     "\n".join(f"{n.get('name')}: {n.get('runs') or ''}" for n in g.get("next_gen") or []), g.get("background") or g.get("control_summary"),
     "\n".join(f"{m.get('year')}: {m.get('event')}" for m in g.get("milestones") or []), "\n".join(f"{c.get('person')}: {c.get('detail')} [{c.get('certainty')}]" for c in g.get("marriage_clues") or []), g.get("certainty")] for g in G],
   [40, 26, 24, 10, 26, 30, 50, 70, 50, 50, 10])
sh("Family tree", ["Family", "Person", "Generation", "Parent", "Spouse", "Role", "Certainty"], [[g.get("display_name") or g.get("family"), p.get("name"), p.get("generation"), p.get("parent"), p.get("spouse"), p.get("role"), p.get("certainty")] for g in G for p in g.get("people") or []], [40, 28, 10, 28, 24, 50, 12])
sh("Group companies", ["Family", "Company", "Listed", "Stage in chain", "State", "Note"], [[g.get("family"), c.get("name"), c.get("listed"), c.get("chain_stage"), c.get("state"), c.get("ownership_note")] for g in G for c in g.get("companies") or []], [34, 34, 8, 40, 22, 36])
sh("Family links", ["From", "To", "Type", "Description", "Source", "Certainty"], [[l.get("from_group"), l.get("to_group"), l.get("type"), l.get("description"), l.get("source"), l.get("certainty")] for l in F["links"]], [30, 30, 14, 70, 40, 10])
wb.save(out); print("xlsx", out, len(rows), len(G))
