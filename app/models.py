from pydantic import BaseModel
from typing import List


class Expense(BaseModel):
    category: str
    vendor: str
    amount: float
    receipt_attached: bool


class ClaimRequest(BaseModel):
    claim_id: str
    employee_id: str
    employee_name: str
    trip_id: str
    total_amount: float
    expenses: List[Expense]


class ClaimResponse(BaseModel):
    decision: str
    approved_amount: float
    deduction: float
    confidence: float
    missing_documents: List[str]
    policy_reference: str
    explanation: str
    audit_trail: List[str]