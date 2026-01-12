import re
from transformers import pipeline
from backend.mcp.agent_base import MCPAgent

# Load NER model once
_ner = pipeline(
    "ner",
    model="dslim/bert-base-NER",
    aggregation_strategy="simple"
)

def extract_custom_entities(text: str):
    entities = []

    patterns = [
        (r"\b\d{10,16}\b", "ACCOUNT_NUMBER"),
        (r"\b[A-Z]{4}0\d{6}\b", "IFSC_CODE"),
        (r"\bbranch\s+[A-Za-z]+\b", "BRANCH_NAME"),
        (r"Order ID\s*\d+", "ORDER_ID"),
        (r"Transaction ID\s*[A-Za-z0-9]+", "TRANSACTION_ID"),
        (r"\b[A-Z]{5}[0-9]{4}[A-Z]\b", "PAN_NUMBER"),
        (r"\b[\w.-]+@[\w.-]+\b", "UPI_ID"),
        (r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "EMAIL"),
        (r"\b\d{10}\b", "PHONE_NUMBER"),
    ]

    for pattern, label in patterns:
        for match in re.findall(pattern, text, flags=re.IGNORECASE):
            entities.append({
                "text": match.strip(),
                "type": label
            })

    return entities


def extract_entities(text: str):
    ner_entities = _ner(text)

    model_entities = [
        {
            "text": e["word"].strip(),
            "type": e["entity_group"].upper()
        }
        for e in ner_entities
    ]

    all_entities = model_entities + extract_custom_entities(text)

    # Deduplicate
    seen = set()
    unique_entities = []

    for e in all_entities:
        key = (e["text"].lower(), e["type"])
        if key not in seen:
            seen.add(key)
            unique_entities.append(e)

    return unique_entities


class EntityAgent(MCPAgent):
    def run(self, context):
        entities = extract_entities(context.raw_text)

        context.entities = entities
        context.agent_logs.append(
            f"EntityAgent → extracted {len(entities)} entities"
        )

        return context
