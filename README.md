# ✈️ AI Travel Reimbursement Approval Agent

An AI-powered Travel Reimbursement Approval System that automates employee travel claim evaluation using **FastAPI**, **LangGraph**, **Groq Llama 3**, **ChromaDB**, **RAG (Retrieval-Augmented Generation)**, and **Streamlit**.

The system validates travel expenses against company policy, checks receipts, detects duplicate claims, determines the required approval level, and generates an explainable AI decision.

---

# 📌 Features

- ✅ AI-powered reimbursement approval
- ✅ Retrieval-Augmented Generation (RAG)
- ✅ Company policy retrieval using ChromaDB
- ✅ Receipt validation
- ✅ Duplicate claim detection
- ✅ Expense limit validation
- ✅ Approval matrix (Auto / Manager / Finance)
- ✅ Explainable AI decisions
- ✅ Confidence score
- ✅ FastAPI REST API
- ✅ Interactive Streamlit dashboard
- ✅ Swagger API documentation
- ✅ Unit testing with Pytest

---

# 🏗 Project Architecture

```
                Streamlit Frontend
                       │
                       ▼
                FastAPI Backend
                       │
                       ▼
                 LangGraph Workflow
                       │
 ┌───────────────────────────────────────────────┐
 │                                               │
 │  Policy Retrieval (RAG)                       │
 │  Receipt Validation                           │
 │  Duplicate Claim Detection                    │
 │  Expense Limit Validation                     │
 │  Approval Matrix                              │
 │  AI Decision Generation (Groq Llama 3)        │
 │                                               │
 └───────────────────────────────────────────────┘
                       │
                       ▼
               Final Approval Decision
```

---

# 📂 Project Structure

```
Travel-Reimbursement-Agent/

│
├── app/
│   ├── api.py
│   ├── agent.py
│   ├── graph.py
│   ├── state.py
│   ├── vectorstore.py
│   ├── prompts.py
│   ├── schemas.py
│   │
│   └── nodes/
│       ├── policy_node.py
│       ├── receipt_node.py
│       ├── duplicate_node.py
│       ├── expense_limit_node.py
│       ├── approval_node.py
│       └── decision_node.py
│
├── frontend/
│   ├── streamlit_app.py
│   ├── api_client.py
│   └── styles.py
│
├── data/
│   └── policy.md
│
├── tests/
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Tech Stack

| Component | Technology |
|------------|------------|
| Backend | FastAPI |
| Workflow | LangGraph |
| LLM | Groq Llama 3 |
| Vector Database | ChromaDB |
| Embeddings | HuggingFace MiniLM |
| Frontend | Streamlit |
| Testing | Pytest |

---

# 🚀 Setup Instructions

## 1. Clone Repository

```bash
git clone <repository-url>

cd Travel-Reimbursement-Agent
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Required Environment Variables

Create a `.env` file inside the project root.

```
GROQ_API_KEY=your_groq_api_key
```

---

# ▶ Running the Backend

```bash
uvicorn app.api:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# ▶ Running the Frontend

```bash
cd frontend

streamlit run streamlit_app.py
```

Streamlit URL

```
http://localhost:8501
```

---

# 🧠 Workflow

The reimbursement claim passes through multiple AI validation stages.

### Step 1

Employee submits travel reimbursement claim.

↓

### Step 2

FastAPI receives the request.

↓

### Step 3

LangGraph starts the workflow.

↓

### Step 4

Relevant travel policy is retrieved from ChromaDB using RAG.

↓

### Step 5

Receipt validation is performed.

↓

### Step 6

Duplicate claim detection.

↓

### Step 7

Expense limit validation.

↓

### Step 8

Approval level is determined.

↓

### Step 9

Groq Llama 3 generates the final decision.

↓

### Step 10

The API returns

- Decision
- Approved Amount
- Deduction
- Confidence Score
- Policy References
- Explanation
- Missing Documents
- Audit Trail

---

# 🤖 AI Decisions

The AI returns one of the following decisions.

- Approved
- Partially Approved
- Manual Review
- Rejected

Each response includes:

- Decision
- Explanation
- Confidence Score
- Approved Amount
- Deduction
- Policy References

---

# 🧪 Testing

Run all tests

```bash
pytest
```

Example output

```
====================

4 passed

====================
```

---

# 📷 Sample Outputs

The project demonstrates three scenarios.

### Approved Claim

- All receipts available
- Within policy limits
- No duplicate claim
- Auto approval

---

### Partially Approved

- Expense exceeds policy limit
- Deduction applied
- Partial reimbursement

---

### Manual Review

- Missing receipt
- Duplicate claim
- Insufficient information
- Human verification required

---

# 📌 Key Design Choices

- FastAPI was chosen for high-performance REST APIs.
- LangGraph models the reimbursement workflow as modular nodes.
- ChromaDB enables semantic search over company travel policies.
- RAG ensures the LLM uses relevant policy sections instead of relying only on prompts.
- Groq Llama 3 provides fast and explainable AI decisions.
- Streamlit offers a lightweight interactive frontend for rapid prototyping and demonstration.

---

# 📈 Future Improvements

- OCR-based receipt extraction
- Real-time receipt verification
- Database integration (PostgreSQL)
- Authentication and Role-Based Access Control
- Cloud deployment (AWS/Azure/GCP)
- Email notifications
- Multi-company policy support
- Dashboard analytics
- Audit logging
- Human-in-the-loop approval workflow

---

# ⚠ Assumptions

- Travel policy is stored as a Markdown document.
- Receipt validation is based on receipt availability.
- Duplicate claim detection uses simplified logic.
- Policy limits are predefined.
- One claim is processed at a time.

---

# 🚧 Limitations

- No OCR-based receipt extraction.
- No persistent database.
- No authentication.
- No cloud deployment.
- No real ERP integration.
- Limited sample travel policy.



AI Travel Reimbursement Approval Agent

Built using FastAPI, LangGraph, Groq Llama 3, ChromaDB, RAG, and Streamlit.
