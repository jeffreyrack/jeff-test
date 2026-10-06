# User-supplied ideas (round 2)

## U4 — AI-matched job board: aggregated listings + "upload your resume, see exact matches"; later charge employers to post

- **Persona:** User-supplied
- **One-liner:** A job board that collects listings automatically and lets a job seeker upload a resume. It ranks jobs that match the candidate's experience exactly, and explains each match. It starts free. Once traffic exists, it charges employers to post jobs directly.
- **Demand test:** (assumed; the demand-validator should design the real one)
- **Customer:**
  - **Side 1, job seekers:** (assumed) tech or professional workers who are actively searching and tired of keyword search and irrelevant results.
  - **Side 2, employers and recruiters:** they pay to post once the audience exists.
- **Problem / desire:** "Job boards show me hundreds of roles that don't fit. I want only the ones I'm actually qualified for."
- **Offering:**
  - A web app with resume upload (PDF), an extracted skills and experience profile, and a ranked match list with a "why you match" explanation for each role.
  - Daily email alerts.
  - Later, a paid employer posting flow.
- **Price & revenue model:**
  - As proposed: free for job seekers, with employer job posts later (typically $99–$399 per post on niche boards).
  - **Alternative to evaluate:** charge job seekers from day 1, e.g. $9–19/month for premium alerts and match explanations. The goal is for the business to cover its own token costs, and "unprofitable at first" works against that.
  - Affiliate revenue (resume services, courses) is a possible bridge.
- **Physical items required?** No

### Job-data sourcing (critical; evaluators must check the legality)
- **Avoid:** LinkedIn and Indeed. Their terms of service forbid scraping, and LinkedIn has litigated over it.
- **Likely cleaner:** public applicant-tracking-system job-board endpoints that companies publish for exactly this purpose (Greenhouse, Lever, Ashby, Workable, SmartRecruiters), company careers pages, the USAJobs API, and remote-job RSS feeds.
- **Check:** the terms for each source, and whether reposting full job descriptions or linking out is required.

### Upfront capital
| Item | Cost |
|---|---|
| Domain | $12 |
| Hosting/DB (free tiers) | $0 |
| **Total** | **~$12** |

### Monthly running costs (excluding operator tokens)
Per-resume parsing and embedding are cheap. Re-matching every user against the full job index daily scales with users × jobs; use embeddings plus a vector DB, with LLM explanations only for the top matches. Email sending will exceed free tiers at scale.

### Customer acquisition plan
(assumed)
- Programmatic SEO pages: "<role> jobs in <city>" and "<skill> jobs". These take 3–6 months and compete with Indeed, LinkedIn, Google for Jobs and Hiring Cafe.
- Show-and-tell posts in job-seeker communities by the human.
- Niche positioning may be needed, e.g. one profession or one skill.

### Path to first sale
Users first, then employers. The user expects it to be unprofitable at first. (assumed) Employer revenue only arrives after meaningful seeker traffic, which means months.

### Who does what
- **AI operator:** ingestion pipelines, dedupe and expiry, matching, the site, emails, SEO pages, support.
- **Human sponsor:** payment KYC, community posts, and employer sales conversations if employers want a human.

### Moat — why not just ask ChatGPT?
- ChatGPT can't search live job inventory well.
- Existing AI job-search tools already do resume matching: Hiring Cafe (free, pulls company ATS feeds directly), Jobright.ai, Simplify, Teal, LoopCV and others. Their exact features need verification.
- The moat would need to come from niche focus, data quality and freshness, or match accuracy.

### Biggest risks (ideator view)
- Two-sided marketplace chicken-and-egg: employers won't pay without seekers.
- Free, well-funded AI job-search incumbents.
- Legal: scraping terms of service; resumes are personal data (GDPR/CCPA); EU AI Act treats recruitment AI as high-risk; NYC Local Law 144 on automated employment decision tools; job-posting discrimination rules.
