from app.state import AgentState
from app.tools.policy_tool import get_policy_context
from app.logger import logger

def policy_node(state: AgentState) -> AgentState:
    """
    Retrieve the most relevant travel policy
    using the submitted claim.
    """

    print("=" * 60)
    logger.info("Policy Node Started")
    print("=" * 60)

    claim = state["claim"]

    # Create a search query from the claim
    search_query = f"""
    Employee is claiming expenses for:
    {claim}
    """

    policy = get_policy_context(search_query)

    state["policy_context"] = policy
    state["audit_trail"].append("Policy Retrieved")

    print("Policy Retrieved Successfully")

    return state