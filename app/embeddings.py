from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)

from app.config import EMBEDDING_MODEL


def load_embedding_model():
    """
    Load HuggingFace embedding model
    for semantic search.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    return embeddings