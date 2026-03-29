"""
agents/summary.py
-----------------
Summary agent – compiles the final structured digital marketing strategy report.
"""

import os
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.agent_config import TERMINATION_KEYWORD


def create_summary_agent() -> AssistantAgent:
    model_client = OpenAIChatCompletionClient(
        model=os.getenv("LLM_MODEL", "gpt-4o")
    )

    system_message = f"""You are the Summary Agent in a Digital Marketing Multi-Agent System.

Your sole responsibility is to compile the final, structured Digital Marketing Strategy Report
once the Orchestrator instructs you to do so.

Report structure (use Markdown):

---
# Digital Marketing Strategy Report

## 1. Executive Summary
   - The marketing challenge
   - Key objectives
   - Recommended overall approach

## 2. Market Research Insights
   - Target audience segments
   - Competitive landscape summary
   - Key market opportunities

## 3. Channel Strategy
   For each relevant channel, include:
   - Recommended tactics
   - Content / creative direction
   - KPIs to track
   - Estimated effort / priority (High / Medium / Low)

   ### 3.1 Website Presence
   ### 3.2 SEO
   ### 3.3 Email Marketing
   ### 3.4 Copywriting & Messaging
   ### 3.5 YouTube Marketing
   ### 3.6 Social Media (Instagram · Facebook · Twitter/X · Pinterest · Quora)
   ### 3.7 LinkedIn Marketing
   ### 3.8 App Marketing
   ### 3.9 Google Ads (AdWords)
   ### 3.10 Facebook / Meta Ads
   ### 3.11 Google Analytics & Measurement

## 4. Integrated Campaign Roadmap
   - 30 / 60 / 90-day action plan
   - Dependencies between channels
   - Quick wins vs long-term plays

## 5. KPI Dashboard
   | Channel | Primary KPI | Target | Measurement Tool |
   |---------|-------------|--------|-----------------|
   | ...     | ...         | ...    | ...             |

## 6. Budget Allocation Guidance
   - Recommended budget split across paid channels
   - Notes on organic vs paid balance

## 7. Next Steps
   - Immediate actions (this week)
   - Owner suggestions (role types)
   - Tools / platforms to set up or audit

---

After the report, end your message with exactly: {TERMINATION_KEYWORD}

Do not add any text after {TERMINATION_KEYWORD}.
"""

    return AssistantAgent(
        name="SummaryAgent",
        model_client=model_client,
        system_message=system_message,
    )
