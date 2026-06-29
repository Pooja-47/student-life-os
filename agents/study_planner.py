"""Study Planner Agent.

This agent is responsible for creating study plans
based on the user's academic tasks.
"""


def create_study_plan(task: str) -> str:
    """
    Create a study plan for the given task.

    Args:
        task: The academic task provided by the user.

    Returns:
        A formatted study plan as a string.
    """

    if not task or not task.strip():
        return "No task provided. Please specify a task to create a study plan."

    study_plan = f"""📚 Study Plan

Task:
- {task}

Suggested Steps:
1. Understand the task requirements.
2. Break the task into smaller parts.
3. Allocate dedicated study time.
4. Complete one part at a time.
5. Review your work before submission.
"""

    return study_plan

if __name__ == "__main__":
    task = "Complete AI Capstone Project"
    print(create_study_plan(task))