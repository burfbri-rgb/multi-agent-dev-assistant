print("\n=== MULTI-AGENT MOCK SYSTEM STARTED ===\n")

class Planner:
    def run(self):
        print("[Planner] Breaking task into steps...")
        return ["design", "implement", "review"]

class Coder:
    def run(self, plan):
        print("[Coder] Writing code based on plan...")
        return "def hello(): return 'Hello World'"

class Reviewer:
    def run(self, code):
        print("[Reviewer] Checking code quality...")
        return "Looks good. Add logging in production."

planner = Planner()
coder = Coder()
reviewer = Reviewer()

plan = planner.run()
print("Plan:", plan)

code = coder.run(plan)
print("Code:", code)

review = reviewer.run(code)
print("Review:", review)

print("\n=== DONE ===")