from app.graph import graph
from app.models import ClaimRequest, ClaimResponse
from app.state import create_initial_state


def process_claim(claim: ClaimRequest) -> ClaimResponse:
    """
    Executes the LangGraph workflow for a reimbursement claim.
    """

    initial_state = create_initial_state(claim)

    final_state = graph.invoke(initial_state)

    return ClaimResponse(
        decision=final_state["decision"] or "Manual Review",
        approved_amount=final_state["approved_amount"],
        deduction=final_state["deduction"],
        confidence=final_state["confidence_score"],
        missing_documents=final_state["missing_documents"],
        policy_reference=", ".join(final_state["policy_references"]),
        explanation=final_state["explanation"] or "Workflow executed successfully.",
        audit_trail=final_state["audit_trail"]
    )