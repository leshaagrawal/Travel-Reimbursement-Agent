import json


def check_expense_limits(claim: dict):

    with open("data/limits.json") as file:
        limits = json.load(file)

    violations = []

    expenses = claim.get("expenses", [])

    for expense in expenses:

        category = expense["category"]

        amount = expense["amount"]

        limit = limits.get(category)

        if limit is not None and amount > limit:

            violations.append({
                "category": category,
                "claimed": amount,
                "limit": limit
            })

    return {
        "within_limits": len(violations) == 0,
        "violations": violations
    }