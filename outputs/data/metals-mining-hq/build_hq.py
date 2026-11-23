"""Build the head-office-anchored metals and mining map.
Usage: build_hq.py <scratch dir> <out html>
Reads india_paths.json and, per mapped state, <code>_listed*.json, <code>_unlisted*.json, <code>_families.json."""
import json, sys, os, html, datetime
S, OUT = sys.argv[1], sys.argv[2]
paths = json.load(open(os.path.join(S, "india_paths.json")))

def load(name):
    p = os.path.join(S, name)
    return json.load(open(p)) if os.path.exists(p) else None

STATES = {"West Bengal": "wb", "Maharashtra": "mh"}  # extended as states are added
QUEUE = ["Maharashtra", "Delhi", "Chhattisgarh", "Odisha", "Telangana", "Gujarat", "Jharkhand", "Karnataka", "Rajasthan", "Punjab", "Haryana", "Uttar Pradesh", "Tamil Nadu", "Andhra Pradesh", "Madhya Pradesh"]
data = {}
for st, code in STATES.items():
    if not os.path.exists(os.path.join(S, f"{code}_listed_v.json")): continue
    L = load(f"{code}_listed_v.json") or load(f"{code}_listed.json") or []
    U = load(f"{code}_unlisted_v.json") or load(f"{code}_unlisted.json") or []
    F = load(f"{code}_families.json")
    if F is None:
        F = {"groups": [], "links": []}
        for part in ("A", "B", "C", "D"):
            x = load(f"{code}_families_{part}.json")
            if x:
                F["groups"] += x.get("groups", []); F["links"] += x.get("links", [])
    for part in ("A", "B", "C"):
        for e in (load(f"{code}_fam_enrich_{part}.json") or []):
            i = e.get("index")
            if isinstance(i, int) and i < len(F["groups"]) and i < 100:
                F["groups"][i].update({k: v for k, v in e.items() if v not in (None, "", [])})
            elif isinstance(i, int):
                F["groups"].append(e)
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
        g.setdefault("companies", []); g.setdefault("people", [])
        for p_ in g.get("people", []):
            gv = str(p_.get("generation"))
            p_["gen_label"] = GEN.get(gv, {"1":"1st generation","2":"2nd generation","3":"3rd generation","4":"4th generation"}.get(gv, "Next generation / other"))
        head = (g.get("head") or {}).get("name") if isinstance(g.get("head"), dict) else None
        sur = short(g.get("family") or "")
        g["label"] = (sur + (" · " + head if head else "")) or g.get("group", "")
        for c in g.get("companies", []):
            c["state_short"] = re.split(r"[(;,]", c.get("state") or "")[0].strip()
    checked, links = [], []
    for l in F.get("links", []):
        def lab(x):
            for g in F.get("groups", []):
                if x in (g.get("group"), g.get("family")) or short(x) in (short(g.get("group") or ""), short(g.get("family") or "")):
                    return g["label"]
            return short(x)
        l["from_short"], l["to_short"] = lab(l["from_group"]), lab(l["to_group"])
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
    data[st] = {"companies": cos, "groups": F.get("groups", []), "links": F.get("links", []), "checked": F.get("checked", []), "takeaways": open(os.path.join(S, f"{code}_takeaways.html")).read() if os.path.exists(os.path.join(S, f"{code}_takeaways.html")) else ""}


page = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "hq_template.html")).read()
page = (page.replace("/*PATHS*/", json.dumps(paths))
            .replace("/*DATA*/", json.dumps(data, ensure_ascii=False))
            .replace("/*QUEUE*/", json.dumps([q for q in QUEUE if q not in data]))
            .replace("{{DATE}}", "23 Nov 2026").replace("<!--TAKEAWAYS-->", ""))
open(OUT, "w").write(page)
print("ok", {k: (len(v["companies"]), len(v["groups"]), len(v["links"])) for k, v in data.items()})
