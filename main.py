"""
main.py
-------
Entry point for the Digital Marketing Multi-Agent System.

Usage:
    python main.py
    python main.py --batch "We need a comprehensive social media strategy for our B2B SaaS product."
    python main.py --no-save  (disables report saving)
"""

import os
import sys
import asyncio
import argparse
from dotenv import load_dotenv

load_dotenv()

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.messages import TextMessage, StopMessage, MultiModalMessage
from rich.console import Console
from rich.panel import Panel

from agents.orchestrator import create_orchestrator
from agents.market_research import create_market_research_agent
from agents.website_presence import create_website_presence_agent
from agents.email_marketing import create_email_marketing_agent
from agents.copywriting import create_copywriting_agent
from agents.seo import create_seo_agent
from agents.youtube_marketing import create_youtube_marketing_agent
from agents.social_media import create_social_media_agent
from agents.linkedin_marketing import create_linkedin_marketing_agent
from agents.app_marketing import create_app_marketing_agent
from agents.google_adwords import create_google_adwords_agent
from agents.facebook_ads import create_facebook_ads_agent
from agents.google_analytics import create_google_analytics_agent
from agents.summary import create_summary_agent
from agents.user import create_user
from config.agent_config import TERMINATION_KEYWORD
from utils.prompts import WELCOME_MESSAGE
from utils.report_generator import save_report, extract_report_from_chat

console = Console()


async def build_team(interactive: bool = True):
    """Instantiate agents and wire them into a SelectorGroupChat Team."""

    agents = [
        create_orchestrator(),
        create_market_research_agent(),
        create_website_presence_agent(),
        create_email_marketing_agent(),
        create_copywriting_agent(),
        create_seo_agent(),
        create_youtube_marketing_agent(),
        create_social_media_agent(),
        create_linkedin_marketing_agent(),
        create_app_marketing_agent(),
        create_google_adwords_agent(),
        create_facebook_ads_agent(),
        create_google_analytics_agent(),
        create_summary_agent(),
    ]

    # Only add the human bridge if we are in interactive mode
    if interactive:
        agents.append(create_user())

    user_exit_condition   = TextMentionTermination("quit") | TextMentionTermination("exit")
    system_done_condition = TextMentionTermination(TERMINATION_KEYWORD)

    termination = user_exit_condition | system_done_condition

    selector_model = OpenAIChatCompletionClient(
        model=os.getenv("LLM_MODEL", "gpt-4o")
    )

    team = SelectorGroupChat(
        participants=agents,
        model_client=selector_model,
        termination_condition=termination,
    )

    return team


async def run_interactive() -> None:
    console.print(Panel(WELCOME_MESSAGE, style="bold cyan", expand=False))

    team = await build_team()

    instruction = (
        "Orchestrator, please greet the user, briefly introduce the marketing team, "
        "and ask: 'What digital marketing challenge can we help you with today?'"
    )

    history = []
    is_first_message = True

    async for message in team.run_stream(task=instruction):
        history.append(message)

        if is_first_message:
            is_first_message = False
            continue

        if isinstance(message, TextMessage):
            console.print(f"\n[bold]{message.source}:[/bold] {message.content}")
        elif isinstance(message, MultiModalMessage):
            console.print(f"\n[bold]{message.source}:[/bold] [Multi-modal content received]")
        elif isinstance(message, StopMessage):
            console.print("\n[italic yellow]Agents have reached a stopping point.[/italic yellow]")

    if os.getenv("SAVE_REPORT", "true").lower() == "true":
        console.print("\n[bold green]Session ended. Generating final report...[/bold green]")
        report_content = extract_report_from_chat(history)
        if report_content:
            file_path = save_report(report_content)
            console.print(f"[bold green]Report saved to:[/bold green] {file_path}")
        else:
            console.print(
                "[bold yellow]No formal report was extracted from the conversation.[/bold yellow]"
            )


async def run_batch(requirements: str, save: bool = True) -> None:
    console.print("[bold cyan]Running in BATCH mode...[/bold cyan]")

    team = await build_team(interactive=False)

    instruction = (
        f"Orchestrator, please coordinate the full marketing team to analyse the following "
        f"challenge and produce a comprehensive digital marketing strategy: {requirements}. "
        f"Once the analysis is complete, have the Summary Agent produce a final structured report."
    )

    history = []

    async for message in team.run_stream(task=instruction):
        if hasattr(message, "source") and hasattr(message, "content"):
            history.append(message)

        if isinstance(message, TextMessage):
            console.print(f"\n[bold]{message.source}:[/bold] {message.content}")
        elif isinstance(message, MultiModalMessage):
            console.print(f"\n[bold]{message.source}:[/bold] [Multi-modal content received]")
        elif isinstance(message, StopMessage):
            console.print("\n[italic yellow]Agents have reached a stopping point.[/italic yellow]")

    if save:
        console.print("\n[bold green]Generating final report...[/bold green]")
        report_content = extract_report_from_chat(history)
        if report_content:
            file_path = save_report(report_content)
            console.print(f"[bold green]Report saved to:[/bold green] {file_path}")
        else:
            console.print(
                "[bold yellow]No formal report was extracted from the conversation.[/bold yellow]"
            )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="📣 Digital Marketing Multi-Agent System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py
  python main.py --batch "B2B SaaS startup needs a full-funnel digital marketing strategy"
  python main.py --batch "E-commerce brand wants to grow Instagram and improve Google Ads ROI" --no-save
""",
    )
    parser.add_argument(
        "--batch",
        metavar="CHALLENGE",
        type=str,
        default=None,
        help="Run in batch mode with the given marketing challenge (non-interactive).",
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        default=False,
        help="Do not save the report to disk.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.batch:
        asyncio.run(run_batch(args.batch, save=not args.no_save))
    else:
        asyncio.run(run_interactive())


if __name__ == "__main__":
    main()
