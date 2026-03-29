"""
examples/ecommerce_brand.py
----------------------------
Example: E-commerce fashion brand wants to grow revenue by 40% YoY
through digital marketing.

Run:
    python examples/ecommerce_brand.py
"""

import sys
import asyncio
from pathlib import Path

# Allow running from the examples/ subdirectory
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dotenv import load_dotenv
load_dotenv()

from main import run_batch

CHALLENGE = (
    "We are a direct-to-consumer (DTC) fashion e-commerce brand with an average "
    "order value of $85. We currently generate $2M in annual revenue and want to "
    "grow by 40% YoY. Our best-performing channel is Instagram but we have no "
    "Google Ads presence. We have a Shopify store and have not set up GA4 properly. "
    "Please build a comprehensive digital marketing strategy to hit our growth targets."
)

if __name__ == "__main__":
    asyncio.run(run_batch(CHALLENGE))
