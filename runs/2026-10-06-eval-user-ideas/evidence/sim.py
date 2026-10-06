import json, urllib.request, time, os, statistics as st
UA={"User-Agent":"jeff-test ge-flipper profitability research (github.com/jeffreyrack/jeff-test)"}
S=json.load(open("snap.json")); m={int(k):v for k,v in S["m"].items()}; h1=S["h1"]
tax=lambda p:min(int(p*0.02),5_000_000)
# universe: top 60 items by hourly gp traded (both sides), price >= 100gp, chosen by liquidity only (not margin)
liq=[]
for k,v in h1.items():
    a,b=v.get("avgHighPrice"),v.get("avgLowPrice")
    if not a or not b or b<100: continue
    gp=min(v.get("highPriceVolume",0),v.get("lowPriceVolume",0))*b
    if int(k) in m and m[int(k)].get("limit"): liq.append((gp,int(k)))
liq.sort(reverse=True); ids=[i for _,i in liq[:60]]
ts={}
os.makedirs("ts",exist_ok=True)
for i in ids:
    f=f"ts/{i}.json"
    if not os.path.exists(f):
        d=json.load(urllib.request.urlopen(urllib.request.Request(f"https://prices.runescape.wiki/api/v1/osrs/timeseries?timestep=1h&id={i}",headers=UA),timeout=30))["data"]
        json.dump(d,open(f,"w")); time.sleep(0.3)
    ts[i]={r["timestamp"]:r for r in json.load(open(f))}
T=sorted(set.intersection(*[set(v) for v in ts.values()]))
print("items",len(ids),"common hours",len(T), "days %.1f"%(len(T)/24))
# spread stats
spr=[]
for i in ids:
    xs=[(r["avgHighPrice"]-tax(r["avgHighPrice"])-r["avgLowPrice"])/r["avgLowPrice"] for r in ts[i].values() if r["avgHighPrice"] and r["avgLowPrice"]]
    if xs: spr.append((st.median(xs), sum(x>0 for x in xs)/len(xs), m[i]["name"]))
spr.sort(reverse=True)
print("median after-tax hourly spread across universe: %.2f%%"%(100*st.median(s[0] for s in spr)), "| items with median>0:",sum(s[0]>0 for s in spr))
def sim(bank, share=0.10, maxhold=12, cap_frac=0.2):
    cash=bank; inv={}; bought={}  # inv[i]=[qty,cost_each,ask,age]
    flips=0; pnl_items={}
    for t in range(3,len(T)-1):
        now,nxt=T[t],T[t+1]
        # sells fill in next hour
        for i,(q,c,ask,age) in list(inv.items()):
            r=ts[i][nxt]
            if age>=maxhold:
                px=r["avgLowPrice"] or c
                if px: 
                    sq=q; cash+=sq*(px-tax(px)); pnl_items[m[i]["name"]]=pnl_items.get(m[i]["name"],0)+sq*(px-tax(px)-c); del inv[i]; continue
            if r["avgHighPrice"] and r["avgHighPrice"]>=ask:
                sq=min(q,int(share*(r["highPriceVolume"] or 0)))
                if sq>0:
                    cash+=sq*(ask-tax(ask)); pnl_items[m[i]["name"]]=pnl_items.get(m[i]["name"],0)+sq*(ask-tax(ask)-c); flips+=1
                    q-=sq
            if q>0: inv[i]=[q,c,ask,age+1]
            else: inv.pop(i,None)
        # signals: require positive after-tax spread in each of last 3 hours
        cands=[]
        for i in ids:
            if i in inv: continue
            rs=[ts[i][T[t-k]] for k in range(3)]
            if any(not r["avgHighPrice"] or not r["avgLowPrice"] for r in rs): continue
            if not all(r["avgHighPrice"]-tax(r["avgHighPrice"])-r["avgLowPrice"]>0 for r in rs): continue
            r=rs[0]; bid=r["avgLowPrice"]; ask=r["avgHighPrice"]; mg=ask-tax(ask)-bid
            lim=m[i]["limit"]; used=sum(q for (tt,q) in bought.get(i,[]) if now-tt<4*3600)
            cands.append((mg/bid,i,bid,ask,max(0,lim-used)))
        cands.sort(reverse=True)
        for roi,i,bid,ask,room in cands:
            alloc=min(cash, bank*cap_frac); q=min(room,int(alloc//bid))
            if q<1: continue
            r=ts[i][nxt]
            if r["avgLowPrice"] and r["avgLowPrice"]<=bid:
                fq=min(q,int(share*(r["lowPriceVolume"] or 0)))
                if fq>0:
                    cash-=fq*bid; inv[i]=[fq,bid,ask,0]; bought.setdefault(i,[]).append((nxt,fq))
    # liquidate at last avgLow
    for i,(q,c,ask,age) in inv.items():
        px=ts[i][T[-1]]["avgLowPrice"] or c; cash+=q*(px-tax(px))
    return cash-bank, flips, pnl_items
days=len(T)/24
for bank in [10e6,100e6,1e9]:
  for share in [0.05,0.10]:
    p,f,pi=sim(bank,share)
    print(f"bank {bank/1e6:>6.0f}M share {share:.2f}: profit {p/1e6:8.2f}M over {days:.1f}d = {p/days/1e6:6.2f}M/day ({100*p/bank/days:5.2f}%/day), sell fills {f}")
p,f,pi=sim(100e6,0.10)
print("top/bottom items @100M:", sorted(pi.items(),key=lambda x:-x[1])[:5], sorted(pi.items(),key=lambda x:x[1])[:5])
