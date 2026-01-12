from backend.mcp.agent_base import MCPAgent

# -------------------------
# Category-level templates
# -------------------------
SUMMARY_TEMPLATES = {
    "Payment Issue": "Customer reports a payment-related issue",
    "Delivery Issue": "Customer reports a delivery-related issue",
    "Technical Issue": "Customer reports a technical issue while using the service",
    "Account Issue": "Customer reports an account-related issue"
}

# -------------------------
# Entity-driven phrases
# -------------------------
ENTITY_PHRASES = {
    "ORDER_ID": lambda e: f"associated with {e}",
    "TRANSACTION_ID": lambda _: "related to a transaction",
    "ACCOUNT_NUMBER": lambda _: "related to a specific account",
    "PAN_NUMBER": lambda _: "linked to identity verification",
    "ACCOUNT_STATUS": lambda _: "resulting in restricted account access",
    "LOC": lambda e: f"reported from {e}",
    "EMAIL": lambda _: None,
    "PHONE_NUMBER": lambda _: None
}


def summarize_ticket(category: str, entities: list) -> str:
    """
    Generate a structured summary using category and extracted entities.
    """
    base = SUMMARY_TEMPLATES.get(
        category,
        "Customer reports an issue requiring assistance"
    )

    clauses = []

    for ent in entities or []:
        ent_type = ent.get("type")
        ent_text = ent.get("text")

        if not ent_type or not ent_text:
            continue

        if ent_type in ENTITY_PHRASES:
            phrase = ENTITY_PHRASES[ent_type](ent_text)
            if phrase and phrase not in clauses:
                clauses.append(phrase)

    if clauses:
        return base + ", " + ", ".join(clauses) + "."

    return base + "."


class SummaryAgent(MCPAgent):
    def run(self, context):
        if not context.category:
            context.summary = "Customer reports an issue requiring assistance."
            context.agent_logs.append(
                "SummaryAgent → fallback summary used"
            )
            return context

        summary = summarize_ticket(
            context.category,
            context.entities
        )

        context.summary = summary
        context.agent_logs.append(
            "SummaryAgent → summary generated"
        )

        return context
