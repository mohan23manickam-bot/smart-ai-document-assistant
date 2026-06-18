def build_prompt(context, query, chat_history):

    history = "\n".join(chat_history)

    prompt = f"""
You are an AI Document Assistant.

IMPORTANT RULES:

1. Answer ONLY from DOCUMENT CONTEXT.

2. If answer is not available in document context,
respond exactly:

"I cannot find this answer in the uploaded document."

3. Never use outside knowledge.

4. Never guess.

DOCUMENT CONTEXT:
{context}

CHAT HISTORY:
{history}

QUESTION:
{query}

ANSWER:
"""

    return prompt