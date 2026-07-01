from langgraph.graph import StateGraph, END

from app.state import AgentState

from app.nodes.policy_node import policy_node
from app.nodes.receipt_node import receipt_node
from app.nodes.duplicate_node import duplicate_node
from app.nodes.limit_node import limit_node
from app.nodes.approval_node import approval_node
from app.nodes.decision_node import decision_node
workflow = StateGraph(AgentState)

workflow.add_node("policy", policy_node)
workflow.add_node("receipt", receipt_node)
workflow.add_node("duplicate", duplicate_node)
workflow.add_node("limit", limit_node)
workflow.add_node("approval", approval_node)
workflow.add_node("decision", decision_node)

workflow.set_entry_point("policy")

workflow.add_edge("policy", "receipt")
workflow.add_edge("receipt", "duplicate")
workflow.add_edge("duplicate", "limit")
workflow.add_edge("limit", "approval")
workflow.add_edge("approval", "decision")
workflow.add_edge("decision", END)

graph = workflow.compile()