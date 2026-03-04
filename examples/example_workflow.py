import asyncio
from sentix.workflow import Workflow
from sentix.agent import Agent

async def main():
    workflow = Workflow("Example Workflow")

    # Step 1: Sequential
    workflow.add_step("sequential", [Agent("setup_env"), Agent("load_data")])

    # Step 2: Concurrent
    workflow.add_step("concurrent", [Agent("process_A"), Agent("process_B")])

    # Step 3: Sequential
    workflow.add_step("sequential", [Agent("cleanup"), Agent("notify")])

    results = await workflow.run()
    print("Workflow Results:", results)

if __name__ == "__main__":
    asyncio.run(main())
