from backend.mcp.context import TicketContext

class MCPOrchestrator:
    """
    Executes MCP agents sequentially over a shared TicketContext.
    """
    def __init__(self, agents):
        self.agents = agents

    def execute(self, context: TicketContext) -> TicketContext:
        for agent in self.agents:
            context = agent.run(context)
        return context
