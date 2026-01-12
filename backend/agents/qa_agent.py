from backend.mcp.agent_base import MCPAgent

# -------------------------
# Category keyword checks
# -------------------------
CATEGORY_KEYWORDS = {
    "Payment Issue": ["payment", "transaction"],
    "Account Issue": ["account", "identity"],
    "Technical Issue": ["technical", "error", "issue"],
    "Delivery Issue": ["delivery", "shipment", "order"]
}

GENERIC_FALLBACK = "customer reports an issue requiring assistance"


def validate_response(category: str, summary: str):
    """
    Validate classification and summary output.
    Returns validity flag and confidence score.
    """
    category = category.strip()
    summary = summary.strip().lower()

    confidence = 0.3
    valid = False

    # 1️⃣ Reject generic fallback summary
    if GENERIC_FALLBACK in summary:
        return {
            "valid": False,
            "confidence": 0.3
        }

    # 2️⃣ Category alignment
    keywords = CATEGORY_KEYWORDS.get(category, [])
    category_match = any(k in summary for k in keywords)

    if category_match:
        confidence += 0.4
        valid = True

    # 3️⃣ Implicit entity / relation presence
    if any(k in summary for k in ["associated", "related", "linked"]):
        confidence += 0.3

    confidence = min(round(confidence, 2), 1.0)

    return {
        "valid": valid,
        "confidence": confidence
    }


class QAAgent(MCPAgent):
    def run(self, context):
        # Guard clauses
        if not context.category or not context.summary:
            context.agent_logs.append(
                "QAAgent → skipped (missing category or summary)"
            )
            context.qa_validation = {
                "valid": False,
                "confidence": 0.0
            }
            return context

        result = validate_response(
            context.category,
            context.summary
        )

        context.qa_validation = result

        context.agent_logs.append(
            f"QAAgent → valid={result['valid']}, confidence={result['confidence']}"
        )

        return context
