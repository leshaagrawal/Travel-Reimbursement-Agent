import json

from app.state import AgentState
from app.prompts import DECISION_PROMPT
from app.llm import llm
from app.decision_parser import parse_decision


def decision_node(state: AgentState) -> AgentState:

    print("=" * 60)
    print("Decision Node (LLM)")
    print("=" * 60)

    # =====================================================
    # BUSINESS RULE 1
    # Missing Receipts
    # =====================================================

    if not state["receipt_result"]["valid"]:

        state["decision"] = "Manual Review"
        state["approved_amount"] = 0
        state["deduction"] = 0
        state["confidence_score"] = 1.0
        state["policy_references"] = ["Receipt Policy"]
        state["missing_documents"] = state["receipt_result"]["missing_documents"]

        state["explanation"] = (
            "One or more receipts are missing. "
            "According to company policy, the claim requires manual review."
        )

        print("Business Rule Triggered → Missing Receipt")

        return state

    # =====================================================
    # BUSINESS RULE 2
    # Duplicate Claim
    # =====================================================

    if state["duplicate_result"]["duplicate"]:

        state["decision"] = "Manual Review"
        state["approved_amount"] = 0
        state["deduction"] = 0
        state["confidence_score"] = 1.0
        state["policy_references"] = ["Duplicate Claim Policy"]

        state["explanation"] = (
            "A duplicate claim was detected. "
            "The reimbursement has been routed for manual review."
        )

        print("Business Rule Triggered → Duplicate Claim")

        return state

    # =====================================================
    # OTHERWISE
    # LET LLM DECIDE
    # =====================================================

    prompt = DECISION_PROMPT.format(

        claim=json.dumps(state["claim"], indent=2),

        policy=state["policy_context"],

        receipt_result=json.dumps(
            state["receipt_result"], indent=2
        ),

        duplicate_result=json.dumps(
            state["duplicate_result"], indent=2
        ),

        limit_result=json.dumps(
            state["limit_result"], indent=2
        ),

        approval_result=json.dumps(
            state["approval_result"], indent=2
        ),
    )

    try:

        response = llm.invoke(prompt)

        print("\nLLM Response\n")
        print(response.content)

        result = parse_decision(response.content)

        state["decision"] = result.decision
        state["approved_amount"] = result.approved_amount
        state["deduction"] = result.deduction
        state["confidence_score"] = result.confidence
        state["policy_references"] = result.policy_references
        state["explanation"] = result.explanation

        print("AI Decision Generated")

    except Exception as e:

        print("LLM Error :", e)

        state["decision"] = "Manual Review"
        state["approved_amount"] = 0
        state["deduction"] = 0
        state["confidence_score"] = 0
        state["policy_references"] = []
        state["explanation"] = (
            "The AI response could not be parsed."
        )
        state["audit_trail"].append(
       "Business Rule: Missing Receipt → Manual Review"
        )
        state["audit_trail"].append(
       "Business Rule: Duplicate Claim → Manual Review"
        )
        state["audit_trail"].append("AI Decision Generated")
    return state