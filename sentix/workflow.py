import asyncio
from .agent import Agent

class Workflow:
    def __init__(self, name):
        self.name = name
        self.steps = []

    def add_step(self, step_type, agents):
        self.steps.append({"type": step_type, "agents": agents})

    async def run(self):
        results = []
        for step in self.steps:
            step_type = step["type"]
            agents = step["agents"]

            if step_type == "sequential":
                for agent in agents:
                    result = await agent.run()
                    results.append(result)

            elif step_type == "concurrent":
                coros = [agent.run() for agent in agents]
                res = await asyncio.gather(*coros)
                results.extend(res)

            else:
                raise ValueError(f"Unknown step type: {step_type}")
        return results
