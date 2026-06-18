import streamlit as st
import time

from app.document_processor import process_uploaded_files
from app.chunking import split_documents
from app.vector_store import create_vector_store
from app.rag_chain import ask_question
from app.chat_memory import update_chat_history, clear_chat_history


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="RAG Document Assistant",
    page_icon="🤖",
    layout="wide"
)


# ---------------------------------------------------
# CSS (ChatGPT Style)
# ---------------------------------------------------

st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #212121;
}

/* Main container */
.block-container {
    max-width: 900px;
    padding-top: 2rem;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 700;
    color: white;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #d1d5db;
    margin-bottom: 30px;
    font-size: 18px;
}

/* Chat message */
[data-testid="stChatMessage"] {
    background-color: #2f2f2f !important;
    border-radius: 15px;
    padding: 15px;
    margin-bottom: 10px;
}

/* Chat text */
[data-testid="stMarkdownContainer"] p {
    color: white !important;
    font-size: 17px;
    line-height: 1.7;
}

/* Chat input */
[data-testid="stChatInput"] {
    background-color: #2f2f2f !important;
    border-radius: 20px !important;
    border: 1px solid #444 !important;
}

/* Buttons */
.stButton>button {
    background-color: #10A37F;
    color: white;
    border-radius: 12px;
    border: none;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "vector_db" not in st.session_state:
    st.session_state.vector_db = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    "<div class='main-title'>🤖 RAG Document Assistant</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Upload documents and chat with your knowledge base</div>",
    unsafe_allow_html=True
)


# ---------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------

uploaded_files = st.file_uploader(
    "Upload PDF or TXT Files",
    type=["pdf", "txt"],
    accept_multiple_files=True
)

if uploaded_files:

    with st.spinner("Processing documents..."):

        docs = process_uploaded_files(
            uploaded_files
        )

        chunks = split_documents(
            docs
        )

        vector_db = create_vector_store(
            chunks
        )

        st.session_state.vector_db = vector_db

    st.success("Documents ready for chat ✅")


# ---------------------------------------------------
# CLEAR CHAT BUTTON
# ---------------------------------------------------

col1, col2 = st.columns([8, 1])

with col2:

    if st.button("🗑"):

        st.session_state.messages = []

        st.session_state.chat_history = clear_chat_history()

        st.rerun()


# ---------------------------------------------------
# DISPLAY OLD CHAT
# ---------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )


# ---------------------------------------------------
# CHAT INPUT
# ---------------------------------------------------

if st.session_state.vector_db:

    user_query = st.chat_input(
        "Message IntelliDocs AI..."
    )

    if user_query:

        # ---------------- USER MESSAGE ----------------

        user_message = {
            "role": "user",
            "content": user_query
        }

        st.session_state.messages.append(
            user_message
        )

        with st.chat_message("user"):

            st.write(user_query)

        # ---------------- AI RESPONSE ----------------

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                start = time.time()

                answer, docs = ask_question(
                    query=user_query,
                    vector_db=st.session_state.vector_db,
                    chat_history=st.session_state.chat_history
                )

                end = time.time()

            # if question unrelated to document
            if "could not find" in answer.lower():

                st.warning(
                    answer
                )

            else:

                st.write(
                    answer
                )

                st.caption(
                    f"⏱ Response Time: {round(end-start,2)} sec"
                )

                # source viewer
                with st.expander("📎 View Sources"):

                    for i, doc in enumerate(docs):

                        st.markdown(
                            f"**Source {i+1}**"
                        )

                        st.write(
                            doc.metadata
                        )

                        st.write(
                            doc.page_content[:400]
                        )

                        st.divider()

        # save assistant message
        assistant_message = {
            "role": "assistant",
            "content": answer
        }

        st.session_state.messages.append(
            assistant_message
        )

        # update memory
        st.session_state.chat_history = update_chat_history(
            st.session_state.chat_history,
            user_query,
            answer
        )


else:

    st.info(
        "Upload a document to start chatting."
    )