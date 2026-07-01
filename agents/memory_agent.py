"""Memory Agent for Student Life OS.

This agent is responsible for storing and retrieving
simple user memories during the application's runtime.
"""

import re
class MemoryAgent:
    """Handles memory-related user requests."""

    def __init__(self):
        """Initializes the Memory Agent."""
        self.name = "Memory Agent"
        self.memories = []

    def handle(self, user_input: str):
        """
        Stores a memory provided by the user.
        """

        if not isinstance(user_input, str) or not user_input.strip():
            return {
                "status": "error",
                "message": "No memory provided."
            }

        memory = user_input.strip()

        memory = re.sub(
            r"(?i)^remember\b\s*:?\s*",
            "",
            memory
        )

        if not memory:
            return {
                "status": "error",
                "message": "No memory provided."
            }

        self.memories.append(memory)

        return {
            "status": "success",
            "message": f"Memory stored: {memory}"
        }


if __name__ == "__main__":
    agent = MemoryAgent()

    test_inputs = [
        "Remember I have an AI exam tomorrow",
        "Remember: My interview is on Monday",
        "remember Python is my favorite language",
        "Remember",
        "Remembering AI",
        ""
    ]

    for memory in test_inputs:
        print("\nInput:", repr(memory))
        print("Output:", agent.handle(memory))

    print("\nStored Memories:")
    print(agent.memories)