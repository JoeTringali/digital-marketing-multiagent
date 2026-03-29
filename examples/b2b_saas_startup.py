"""
examples/b2b_saas_startup.py
-----------------------------
Example: Early-stage B2B SaaS startup needs a full-funnel digital marketing
strategy to reach its first 500 paying customers.

Run:
    python examples/b2b_saas_startup.py
"""

import sys
import asyncio
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dotenv import load_dotenv
load_dotenv()

from main import run_batch

CHALLENGE = (
    "We are a B2B SaaS startup that has just launched a project-management tool "
    "targeting small construction companies (5–50 employees) in the United States. "
    "We have a $10,000/month marketing budget, a WordPress website, and no current "
    "paid campaigns. Our goal is to reach 500 paying customers within 12 months at "
    "a target CAC below $200. Please create a full digital marketing strategy covering "
    "SEO, LinkedIn, Google Ads, email marketing, and content/copywriting."
)

if __name__ == "__main__":
    asyncio.run(run_batch(CHALLENGE))
