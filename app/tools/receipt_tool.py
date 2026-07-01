def validate_receipts(claim: dict):
    """
    Check if receipts are attached for all expenses.
    """

    missing = []

    expenses = claim.get("expenses", [])

    for expense in expenses:

        if not expense.get("receipt_attached", False):

            missing.append(expense["category"])

    return {
        "valid": len(missing) == 0,
        "missing_documents": missing
    }