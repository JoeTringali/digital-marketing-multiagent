"""
utils/report_generator.py
--------------------------
Extracts the final strategy report from the conversation history and
saves it as a timestamped Markdown file in the reports/ directory.
"""

import os
import re
from datetime import datetime
from pathlib import Path
from typing import Optional

from config.agent_config import TERMINATION_KEYWORD


REPORTS_DIR = Path("reports")


def extract_report_from_chat(history: list) -> Optional[str]:
    """
    Walk the message history (newest-first) and return the content of the
    last SummaryAgent message that contains the termination keyword.

    Returns None if no suitable message is found.
    """
    for message in reversed(history):
        source = getattr(message, "source", None)
        content = getattr(message, "content", None)

        if source == "SummaryAgent" and isinstance(content, str):
            if TERMINATION_KEYWORD in content:
                # Strip the termination keyword and any trailing whitespace
                report = content.replace(TERMINATION_KEYWORD, "").rstrip()
                return report

    # Fallback: return the last SummaryAgent message even without the keyword
    for message in reversed(history):
        source = getattr(message, "source", None)
        content = getattr(message, "content", None)
        if source == "SummaryAgent" and isinstance(content, str) and len(content) > 100:
            return content

    return None


def save_report(content: str, filename: Optional[str] = None) -> Path:
    """
    Save *content* to a Markdown file inside the reports/ directory.

    Returns the Path of the saved file.
    """
    REPORTS_DIR.mkdir(exist_ok=True)

    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"marketing_strategy_{timestamp}.md"

    file_path = REPORTS_DIR / filename
    file_path.write_text(content, encoding="utf-8")
    return file_path


def list_reports() -> list[Path]:
    """Return all Markdown reports in the reports/ directory, newest first."""
    if not REPORTS_DIR.exists():
        return []
    return sorted(REPORTS_DIR.glob("*.md"), reverse=True)
