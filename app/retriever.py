from app.config import TOP_K_RESULTS

def retrieve_documents(vector_db, query):

    results = vector_db.similarity_search_with_score(
        query=query,
        k=TOP_K_RESULTS
    )

    return results