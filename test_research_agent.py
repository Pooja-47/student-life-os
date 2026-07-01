from agents.research_agent import ResearchAgent

agent = ResearchAgent()

# Test cases
test_queries = [
    "data science",
    "machine learning career",
    "",
    "  artificial intelligence  "
]

for q in test_queries:
    print("\n======================")
    print("INPUT:", repr(q))
    result = agent.handle(q)
    print("OUTPUT:", result)