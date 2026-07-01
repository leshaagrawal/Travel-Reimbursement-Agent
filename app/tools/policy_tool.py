from app.vectorstore import get_vectorstore

# Load vector database once
vector_db = get_vectorstore()


def get_policy_context(query: str) -> str:
    """
    Retrieve relevant policy text from ChromaDB.
    """

    retriever = vector_db.as_retriever(
        search_kwargs={"k": 2}
    )

    docs = retriever.invoke(query)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    return context