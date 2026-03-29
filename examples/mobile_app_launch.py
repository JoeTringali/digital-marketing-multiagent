"""
examples/mobile_app_launch.py
------------------------------
Example: A wellness app is preparing to launch on iOS and Android and
needs a go-to-market digital marketing strategy.

Run:
    python examples/mobile_app_launch.py
"""

import sys
import asyncio
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dotenv import load_dotenv
load_dotenv()

from main import run_batch

CHALLENGE = (
    "We are launching a meditation and sleep wellness app on iOS and Android in "
    "45 days. Our target audience is adults aged 25–44 experiencing work-related "
    "stress. We have a freemium model with a $9.99/month premium tier. Our launch "
    "budget is $50,000. We need a full go-to-market strategy covering ASO, social "
    "media, YouTube, influencer marketing, paid user acquisition (Meta and Google "
    "UAC), and a measurement framework to track LTV and D30 retention."
)

if __name__ == "__main__":
    asyncio.run(run_batch(CHALLENGE))
