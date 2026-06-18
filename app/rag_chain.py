from langchain_groq import ChatGroq

from app.config import GROQ_API_KEY, LLM_MODEL
from app.retriever import retrieve_documents
from app.prompt_template import build_prompt


def ask_question(query, vector_db, chat_history):

    results = retrieve_documents(
        vector_db,
        query
    )

    docs = [doc for doc, score in results]

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # only reject if retriever returns almost nothing
    if len(context.strip()) < 50:

        return (
            "I cannot find this answer in the uploaded document.",
            []
        )

    prompt = build_prompt(
        context=context,
        query=query,
        chat_history=chat_history
    )

    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name=LLM_MODEL
    )

    response = llm.invoke(
        prompt
    )

    return response.content, docs