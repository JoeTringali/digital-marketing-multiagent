"""
agents/user.py
--------------
UserProxy agent – bridges the human user into the multi-agent team.
When the Orchestrator needs additional information from the user, it
routes here and this agent surfaces the question to the human in the
terminal.
"""

import os
from autogen_agentchat.agents import UserProxyAgent


def create_user() -> UserProxyAgent:
    return UserProxyAgent(
        name="UserProxy",
        description=(
            "A proxy for the human user. Route here whenever you need the user "
            "to provide additional information, approve a direction, or answer a "
            "clarifying question."
        ),
    )
