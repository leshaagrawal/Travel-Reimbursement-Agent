from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.agent import process_claim
from app.models import ClaimRequest, ClaimResponse
from app.vectorstore import get_vectorstore


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Runs once when the application starts.
    """

    print("=" * 50)
    print("Initializing Vector Database...")
    print("=" * 50)

    app.state.vector_db = get_vectorstore()

    print("Application Ready!")

    yield

    print("Shutting down...")


app = FastAPI(
    title="Travel Reimbursement Approval Agent",
    version="1.0.0",
    description="AI-powered Travel Reimbursement Approval System",
    lifespan=lifespan
)


@app.get("/")
def home():
    return {
        "message": "Travel Reimbursement Approval Agent is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/claim", response_model=ClaimResponse)
def evaluate_claim(claim: ClaimRequest):
    return process_claim(claim)