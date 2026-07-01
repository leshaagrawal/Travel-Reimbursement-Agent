from pydantic import BaseModel
from typing import List


class DecisionResponse(BaseModel):
    decision: str
    approved_amount: float
    deduction: float
    confidence: float
    policy_references: List[str]
    explanation: str