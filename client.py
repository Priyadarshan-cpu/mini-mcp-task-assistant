
import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

#THIS CALLS MCP SERVER AND ASYNCH FOR ASYNCHRONOUS COMMUNICATION BETWEEN CLIENT AND SERVER
async def main():
    server = StdioServerParameters(
        command=sys.executable,
        args=[str(Path(__file__).with_name("server.py"))]
    )

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:")
            for tool in tools.tools:
                print("-", tool.name)

            result = await session.call_tool(
                "add", arguments={"a": 10, "b": 20}
            )
            print("Addition:", result.content)

            result = await session.call_tool(
                "add_task",
                arguments={"task": "Learn MCP"}
            )
            print("Save:", result.content)

            result = await session.call_tool(
                "get_tasks", arguments={}
            )
            print("Tasks:", result.content)


if __name__ == "__main__":
    print("RUNNING")
    asyncio.run(main())
