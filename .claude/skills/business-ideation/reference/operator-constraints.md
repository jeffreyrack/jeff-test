# Operator Constraints

Every agent in this system must judge ideas against **who actually runs the business**.
Ideas that ignore these constraints are worthless, no matter how good they sound.

## The goal

An AI agent runs a business that **pays for its own tokens**.

| Parameter | Default | Notes |
|---|---|---|
| Break-even target | **$300 / month net revenue** | Roughly what an AI operator running a few sessions a day costs in tokens. |
| Stretch target | $1,000 / month | Funds a bigger operator budget and more experiments. |
| Upfront capital | **$0 ideal**, $100 hard cap | Anything above $100 is an automatic reject. |
| Time to first sale | ≤ 30 days is good, ≤ 90 days acceptable | > 90 days needs a strong justification. |

## The operator: an AI agent (e.g. Claude Code sessions)

**Can do on its own:**
- Write and run code; build websites, web apps, browser extensions, CLIs, APIs, bots.
- Deploy to free tiers: GitHub Pages, Cloudflare Pages/Workers, Vercel/Netlify hobby, Supabase/Neon free DBs.
- Do web research: search, read pages, read public forums.
- Generate text, and images through paid image APIs at small per-image cost (assume ~$0.01–$0.08 per image).
- Write SEO content, docs, emails, social posts, and product listings.
- Run scheduled jobs (cron, GitHub Actions, scheduled sessions).
- Answer customer emails and support tickets through an API-connected inbox.
- Analyze data and produce reports, datasets, and PDFs.

**Cannot do. A human must handle these, so count them as human intervention:**
- Pass KYC / identity checks: open bank, Stripe, PayPal, Gumroad, Lemon Squeezy, Etsy, Amazon KDP, or app store developer accounts.
- Sign contracts, hold liability, or file taxes.
- Pass phone verification or CAPTCHAs on new accounts on most platforms.
- Handle physical goods: receive, inspect, pack, ship, or return them.
- Make phone calls or attend video meetings.
- Create social media accounts where bots or automated accounts are banned. Reddit, X, LinkedIn, Facebook groups, and Discord servers all penalise or ban undisclosed automation and self-promotion.

## The human sponsor

- Does **one-time setup** (≈ 2–4 hours): creates a payment account (prefer a merchant-of-record such as Lemon Squeezy, Gumroad, or Paddle so sales tax/VAT is handled), buys a domain (~$12), and creates the platform accounts that need ID.
- Ongoing budget: **≤ 1 hour/week** ideally, 3 hours/week maximum. Anything recurring above that fails the "autonomous" test.
- Is the legal "runner" of the business and carries all of its legal risk.

## Reality checks every agent must apply

1. **"Why wouldn't the customer just ask ChatGPT?"** If an end user can get the same value by prompting a free chatbot, the idea needs a strong moat: distribution, data, workflow integration, curation, trust, or convenience.
2. **Distribution beats product.** A new site with zero domain authority gets roughly no organic search traffic for 3–6 months. Marketplaces (Chrome Web Store, Etsy, Gumroad Discover, VS Code marketplace, Shopify App Store, Notion template galleries, etc.) give built-in traffic but come with rules.
3. **Platform rules about AI and automation.** Examples: KDP requires AI disclosure and limits uploads; Etsy restricts AI-generated items under "made by"; Reddit bans spam; Google demotes scaled, low-value AI content. Check the current rules.
4. **AI-generated works may not be copyrightable** (US Copyright Office position). Others can freely copy pure AI output.
5. **Spam is not a strategy.** Cold email and mass DMs carry legal risk (CAN-SPAM, GDPR) and reputational risk, and get accounts banned.
