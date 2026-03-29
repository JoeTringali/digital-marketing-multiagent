"""
config/agent_config.py
----------------------
Agent behaviour settings and shared constants.
"""

# ── Termination ────────────────────────────────────────────────────────────────
# The SummaryAgent appends this keyword to its final message so the
# SelectorGroupChat knows the task is complete.
TERMINATION_KEYWORD = "MARKETING_STRATEGY_COMPLETE"

# ── Conversation limits ────────────────────────────────────────────────────────
# Maximum number of consecutive auto-replies before a human turn is forced
# (applies to UserProxyAgent in interactive mode).
MAX_CONSECUTIVE_AUTO_REPLY = 20

# ── Agent display names (used in report headers) ──────────────────────────────
AGENT_DISPLAY_NAMES = {
    "Orchestrator":           "🎯 Orchestrator",
    "MarketResearchAgent":    "🔍 Market Research",
    "WebsitePresenceAgent":   "🌐 Website Presence",
    "EmailMarketingAgent":    "📧 Email Marketing",
    "CopywritingAgent":       "✍️  Copywriting",
    "SEOAgent":               "🔎 SEO",
    "YouTubeMarketingAgent":  "▶️  YouTube Marketing",
    "SocialMediaAgent":       "📱 Social Media",
    "LinkedInMarketingAgent": "💼 LinkedIn Marketing",
    "AppMarketingAgent":      "📲 App Marketing",
    "GoogleAdWordsAgent":     "🔵 Google Ads",
    "FacebookAdsAgent":       "🟦 Facebook / Meta Ads",
    "GoogleAnalyticsAgent":   "📊 Google Analytics",
    "SummaryAgent":           "📋 Summary",
    "UserProxy":              "👤 User",
}
