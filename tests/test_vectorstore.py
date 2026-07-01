from app.vectorstore import (
    get_embedding_model,
    create_vectorstore,
    load_vectorstore,
    get_vectorstore,
)


def test_embedding_model():
    embedding = get_embedding_model()

    assert embedding is not None


def test_vectorstore_load():
    db = get_vectorstore()

    assert db is not None