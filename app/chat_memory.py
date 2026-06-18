def update_chat_history(
    chat_history,
    user_query,
    assistant_response
):
    """
    Store conversation history
    for follow-up questions.
    """

    chat_history.append(
        f"User: {user_query}"
    )

    chat_history.append(
        f"Assistant: {assistant_response}"
    )

    return chat_history


def clear_chat_history():
    """
    Reset conversation memory.
    """

    return []