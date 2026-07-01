from app.state import AgentState
from app.tools.duplicate_tool import check_duplicate_claim


def duplicate_node(state: AgentState) -> AgentState:
    """
    Checks whether the submitted claim is a duplicate.
    """

    print("=" * 60)
    print("Duplicate Claim Node")
    print("=" * 60)

    result = check_duplicate_claim(state["claim"])

    state["duplicate_result"] = result
    state["audit_trail"].append("Duplicate Claim Check Completed")

    print("✅ Duplicate Check Completed")

    return state