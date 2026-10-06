import json, urllib.request, time
UA={"User-Agent":"jeff-test ge-flipper profitability research (github.com/jeffreyrack/jeff-test)"}
def get(p):
    return json.load(urllib.request.urlopen(urllib.request.Request("https://prices.runescape.wiki/api/v1/osrs/"+p,headers=UA),timeout=30))
m={i['id']:i for i in get("mapping")}; lat=get("latest")["data"]; h1=get("1h")["data"]
json.dump({"m":m,"lat":lat,"h1":h1},open("snap.json","w"))
now=time.time(); tax=lambda p:min(int(p*0.02),5_000_000)
rows=[]
for k,v in lat.items():
    i=int(k); it=m.get(i); hv=h1.get(k)
    if not it or not hv or not v.get("high") or not v.get("low"): continue
    if now-v["highTime"]>3600 or now-v["lowTime"]>3600: continue
    hi,lo=v["high"],v["low"]; margin=hi-tax(hi)-lo
    vol=min(hv.get("highPriceVolume") or 0, hv.get("lowPriceVolume") or 0)
    lim=it.get("limit") or 0
    if margin<=0 or vol<1 or lim<1: continue
    # realistic qty per 4h window: min(limit, 10% of 4h matched volume)
    q=min(lim, int(0.10*vol*4))
    if q<1: continue
    rows.append((margin*q, it['name'], lo, hi, margin, q, lim, vol, lo*q))
rows.sort(reverse=True)
print("items w/ fresh, positive after-tax spread & volume:",len(rows))
print("bond price gp:", lat.get("13190"))
print(f"{'item':32}{'buy':>11}{'sell':>11}{'mgn':>8}{'qty':>7}{'cap gp':>14}{'profit/4h':>12}")
for r in rows[:25]: print(f"{r[1][:31]:32}{r[2]:>11,}{r[3]:>11,}{r[4]:>8,}{r[5]:>7}{r[8]:>14,}{r[0]:>12,}")
for bank in [1e6,10e6,100e6,1e9]:
    cash=bank; tot=0; n=0
    for r in sorted(rows,key=lambda r:-(r[4]/r[2])):  # greedy by ROI
        cap=min(r[8], bank*0.25, cash)
        if cap<r[2]: continue
        q=int(cap//r[2]); tot+=q*r[4]; cash-=q*r[2]; n+=1
        if cash<1e4: break
    print(f"bankroll {bank:>14,.0f}: theoretical snapshot profit/4h window {tot:>14,.0f} gp across {n} items (assumes every order fills at quoted price)")
