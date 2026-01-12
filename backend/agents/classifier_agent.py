from transformers import pipeline
from backend.mcp.agent_base import MCPAgent

_classifier = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

VALID_LABELS = [
    "Payment Issue",
    "Account Issue",
    "Technical Issue",
    "Delivery Issue",
    "Other"
]

def classify_ticket(text: str) -> str:
    prompt = f"""
Classify the following customer support ticket into one of these category:
Payment Issue
Account Issue
Technical Issue
Delivery Issue
Other

Ticket:
{text}

Answer with ONLY one of these labels exactly.
"""
    result = _classifier(prompt, max_length=10)
    output = result[0]["generated_text"].strip()

    for label in VALID_LABELS:
        if label.lower() in output.lower():
            return label

    return "Other"


class ClassificationAgent(MCPAgent):
    def run(self, context):
        category = classify_ticket(context.raw_text)
        context.category = category
        context.agent_logs.append(
            f"ClassificationAgent → {category}"
        )
        return context
