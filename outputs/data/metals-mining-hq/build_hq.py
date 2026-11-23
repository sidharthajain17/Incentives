"""Build the head-office-anchored metals and mining map.
Usage: build_hq.py <scratch dir> <out html>
Reads india_paths.json and, per mapped state, <code>_listed*.json, <code>_unlisted*.json, <code>_families.json."""
import json, sys, os, html, datetime
S, OUT = sys.argv[1], sys.argv[2]
paths = json.load(open(os.path.join(S, "india_paths.json")))

def load(name):
    p = os.path.join(S, name)
    return json.load(open(p)) if os.path.exists(p) else None

STATES = {"West Bengal": "wb"}  # extended as states are signed off
QUEUE = ["Maharashtra", "Delhi", "Chhattisgarh", "Odisha", "Telangana", "Gujarat", "Jharkhand", "Karnataka", "Rajasthan", "Punjab", "Haryana", "Uttar Pradesh", "Tamil Nadu", "Andhra Pradesh", "Madhya Pradesh"]
data = {}
for st, code in STATES.items():
    L = load(f"{code}_listed_v.json") or load(f"{code}_listed.json") or []
    U = load(f"{code}_unlisted_v.json") or load(f"{code}_unlisted.json") or []
    F = load(f"{code}_families.json") or {"groups": [], "links": []}
    def clean(rows, kind):
        out = []
        for r in rows:
            if "name" not in r: continue
            r["kind"] = kind; out.append(r)
        return out
    cos = clean(L, "Listed") + clean(U, "Unlisted")
    import re
    short = lambda x: re.sub(r"\s*\(.*?\)", "", x or "").strip()
    GEN = {"1st":"1st generation","2nd":"2nd generation","3rd":"3rd generation","1st/2nd":"1st generation"}
    for g in F.get("groups", []):
        for p_ in g.get("people", []):
            p_["generation"] = GEN.get(str(p_.get("generation")), "Next generation / other")
        for c in g.get("companies", []):
            c["state_short"] = re.split(r"[(;,]", c.get("state") or "")[0].strip()
    checked, links = [], []
    for l in F.get("links", []):
        l["from_short"], l["to_short"] = short(l["from_group"]), short(l["to_group"])
        if (l.get("description") or "").lower().startswith("no link"):
            checked.append(l)
        else:
            links.append(l)
    F["links"], F["checked"] = links, checked
    cos.sort(key=lambda r: -(r.get("revenue_inr_cr") or 0))
    CITIES = ["Kolkata","Howrah","Bhubaneswar","Rajgangpur","Kalunga","East Midnapore","Durgapur","Asansol"]
    STN = ["West Bengal","Odisha","Jharkhand","Andhra Pradesh","Gujarat","Maharashtra","Delhi"]
    def short_office(x, dec=False):
        t = x if isinstance(x, str) else ""
        if not t or t.lower().startswith(("not confirmed","none","unresolved","unclear")):
            return "To confirm"
        city = next((c for c in CITIES if c in t), None); st_ = next((z for z in STN if z in t), None)
        if city == "Kalunga": city = "Kalunga, Sundergarh"
        if city == "Rajgangpur": city = "Rajgangpur, Sundergarh"
        return ", ".join([v for v in (city, st_) if v]) or t.split(" (")[0]
    for c in cos:
        c["dec_short"] = short_office(c.get("decision_office"), True)
        if (c.get("decision_office") or "").startswith(("West Bengal (Kolkata inferred","Kolkata / Howrah")): c["dec_short"] = "Kolkata, West Bengal"
        c["reg_short"] = short_office(c.get("reg_office"))
        c["name_short"] = re.sub(r"\s*\((?!India\)).*$", "", c["name"])
    STOP = {"ltd","limited","pvt","private","and","the","industries","india","steel","steels","power","metaliks","group"}
    tok = lambda x: [w for w in re.sub(r"[^a-z ]", " ", (x or "").lower()).split() if len(w) > 2 and w not in STOP]
    def gsize(g):
        if "government" in (g.get("family") or "").lower(): return -1
        keys = {tuple(tok(c["name"])[:1]) for c in g.get("companies", []) if tok(c["name"])}
        return sum((c.get("revenue_inr_cr") or 0) for c in cos if tuple(tok(c["name"])[:1]) in keys)
    F["groups"].sort(key=lambda g: -gsize(g))
    data[st] = {"companies": cos, "groups": F.get("groups", []), "links": F.get("links", []), "checked": F.get("checked", [])}

TK = """<div class="box"><b>Key takeaways: West Bengal (Kolkata)</b><ul>
<li><b>45 metals and mining companies above ₹500 crore make their decisions from Kolkata:</b> 26 listed and 19 unlisted. Almost all of them have both registered and decision office in Kolkata. Three listed companies are registered in Odisha but run from Kolkata (Electrosteel Castings, IFGL Refractories, VISA Chrome). <span class="tag verified">verified</span></li>
<li><b>Unlisted companies outweigh listed private ones.</b> Unlisted companies together report about ₹1.03 lakh crore of revenue, against about ₹74,000 crore for the listed private companies (excluding Coal India). The largest private group in Kolkata, Rashmi (about ₹31,700 crore, FY25), is unlisted, as are Rungta Mines and Rungta Sons. A listed-only view would miss the biggest relationships. <span class="tag verified">verified</span> (rating reports)</li>
<li><b>Kolkata decides, but most plants are elsewhere.</b> Of 113 plant locations, 49 are in West Bengal. The rest sit mainly in Odisha, Jharkhand and Andhra Pradesh. A Kolkata relationship therefore drives work across the eastern mineral belt. <span class="tag">interpretation</span></li>
<li><b>Ownership is family-held, often split between branches.</b> Manaksia became four listed companies, one for each family line (2013). The two branches of the Jhawar family behind Usha Martin have been in dispute since 2017. The Beriwala family has two separate steel brands (Shyam Steel and SRMB). The Bansal families behind Skipper and BMW Industries likely share a common ancestor. Jindal (India) belongs to the B.C. Jindal branch, B.C. Jindal being O.P. Jindal's brother. <span class="tag verified">verified</span> / <span class="tag inferred">inferred</span> as tagged</li>
<li><b>The same surname does not mean the same family.</b> Five separate Agarwal steel groups were identified. MSP Steel and Manaksia each have a different "Suresh Kumar Agrawal". It is worth mapping each company to the right branch before any outreach. <span class="tag verified">verified</span></li>
<li><b>No marriage links between these families could be sourced.</b> Company filings list relatives within a family, but not marriages across families. Those links typically come from the community and press; they can be added as you confirm them. <span class="tag">evolving</span></li>
</ul></div>"""
page = open(os.path.join(os.path.dirname(__file__), "hq_template.html")).read()
page = (page.replace("/*PATHS*/", json.dumps(paths))
            .replace("/*DATA*/", json.dumps(data, ensure_ascii=False))
            .replace("/*QUEUE*/", json.dumps(QUEUE))
            .replace("{{DATE}}", "23 Nov 2026").replace("<!--TAKEAWAYS-->", TK))
open(OUT, "w").write(page)
print("ok", {k: (len(v["companies"]), len(v["groups"]), len(v["links"])) for k, v in data.items()})
