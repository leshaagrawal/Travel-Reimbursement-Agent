from typing import TypedDict, Dict, Any, List

from app.models import ClaimRequest


class AgentState(TypedDict):
    """
    Shared state that is passed between all LangGraph nodes.
    """

    # Original Claim
    claim: Dict[str, Any]

    # Retrieved Policy
    policy_context: str

    # Tool Results
    receipt_result: Dict[str, Any]
    duplicate_result: Dict[str, Any]
    limit_result: Dict[str, Any]
    approval_result: Dict[str, Any]

    # Final Decision
    decision: str
    approved_amount: float
    deduction: float
    confidence_score: float
    explanation: str

    # Additional Information
    policy_references: List[str]
    missing_documents: List[str]
    audit_trail: List[str]


def create_initial_state(claim: ClaimRequest) -> AgentState:
    """
    Creates the initial state for the LangGraph workflow.
    """

    return {
    "claim": claim.model_dump(),

    "policy_context": "",

    "receipt_result": {},
    "duplicate_result": {},
    "limit_result": {},
    "approval_result": {},

    "decision": "",
    "approved_amount": 0.0,
    "deduction": 0.0,
    "confidence_score": 0.0,

    "explanation": "",
    "audit_trail": [],
    "policy_references": [],
    "missing_documents": [],
}