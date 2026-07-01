import json
from app.decision_schema import DecisionResponse


def parse_decision(response: str) -> DecisionResponse:
    """
    Parses the JSON returned by the LLM into a validated Pydantic model.
    """

    data = json.loads(response)

    return DecisionResponse(**data)