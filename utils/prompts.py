"""
utils/prompts.py
----------------
Shared prompt templates and UI text used across the system.
"""

WELCOME_MESSAGE = """
📣  Digital Marketing Multi-Agent System
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Powered by AutoGen  |  Your full-stack marketing team, ready to help.

Specialists on the team:
  🔍  Market Research          ✍️  Copywriting
  🌐  Website Presence         🔎  SEO
  📧  Email Marketing          ▶️  YouTube Marketing
  📱  Social Media             💼  LinkedIn Marketing
  📲  App Marketing            🔵  Google Ads
  🟦  Facebook / Meta Ads      📊  Google Analytics

Type  'quit'  or  'exit'  at any time to end the session.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ── Per-agent task instruction templates ──────────────────────────────────────

MARKET_RESEARCH_TASK = (
    "MarketResearchAgent, analyse the target audience and competitive landscape "
    "for the following challenge: {challenge}. Identify the top 3 audience segments "
    "and the key differentiators the brand should exploit."
)

WEBSITE_PRESENCE_TASK = (
    "WebsitePresenceAgent, review the website strategy needed to support this challenge: "
    "{challenge}. Recommend landing page structure, CRO improvements, and any technical "
    "issues to address."
)

EMAIL_MARKETING_TASK = (
    "EmailMarketingAgent, design an email marketing approach for: {challenge}. "
    "Include a list-building tactic, a welcome/nurture sequence outline, and the top "
    "3 segmentation rules to apply."
)

COPYWRITING_TASK = (
    "CopywritingAgent, create the core messaging framework for: {challenge}. "
    "Provide a value proposition, three headline options, and a CTA for the primary "
    "conversion action."
)

SEO_TASK = (
    "SEOAgent, develop an SEO strategy for: {challenge}. Identify the top keyword "
    "clusters, flag any technical SEO priorities, and recommend a content plan for "
    "the first 90 days."
)

YOUTUBE_TASK = (
    "YouTubeMarketingAgent, propose a YouTube content and ads strategy for: {challenge}. "
    "Include video content pillars, thumbnail/title guidance, and a paid amplification "
    "recommendation if appropriate."
)

SOCIAL_MEDIA_TASK = (
    "SocialMediaAgent, recommend a social media strategy across the relevant platforms "
    "for: {challenge}. Include content types, posting cadence, and cross-platform "
    "repurposing opportunities."
)

LINKEDIN_TASK = (
    "LinkedInMarketingAgent, develop a LinkedIn strategy for: {challenge}. "
    "Include content pillars, post-format examples, and lead-generation tactics."
)

APP_MARKETING_TASK = (
    "AppMarketingAgent, outline an app marketing plan for: {challenge}. "
    "Cover ASO, user-acquisition channels, and a retention strategy."
)

GOOGLE_ADS_TASK = (
    "GoogleAdWordsAgent, design a Google Ads strategy for: {challenge}. "
    "Recommend campaign types, a keyword approach, Smart Bidding strategy, "
    "and budget allocation guidance."
)

FACEBOOK_ADS_TASK = (
    "FacebookAdsAgent, create a Meta Ads strategy for: {challenge}. "
    "Cover campaign objective, audience strategy (cold / warm / hot), "
    "creative format recommendations, and tracking setup."
)

ANALYTICS_TASK = (
    "GoogleAnalyticsAgent, define the measurement framework for: {challenge}. "
    "Specify the KPIs, conversion events to track, UTM convention, and a "
    "Looker Studio dashboard structure."
)

SUMMARY_TASK = (
    "SummaryAgent, compile all contributions into the final Digital Marketing "
    "Strategy Report for: {challenge}. Follow the full report template in your "
    "instructions and end with the termination keyword."
)
