import json


def get_approval_level(total_amount: float):

    with open("data/approval_matrix.json") as file:
        matrix = json.load(file)

    if total_amount <= matrix["auto_approval_limit"]:

        return "Auto Approval"

    elif total_amount <= matrix["manager_approval_limit"]:

        return "Manager Approval"

    return "Finance Approval"