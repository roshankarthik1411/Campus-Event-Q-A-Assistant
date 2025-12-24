import sys
import os

# Ensure project root is on Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.ask_assistant import ask_assistant

print("Campus Event Q&A Assistant")
print("=" * 40)

queries = [
    "When is the Tech Fest happening?",
    "Where is the Career Fair located?",
    "Tell me about the Hackathon",
    "What's the schedule for the Music Concert?",
    "Tell me a joke",
    "What's the weather like?"
]

for q in queries:
    print(f"\nQuery: {q}")
    response = ask_assistant(q)

    if isinstance(response, dict):
        print("Response:")
        print(response)
    else:
        print("Response:", response)

    print("-" * 40)
