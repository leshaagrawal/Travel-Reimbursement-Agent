from app.state import AgentState
from app.tools.limit_tool import check_expense_limits


def limit_node(state: AgentState) -> AgentState:
    """
    Checks expense limits against company policy.
    """

    print("=" * 60)
    print("Expense Limit Node")
    print("=" * 60)

    result = check_expense_limits(state["claim"])

    state["limit_result"] = result
    state["audit_trail"].append("Expense Limit Validation Completed")
    print("✅ Expense Limit Validation Completed")

    return state