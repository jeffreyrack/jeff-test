# User-supplied ideas (round 3)

## U5 — Vending machines, AI-managed, physical labour outsourced

- **Persona:** User-supplied
- **One-liner:** Own a small number of snack, drink or combo vending machines (or a micro-market) in good locations. The AI operator runs analytics, pricing, stock planning, ordering and support. Restocking and servicing are **outsourced**, because sponsor time is valued at $300/h (see `../PARAMS.md`).
- **Demand test:** (assumed; the demand-validator should design the real one) Secure a signed location agreement before buying any machine, then start with one used machine and set kill criteria.
- **Customer:** Employees and visitors at the host location (offices, warehouses, gyms, apartment complexes, auto shops, etc.). The host is the "B2B customer" who must agree to the placement.
- **Problem / desire:** The host wants a free amenity, sometimes with a commission. Users want convenient snacks and drinks.
- **Offering:** Card- and phone-pay vending with remote stock monitoring (e.g. Cantaloupe/Nayax-type card readers and telemetry).
- **Price & revenue model:** Product sales at a markup (cost of goods ~40–50% of price), minus the location commission (0–20%), card fees (~5–6%) and telemetry (~$15–30 per machine per month). All figures are assumed and must be verified.
- **Physical items required?** **Yes.** Machines, stock, installation, restocking, repairs and cash/coin handling if any. All recurring labour is outsourced: a paid restocker, TaskRabbit-style labour, or a revenue-share agreement with an existing route operator.

### Upfront capital
| Item | Cost (assumed, verify) |
|---|---|
| Used machine with card reader | $1,500–3,000 each |
| New machine | $4,000–8,000 each |
| Initial stock | $200–400 per machine |
| Delivery, installation, permits/licence, insurance | $200–800 |
| **Total for 1–3 machines** | **~$2,000–10,000** (above the run's <$1k preference; must justify via payback) |

### Monthly running costs (excluding operator tokens)
- Cost of goods
- Location commission
- Card fees
- Telemetry
- Outsourced restocking (e.g. $25–40/h or per visit, weekly per machine)
- Insurance
- Repairs and breakdowns
- Vehicle/fuel, if borne by the restocker

### Customer acquisition plan
Location acquisition is the whole game.
- The AI researches local businesses with 30+ staff on-site, drafts genuine proposals, and handles low-volume compliant outreach.
- Location brokers or locators can be paid ($200–500 per location is common, assumed).
- Alternatively, partner with an existing local route operator.

### Path to first sale
Sign a location, buy and install a machine, and the first sales come on day 1 of placement. (assumed) 30–60 days to the first placement.

### Who does what
- **AI operator:**
  - location research and proposals;
  - telemetry analytics;
  - demand forecasting;
  - planogram and pricing;
  - stock ordering for delivery;
  - restocker scheduling;
  - refund handling via QR code;
  - bookkeeping.
- **Human sponsor:** signing the location contract, buying the machine, any in-person location visit, and business registration and sales-tax permit. Each hour is valued at $300.
- **Contractors:** delivery and installation, weekly restocking, repairs.

### Moat — why not just ask ChatGPT?
- The location contract and the physical asset can't be cloned by an AI agent.
- Competition comes from local vending operators and micro-market companies that offer hosts the same thing.

### Biggest risks (ideator view)
- **Location quality varies enormously;** a bad location may gross under $100/month.
- **Outsourced restocking cost may consume most of the margin at 1–3 machines.**
- **Anthropic's 2025 "Project Vend"** found that an AI shopkeeper lost money through discounting and errors. Guardrails are needed.
- **Equipment risk:** theft, vandalism and breakdowns. Used machines resell at a loss.
