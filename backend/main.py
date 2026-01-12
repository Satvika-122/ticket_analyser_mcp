from fastapi import FastAPI
from pydantic import BaseModel

from backend.mcp.context import TicketContext
from backend.mcp.orchestrator import MCPOrchestrator

from backend.agents.classifier_agent import ClassificationAgent
from backend.agents.entity_agent import EntityAgent
from backend.agents.summary_agent import SummaryAgent
from backend.agents.qa_agent import QAAgent

app = FastAPI(title="AI Ticket Analyzer – MCP Server")

# -------------------------
# API Request Schema
# -------------------------
class TicketRequest(BaseModel):
    text: str


# -------------------------
# MCP Pipeline
# -------------------------
pipeline = MCPOrchestrator([
    ClassificationAgent(),
    EntityAgent(),
    SummaryAgent(),
    QAAgent()
])


# -------------------------
# API Endpoint
# -------------------------
@app.post("/analyze")
def analyze_ticket(req: TicketRequest):
    context = TicketContext(
        raw_text=req.text
    )

    result = pipeline.execute(context)
    return result
