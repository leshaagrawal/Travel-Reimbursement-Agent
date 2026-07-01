from app.tools.receipt_tool import validate_receipts


def test_receipts():

    claim = {
        "expenses": [
            {
                "category": "Hotel",
                "receipt_attached": True
            }
        ]
    }

    result = validate_receipts(claim)

    assert result["valid"] is True