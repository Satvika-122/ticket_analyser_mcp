from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class TicketContext(BaseModel):
    raw_text: Optional[str] = None

    category: Optional[str] = None
    entities: List[Dict[str, Any]] = []
    summary: Optional[str] = None

    qa_validation: Optional[Dict[str, Any]] = None

    agent_logs: List[str] = []
