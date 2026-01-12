from backend.mcp.context import TicketContext

class MCPAgent:
    """
    Base class for all MCP agents.
    Every agent must implement run(context) and return the context.
    """
    def run(self, context: TicketContext) -> TicketContext:
        raise NotImplementedError(
            "MCP agents must implement the run() method"
        )
