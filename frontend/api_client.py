import requests

BASE_URL = "http://127.0.0.1:8000"


def submit_claim(claim_data: dict):
    """
    Sends claim to FastAPI.
    """

    try:
        response = requests.post(
            f"{BASE_URL}/claim",
            json=claim_data,
            timeout=120
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:

        return {
            "error": str(e)
        }