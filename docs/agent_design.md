# Agent Design Notes

## Architecture Overview

The Digital Marketing Multi-Agent System uses **Microsoft AutoGen's `SelectorGroupChat`** team pattern. A central Orchestrator agent analyses the user's marketing challenge and dynamically selects which specialist agents should speak next, driving the conversation toward a comprehensive strategy.

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
                                                │
     ┌─────────┬──────────┬──────────┬──────────┘
     ▼         ▼          ▼          ▼
   App       Google    Facebook  Google
 Marketing    Ads      Meta Ads Analytics
     │         │          │          │
     └─────────┴──────────┴──────────┘
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

## Agent Roster

| Agent | File | Responsibility |
|-------|------|----------------|
| Orchestrator | `agents/orchestrator.py` | Routes queries, manages flow, triggers UserProxy for clarification |
| UserProxy | `agents/user.py` | Human bridge for interactive clarification |
| MarketResearchAgent | `agents/market_research.py` | Audience segmentation, competitive analysis, market sizing |
| WebsitePresenceAgent | `agents/website_presence.py` | UX/CRO, landing pages, Core Web Vitals |
| EmailMarketingAgent | `agents/email_marketing.py` | List building, automation, deliverability |
| CopywritingAgent | `agents/copywriting.py` | Messaging frameworks, headlines, ad copy, scripts |
| SEOAgent | `agents/seo.py` | Keyword strategy, technical SEO, content clusters |
| YouTubeMarketingAgent | `agents/youtube_marketing.py` | Video strategy, channel optimisation, YouTube Ads |
| SocialMediaAgent | `agents/social_media.py` | Instagram, Facebook, Twitter/X, Pinterest, Quora |
| LinkedInMarketingAgent | `agents/linkedin_marketing.py` | B2B content, lead gen, thought leadership |
| AppMarketingAgent | `agents/app_marketing.py` | ASO, UA, push notifications, retention |
| GoogleAdWordsAgent | `agents/google_adwords.py` | Search, Display, Shopping, PMax, Smart Bidding |
| FacebookAdsAgent | `agents/facebook_ads.py` | Meta Ads, retargeting, Pixel/CAPI, creative |
| GoogleAnalyticsAgent | `agents/google_analytics.py` | GA4, GTM, UTMs, attribution, dashboards |
| SummaryAgent | `agents/summary.py` | Final structured Markdown strategy report |

---

## SelectorGroupChat vs GroupChat

This system uses **`SelectorGroupChat`** (team pattern) rather than a plain `GroupChat`. Key differences:

- A **selector LLM** dynamically chooses which agent speaks next based on the conversation context.
- Prevents round-robin chatter; only relevant agents are activated for a given challenge.
- The Orchestrator's system prompt guides the selector via clear agent descriptions.
- Termination is handled by `TextMentionTermination` watching for `MARKETING_STRATEGY_COMPLETE`.

---

## Adding a New Specialist Agent

1. Create `agents/your_agent.py` following the pattern of any existing agent file.
2. Define a `create_your_agent()` factory function that returns an `AssistantAgent`.
3. Write a focused `system_message` describing the agent's domain and expected output format.
4. Import and call the factory in `main.py` inside `build_team()`.
5. Add the agent to the Orchestrator's system prompt "Available specialist agents" list.
6. Add a display name to `config/agent_config.py` → `AGENT_DISPLAY_NAMES`.

---

## Conversation Modes

| Mode | How to run | Description |
|------|-----------|-------------|
| Interactive | `python main.py` | Full back-and-forth; UserProxy bridges human input |
| Batch | `python main.py --batch "..."` | Fully automated; no human input required |
| Example scripts | `python examples/<name>.py` | Pre-defined challenges for demo / testing |

---

## Termination Flow

1. All specialist agents contribute their section.
2. Orchestrator instructs `SummaryAgent` to compile the report.
3. `SummaryAgent` appends `MARKETING_STRATEGY_COMPLETE` to its message.
4. `TextMentionTermination` detects the keyword and halts the team.
5. `extract_report_from_chat()` locates and saves the report.
