import json
S=json.load(open("snap.json")); m={int(k):v for k,v in S["m"].items()}; h1=S["h1"]
tax=lambda p:min(int(p*0.02),5_000_000)
tot=0; n=0; rows=[]
for k,v in h1.items():
    a,b=v.get("avgHighPrice"),v.get("avgLowPrice"); hv,lv=v.get("highPriceVolume",0),v.get("lowPriceVolume",0)
    if not a or not b or min(hv,lv)<10: continue
    mg=a-tax(a)-b
    if mg<=0: continue
    lim=(m.get(int(k)) or {}).get("limit") or 0
    q=min(lim/4, 0.10*min(hv,lv))   # per hour: 10% of matched volume, buy limit spread over 4h
    rows.append((mg*q, m.get(int(k),{}).get("name"), mg/b, min(hv,lv), b*q))
rows.sort(reverse=True)
liquid=sum(1 for k,v in h1.items() if v.get("avgHighPrice") and v.get("avgLowPrice") and min(v.get("highPriceVolume",0),v.get("lowPriceVolume",0))>=10)
print(f"items with >=10 trades/hr each side: {liquid}; with positive after-tax avg spread: {len(rows)}")
print("upper-bound gp/hour if one flipper took 10%% of volume on ALL of them at the average spread: %.2fM; capital tied up ~%.0fM"%(sum(r[0] for r in rows)/1e6, sum(r[4] for r in rows)/1e6))
print("top 10 by gp/hr:"); [print(f"  {r[1][:30]:30} spread {100*r[2]:5.1f}%  vol/hr {r[3]:>6}  gp/hr {r[0]:>10,.0f}") for r in rows[:10]]
