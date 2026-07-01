from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


POLICY_PATH = "data/policy.md"
VECTOR_DB_PATH = "vector_db"


def get_embedding_model():
    """
    Returns the embedding model.
    """

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def create_vectorstore():
    """
    Creates the vector database from the travel policy.
    """

    print("Creating Vector Database...")

    loader = TextLoader(POLICY_PATH)

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=get_embedding_model(),
        persist_directory=VECTOR_DB_PATH
    )

    print("Vector Database Created.")

    return vectordb


def load_vectorstore():
    """
    Loads an existing vector database.
    """

    return Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=get_embedding_model()
    )


def get_vectorstore():
    """
    Automatically creates the vector database
    if it doesn't already exist.
    """

    vector_path = Path(VECTOR_DB_PATH)

    if not vector_path.exists():

        return create_vectorstore()

    return load_vectorstore()