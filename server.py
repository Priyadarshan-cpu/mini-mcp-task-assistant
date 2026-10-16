
from mcp.server.fastmcp import FastMCP
import json
from pathlib import Path

mcp = FastMCP("Mini Task Assistant")

FILE = Path(__file__).with_name("tasks.json")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool()
def add_task(task: str) -> str:
    """Save a new task."""
    tasks = json.loads(FILE.read_text()) if FILE.exists() else []
    tasks.append(task)
    FILE.write_text(json.dumps(tasks, indent=2))
    return f"Task saved: {task}"


@mcp.tool()
def get_tasks() -> list[str]:
    """Return all saved tasks."""
    if not FILE.exists():
        return []
    return json.loads(FILE.read_text())


if __name__ == "__main__":
    mcp.run(transport="stdio")
