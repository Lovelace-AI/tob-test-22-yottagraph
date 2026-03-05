"""
Example MCP Server — a minimal FastMCP server to use as a starting point.

This server exposes simple tools that agents can call. Replace these with
your own tools that connect to your data sources or APIs.

Local testing:
    cd mcp-servers/example-server
    pip install -r requirements.txt
    python -m uvicorn server:app --host 0.0.0.0 --port 8080

Deployment:
    Use the /deploy_mcp Cursor command.
"""

from datetime import datetime, timezone

from fastmcp import FastMCP


mcp = FastMCP(
    name="example-server",
    description="An example MCP server. Replace this with your own tools and data sources.",
)


@mcp.tool()
def hello(name: str) -> str:
    """Greet someone by name. A simple test tool to verify the server is working.

    Args:
        name: The name of the person to greet.

    Returns:
        A greeting message.
    """
    return f"Hello, {name}! This MCP server is working."


@mcp.tool()
def get_current_time() -> dict:
    """Get the current UTC time. Useful for testing and timestamps.

    Returns:
        A dictionary with the current ISO-formatted UTC time.
    """
    now = datetime.now(timezone.utc)
    return {"utc_time": now.isoformat(), "unix_timestamp": int(now.timestamp())}


@mcp.tool()
def echo_data(data: dict) -> dict:
    """Echo back any data sent to this tool. Useful for testing data flow.

    Args:
        data: Any dictionary of key-value pairs.

    Returns:
        The same data, echoed back with a server timestamp.
    """
    return {
        "echoed": data,
        "server_time": datetime.now(timezone.utc).isoformat(),
        "server_name": "example-server",
    }


app = mcp.http_app()
