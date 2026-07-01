from app.state import AgentState
from app.tools.receipt_tool import validate_receipts


def receipt_node(state: AgentState) -> AgentState:
    """
    Validates whether all required receipts are attached.
    """

    print("=" * 60)
    print("Receipt Node")
    print("=" * 60)

    result = validate_receipts(state["claim"])

    state["receipt_result"] = result
    state["missing_documents"] = result.get("missing_documents", [])
    state["audit_trail"].append("Receipt Validation Completed")
    print("✅ Receipt Validation Completed")

    return state