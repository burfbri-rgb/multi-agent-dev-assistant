import time
import random

class PlannerAgent:
    def run(self, task):
        print("[Planner Agent] Analyzing task requirements...")
        time.sleep(1)
        plan = [
            "Define system architecture",
            "Break into modules",
            "Assign implementation steps"
        ]
        print("[Planner Agent] Plan created.")
        return plan


class CodingAgent:
    def run(self, plan):
        print("[Coding Agent] Generating implementation...")
        time.sleep(1)
        code = """
class APIService:
    def get_data(self):
        return {'status': 'success', 'data': []}
"""
        print("[Coding Agent] Code generated.")
        return code


class ReviewerAgent:
    def run(self, code):
        print("[Reviewer Agent] Reviewing generated code...")
        time.sleep(1)
        issues = ["Improve error handling", "Add logging", "Optimize structure"]
        print("[Reviewer Agent] Review complete.")
        return issues


def main():
    task = "Build a Python API service for task management"

    print("\n=== MULTI-AGENT WORKFLOW STARTED ===\n")

    planner = PlannerAgent()
    coder = CodingAgent()
    reviewer = ReviewerAgent()

    plan = planner.run(task)
    print("\nPlan:", plan)

    code = coder.run(plan)
    print("\nGenerated Code:\n", code)

    review = reviewer.run(code)
    print("\nReview Notes:", review)

    print("\n=== WORKFLOW COMPLETE ===")

    main()