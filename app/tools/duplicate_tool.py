import json


def check_duplicate_claim(claim: dict):

    with open("data/claims.json", "r") as file:
        claims = json.load(file)

    current_claim = claim.get("claim_id")

    count = 0

    for existing in claims:

        if existing["claim_id"] == current_claim:
            count += 1

    return {
        "duplicate": count > 1
    }