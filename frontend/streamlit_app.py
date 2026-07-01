import streamlit as st

from api_client import submit_claim
from styles import load_css

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Travel Reimbursement Approval Agent",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(load_css(), unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""
<div class="title">
✈️ Travel Reimbursement Approval Agent
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Enterprise AI Powered Travel Reimbursement Verification
<br>
FastAPI • LangGraph • Groq LLM • ChromaDB • Streamlit
</div>
""", unsafe_allow_html=True)

st.success("🟢 AI Agent Ready")

st.divider()

# ==========================================================
# MAIN LAYOUT
# ==========================================================

left, right = st.columns([3, 2])

# ==========================================================
# LEFT PANEL
# ==========================================================

with left:

    st.header("📝 Employee Claim Form")

    claim_id = st.text_input(
        "Claim ID",
        value="CLM001"
    )

    employee_id = st.text_input(
        "Employee ID",
        value="EMP001"
    )

    employee_name = st.text_input(
        "Employee Name",
        value="Rahul Sharma"
    )

    trip_id = st.text_input(
        "Trip ID",
        value="TRIP001"
    )

    st.divider()

    st.subheader("💳 Expense Details")

    categories = [
        "Hotel",
        "Food",
        "Taxi",
        "Flight",
        "Train",
        "Other"
    ]

    num_expenses = st.number_input(
        "Number of Expenses",
        min_value=1,
        max_value=10,
        value=3,
        step=1
    )

    expenses = []

    total_amount = 0.0

        # ==========================================================
    # DYNAMIC EXPENSE FORM
    # ==========================================================

    for i in range(num_expenses):

        with st.container():

            st.markdown(f"### 💳 Expense #{i+1}")

            col1, col2 = st.columns(2)

            with col1:

                category = st.selectbox(
                    "Category",
                    categories,
                    key=f"category_{i}"
                )

                vendor = st.text_input(
                    "Vendor",
                    key=f"vendor_{i}"
                )

            with col2:

                amount = st.number_input(
                    "Amount (₹)",
                    min_value=0.0,
                    step=100.0,
                    key=f"amount_{i}"
                )
            receipt_attached = st.checkbox(
                    "Receipt Attached",
                    value=True,
                    key=f"receipt_{i}"
                    )

            receipt_name = "Receipt Uploaded" if receipt_attached else ""

            expenses.append(
                {
                    "category": category,
                    "vendor": vendor,
                    "amount": amount,
                    "receipt_attached": receipt_attached,
                    "receipt_name": receipt_name
                }
            )

            total_amount += amount

            st.divider()

    # ==========================================================
    # TOTAL CLAIM
    # ==========================================================

    st.metric(
        "💰 Total Claim Amount",
        f"₹ {total_amount:,.2f}"
    )

    submit = st.button(
        "🚀 Submit Claim",
        use_container_width=True,
        type="primary",
        key="submit_claim"
    )

# ==========================================================
# API CALL
# ==========================================================

if submit:

    claim = {

        "claim_id": claim_id,
        "employee_id": employee_id,
        "employee_name": employee_name,
        "trip_id": trip_id,
        "total_amount": total_amount,
        "expenses": expenses
    }

    with st.spinner("🤖 AI Agent is analysing your reimbursement claim..."):

        result = submit_claim(claim)

    st.session_state["result"] = result

    # ==========================================================
# RIGHT PANEL
# ==========================================================

with right:

    st.header("🤖 AI Decision Dashboard")

    st.caption("Powered by Groq LLM + LangGraph Workflow")

    if "result" not in st.session_state:

        st.info(
            "👈 Fill the claim details and click **Submit Claim** to let the AI evaluate it."
        )

    else:

        result = st.session_state["result"]

        if "error" in result:

            st.error(result["error"])

        else:

            decision = result.get("decision", "Manual Review")

            # ==================================================
            # DECISION STATUS
            # ==================================================

            if decision.lower() == "approved":

                st.success("🟢 CLAIM APPROVED")

            elif decision.lower() == "rejected":

                st.error("🔴 CLAIM REJECTED")

            elif decision.lower() == "partially approved":

                st.warning("🟡 PARTIALLY APPROVED")

            else:

                st.info("🟠 MANUAL REVIEW")

            st.divider()

            # ==================================================
            # FINANCIAL SUMMARY
            # ==================================================

            st.subheader("💰 Financial Summary")

            c1, c2 = st.columns(2)

            with c1:

                st.metric(
                    "Approved Amount",
                    f"₹ {result.get('approved_amount', 0):,.2f}"
                )

            with c2:

                st.metric(
                    "Deduction",
                    f"₹ {result.get('deduction', 0):,.2f}"
                )

            st.divider()

            # ==================================================
            # AI CONFIDENCE
            # ==================================================

            confidence = float(result.get("confidence", 0))

            st.subheader("🎯 AI Confidence")

            st.progress(confidence)

            st.write(f"### {confidence * 100:.1f}%")

            st.divider()

            # ==================================================
            # POLICY REFERENCES
            # ==================================================

            st.subheader("📚 Policy References")

            policy = result.get("policy_reference", "")

            if policy:

                st.info(policy)

            else:

                st.warning("No policy references returned.")

            st.divider()

            # ==================================================
            # MISSING DOCUMENTS
            # ==================================================

            st.subheader("📄 Missing Documents")

            docs = result.get("missing_documents", [])

            if docs:

                for doc in docs:

                    st.warning(f"⚠ {doc}")

            else:

                st.success("✅ No Missing Documents")

            st.divider()

            # ==================================================
            # AI EXPLANATION
            # ==================================================

            st.subheader("📝 AI Explanation")

            st.write(
                result.get(
                    "explanation",
                    "No explanation available."
                )
            )

            st.divider()

            # ==================================================
            # RAW JSON
            # ==================================================

            with st.expander("📦 Raw API Response"):

                st.json(result)

# ==========================================================
# AI WORKFLOW TIMELINE
# ==========================================================

            st.divider()

            st.subheader("🛠 AI Workflow Execution")

            timeline = [
                "📄 Travel Policy Retrieved using ChromaDB",
                "🧾 Receipt Validation Completed",
                "🔍 Duplicate Claim Check Completed",
                "💰 Expense Limit Validation Completed",
                "👨‍💼 Approval Matrix Evaluated",
                "🤖 Groq LLM Generated Final Decision"
            ]

            for step in timeline:
                st.success(step)

            st.divider()

            # ==================================================
            # AUDIT TRAIL (Optional)
            # ==================================================

            if "audit_trail" in result:

                st.subheader("📜 Audit Trail")

                for item in result["audit_trail"]:

                    st.info(item)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("✈️ Travel AI Agent")

    st.markdown("---")

    st.subheader("🧠 Technology Stack")

    st.success("✅ FastAPI")
    st.success("✅ LangGraph")
    st.success("✅ Groq LLM")
    st.success("✅ ChromaDB")
    st.success("✅ Streamlit")
    st.success("✅ Python")

    st.markdown("---")

    st.subheader("⚙ AI Workflow")

    st.write("1️⃣ Retrieve Company Policy (RAG)")
    st.write("2️⃣ Validate Receipts")
    st.write("3️⃣ Check Duplicate Claims")
    st.write("4️⃣ Validate Expense Limits")
    st.write("5️⃣ Determine Approval Level")
    st.write("6️⃣ LLM Decision Generation")

    st.markdown("---")

    st.subheader("✨ Features")

    st.info("✔ Retrieval-Augmented Generation (RAG)")
    st.info("✔ AI Decision Making")
    st.info("✔ Duplicate Detection")
    st.info("✔ Receipt Verification")
    st.info("✔ Expense Limit Validation")
    st.info("✔ Approval Matrix")
    st.info("✔ Confidence Score")
    st.info("✔ Explainable AI Decisions")

    st.markdown("---")

    st.caption("Developed for AI Travel Reimbursement Assignment")