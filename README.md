# 📣 Digital Marketing Multi-Agent System

A multi-agent AI system built with **Microsoft AutoGen** that assembles a full
digital marketing team to tackle any marketing challenge, from SEO and email
campaigns to Google Ads, Facebook/Meta Ads, YouTube, social media, and beyond.

---

## 🧠 Architecture Overview

```
User Input
    │
    ▼
┌──────────────────────────────────────────────────────────────┐
│                      Orchestrator                            │
│  (Routes challenge · manages clarification · drives flow)    │
└────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬───────┘
     │      │      │      │      │      │      │      │
     ▼      ▼      ▼      ▼      ▼      ▼      ▼      ▼
  Market  Website Email  Copy-  SEO   YouTube Social LinkedIn
 Research Presence Mktg  writing       Mktg   Media   Mktg
                                        (IG/FB/
                                       TW/Pin/
                                        Quora)
     │         │          │          │
     ▼         ▼          ▼          ▼
   App       Google    Facebook  Google
 Marketing    Ads      Meta Ads Analytics
                          │
                          ▼
                    ┌───────────┐
                    │  Summary  │
                    │   Agent   │
                    └───────────┘
                          │
                          ▼
              Final Markdown Strategy Report
```

---

## 👥 Agents

| Agent | Role |
|-------|------|
| **Orchestrator** | Routes the challenge, manages conversation flow, triggers UserProxy for clarification |
| **UserProxy** | Human bridge — surfaces clarifying questions to the user in interactive mode |
| **MarketResearchAgent** | Audience segmentation, competitive analysis, market sizing |
| **WebsitePresenceAgent** | UX/CRO, landing pages, Core Web Vitals, CMS recommendations |
| **EmailMarketingAgent** | List building, drip sequences, automation, deliverability |
| **CopywritingAgent** | Value propositions, headlines, ad copy, video scripts |
| **SEOAgent** | Keyword strategy, technical SEO, content clusters, link building |
| **YouTubeMarketingAgent** | Video strategy, channel optimisation, YouTube Ads |
| **SocialMediaAgent** | Instagram · Facebook · Twitter/X · Pinterest · Quora |
| **LinkedInMarketingAgent** | B2B content, lead generation, thought leadership |
| **AppMarketingAgent** | ASO, user acquisition, push notifications, retention |
| **GoogleAdWordsAgent** | Search, Display, Shopping, Performance Max, Smart Bidding |
| **FacebookAdsAgent** | Meta Ads, retargeting, Pixel/CAPI, creative strategy |
| **GoogleAnalyticsAgent** | GA4, GTM, UTMs, attribution modelling, Looker Studio |
| **SummaryAgent** | Compiles the final structured Markdown strategy report |

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/digital-marketing-multiagent.git
cd digital-marketing-multiagent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Keys

