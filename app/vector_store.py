from langchain_community.vectorstores import (
    Chroma
)

from app.embeddings import (
    load_embedding_model
)


def create_vector_store(chunks):
    """
    Create Chroma vector database
    from document chunks.
    """

    embedding_model = load_embedding_model()

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    return vector_db