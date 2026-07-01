from app.state import AgentState
from app.tools.approval_tool import get_approval_level


def approval_node(state: AgentState) -> AgentState:
    """
    Determines approval level based on total claim amount.
    """

    print("=" * 60)
    print("Approval Node")
    print("=" * 60)

    claim = state["claim"]

    expenses = claim.get("expenses", [])

    total_amount = sum(
        expense.get("amount", 0)
        for expense in expenses
    )

    approval = get_approval_level(total_amount)

    state["approval_result"] = {
        "approval_level": approval
    }
    state["audit_trail"].append(
    f"Approval Level: {state['approval_result']['approval_level']}"
)

    print(f"✅ Approval Level : {approval}")

    return state