```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:

```dotenv
OPENAI_API_KEY=your_openai_api_key_here
LLM_MODEL=gpt-4o
```

### 4. Run the System

**Interactive mode** (recommended for first use):

```bash
python main.py
```

**Batch mode** (automated, no user input required):

```bash
python main.py --batch "B2B SaaS startup needs a full digital marketing strategy with a $10k/month budget"
```

**Disable report saving:**

```bash
python main.py --no-save
```

---

## 📁 Project Structure

```
digital-marketing-multiagent/
├── main.py                          # Entry point
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variable template
├── README.md                        # This file
│
├── agents/
│   ├── __init__.py
│   ├── orchestrator.py              # Orchestrator agent
│   ├── user.py                      # UserProxy (human bridge)
│   ├── market_research.py           # Market Research specialist
│   ├── website_presence.py          # Website Presence specialist
│   ├── email_marketing.py           # Email Marketing specialist
│   ├── copywriting.py               # Copywriting specialist
│   ├── seo.py                       # SEO specialist
│   ├── youtube_marketing.py         # YouTube Marketing specialist
│   ├── social_media.py              # Social Media (IG/FB/TW/Pin/Quora)
│   ├── linkedin_marketing.py        # LinkedIn Marketing specialist
│   ├── app_marketing.py             # App Marketing specialist
│   ├── google_adwords.py            # Google Ads specialist
│   ├── facebook_ads.py              # Facebook / Meta Ads specialist
│   ├── google_analytics.py          # Google Analytics specialist
│   └── summary.py                   # Final report compiler
│
├── config/
│   ├── __init__.py
│   ├── agent_config.py              # Shared constants (termination keyword, names)
│   └── llm_config.py                # LLM backend factory (OpenAI / Azure / Ollama)
│
├── utils/
│   ├── __init__.py
│   ├── prompts.py                   # Welcome message & per-agent task templates
│   └── report_generator.py         # Report extraction & Markdown file saving
│
├── examples/
│   ├── ecommerce_brand.py           # DTC fashion brand growth strategy
│   ├── b2b_saas_startup.py          # B2B SaaS customer acquisition strategy
│   └── mobile_app_launch.py         # Wellness app go-to-market strategy
│
├── docs/
│   ├── agent_design.md              # Architecture & agent design notes
│   └── best_practices.md            # Channel-by-channel best practices reference
│
└── reports/                         # Auto-generated strategy reports (git-ignored)
```

---

## 💬 Example Interaction

```
╔══════════════════════════════════════════════════════════════╗
║         📣 Digital Marketing Multi-Agent System              ║
║    Powered by AutoGen  |  Your full-stack marketing team     ║
╚══════════════════════════════════════════════════════════════╝

Hello! I'm your Marketing Orchestrator. Our specialist team is ready.

What digital marketing challenge can we help you with today?
> We're a B2B SaaS company targeting construction firms. We have $10k/month
  and need our first 500 paying customers within 12 months.

[Orchestrator]          → Routing to MarketResearch, SEO, LinkedIn, Google Ads, Email...
[MarketResearchAgent]   → Analysing construction-tech buyer personas and competitive landscape...
[SEOAgent]              → Identifying high-intent keywords and content cluster strategy...
[LinkedInMarketingAgent]→ Building LinkedIn outreach and content plan for construction SMBs...
[GoogleAdWordsAgent]    → Designing Search + Performance Max campaign structure...
[EmailMarketingAgent]   → Creating nurture sequence for free-trial signups...
[CopywritingAgent]      → Drafting value proposition and headline variants...
[GoogleAnalyticsAgent]  → Defining KPI framework, GA4 events, and UTM convention...
[SummaryAgent]          → Compiling final Digital Marketing Strategy Report...

✅  Report saved to: reports/marketing_strategy_20250615_143022.md
```

---

## ⚙️ Configuration

### LLM Backends

Edit `.env` to switch backends:

| Backend | `LLM_BACKEND` value | Required variables |
|---------|--------------------|--------------------|
| OpenAI (default) | `openai` | `OPENAI_API_KEY`, `LLM_MODEL` |
| Azure OpenAI | `azure` | `AZURE_OPENAI_*` variables |
| Ollama (local) | `ollama` | `OLLAMA_BASE_URL`, `LLM_MODEL` |

### Conversation Modes

| Mode | Flag | Description |
|------|------|-------------|
| Interactive | *(none)* | Full back-and-forth with UserProxy for clarification |
| Batch | `--batch "..."` | Fully automated; agents work from the provided challenge string |

---

## 📊 Sample Report Output

The SummaryAgent produces a structured Markdown report including:

- **Executive Summary** — challenge, objectives, overall approach
- **Market Research Insights** — audience segments, competitive landscape
- **Channel Strategy** — tactics, content direction, KPIs, and effort rating per channel
- **Integrated Campaign Roadmap** — 30/60/90-day action plan
- **KPI Dashboard** — channel × primary KPI × target × tool
- **Budget Allocation Guidance** — paid vs organic split
- **Next Steps** — immediate actions and role suggestions

Reports are saved to the `reports/` directory as timestamped Markdown files.

---

## 🤝 Contributing

Pull requests are welcome! See `docs/agent_design.md` for guidance on adding
new specialist agents.

---

## 📄 License

MIT License — see `LICENSE` for details.
