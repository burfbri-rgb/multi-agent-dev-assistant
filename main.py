from crewai import Agent, Task, Crew

planner = Agent(
    role='Planner Agent',
    goal='Break complex software requests into structured subtasks',
    backstory='Expert in software architecture and planning.'
)

coder = Agent(
    role='Coding Agent',
    goal='Generate clean implementation code',
    backstory='Experienced software engineer focused on rapid implementation.'
)

reviewer = Agent(
    role='Reviewer Agent',
    goal='Validate outputs and identify improvements',
    backstory='Senior code reviewer specializing in quality assurance.'
)

planning_task = Task(
    description='Plan a Python API service for task management.',
    agent=planner
)

coding_task = Task(
    description='Generate implementation code based on the architecture plan.',
    agent=coder
)

review_task = Task(
    description='Review generated code for issues and optimization opportunities.',
    agent=reviewer
)

crew = Crew(
    agents=[planner, coder, reviewer],
    tasks=[planning_task, coding_task, review_task]
)

result = crew.kickoff()
print(result)