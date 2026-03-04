import asyncio
from rich.console import Console

console = Console()

class Agent:
    def __init__(self, name):
        self.name = name

    async def run(self, data=None):
        console.log(f"[green]Agent {self.name} started[/green]")
        await asyncio.sleep(1)  # Simulate task
        console.log(f"[blue]Agent {self.name} finished[/blue]")
        return f"{self.name} result"
