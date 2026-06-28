"""Coordinator Agent module for the Student Life OS multi-agent AI system.

This module contains the CoordinatorAgent class, which acts as the central router
directing user prompts to the correct specialized sub-agent.
"""


class CoordinatorAgent:
    """An agent that routes user queries to specialized sub-agents."""

    def __init__(self) -> None:
        """Initializes the Coordinator Agent with its name."""
        self.name: str = "Coordinator Agent"

    def route_request(self, user_input: str) -> str:
        """Routes the user's input to the correct specialized agent.

        Analyzes the text for key phrases and returns the identifier of the
        appropriate agent, or 'unknown' if no match is found.

        Args:
            user_input: The raw text prompt from the user.

        Returns:
            The string identifier of the target agent (e.g., 'study_planner',
            'research_agent', 'memory_agent') or 'unknown'.
        """
        # Create a new variable for the cleaned input to avoid mutating parameters
        clean_input = user_input.lower()

        # Define keyword mappings to separate routing data from execution logic
        routing_rules = {
            "study_planner": ["study", "plan"],
            "research_agent": ["research", "search"],
            "memory_agent": ["save", "remember"],
        }

        # Check keywords for each agent
        for agent_id, keywords in routing_rules.items():
            if any(keyword in clean_input for keyword in keywords):
                return agent_id

        return "unknown"


if __name__ == "__main__":
    # Instantiate the agent and demonstrate routing behavior
    agent = CoordinatorAgent()

    # The expected output is shown next to each print statement for clarity
    print(agent.route_request("help me plan my study"))  # Expected: study_planner
    print(agent.route_request("research AI agents"))    # Expected: research_agent
    print(agent.route_request("save my notes"))          # Expected: memory_agent
    print(agent.route_request("What is the weather today?"))  # Expected: unknown