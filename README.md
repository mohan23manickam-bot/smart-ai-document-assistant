# 🤖 Smart AI Document Assistant

An intelligent AI-powered document assistant built using **Retrieval-Augmented Generation (RAG)** that allows users to upload documents and ask context-aware questions based on the uploaded content.

The system retrieves relevant document chunks using semantic search and generates grounded responses using a Large Language Model (LLM).

---

## 📌 Project Overview

Smart AI Document Assistant enables users to:

* Upload PDF or TXT documents
* Ask questions related to uploaded documents
* Retrieve relevant document context using vector similarity search
* Generate accurate context-based answers using an LLM
* Maintain conversational memory for follow-up questions
* Reduce hallucinations by grounding responses in uploaded document content

This project demonstrates practical implementation of **RAG architecture** for document understanding and question answering.

---

## 🚀 Features

✅ Upload PDF and TXT documents

✅ Document chunking for efficient retrieval

✅ Semantic search using embeddings

✅ ChromaDB vector database for document storage

✅ Context-aware question answering using LLM

✅ Conversation memory for follow-up questions

✅ Source retrieval for answer transparency

✅ Hallucination reduction using document-grounded prompting

✅ Modern ChatGPT-style frontend built with Streamlit

---

## 🏗 Architecture

```text
User Upload Document
        ↓
Document Processing
        ↓
Text Chunking
        ↓
Embedding Generation
        ↓
Vector Storage (ChromaDB)
        ↓
Semantic Retrieval
        ↓
Prompt Construction
        ↓
LLM Response Generation
        ↓
Final Answer + Source Documents
```

---

## 🛠 Tech Stack

### Programming Language

* Python

### Frontend

* Streamlit

### Frameworks & Libraries

* LangChain
* ChromaDB
* Hugging Face Transformers
* Sentence Transformers
* Groq API
* PyPDF

### Vector Database

* ChromaDB

### Embedding Model

* sentence-transformers/all-MiniLM-L6-v2

### LLM

* Groq LLM API

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
smart-ai-document-assistant/

│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── document_processor.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── prompt_template.py
│   ├── rag_chain.py
│   └── chat_memory.py
│
├── streamlit_app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone repository

```bash
git clone https://github.com/mohan23manickam-bot/smart-ai-document-assistant.git
```

Move into project folder

```bash
cd smart-ai-document-assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run application

```bash
streamlit run streamlit_app.py
```

---

## How It Works

### Step 1

Upload a PDF or TXT document.

### Step 2

The document is processed and split into smaller chunks.

### Step 3

Each chunk is converted into embeddings.

### Step 4

Embeddings are stored inside ChromaDB vector database.

### Step 5

User asks a question.

### Step 6

Retriever finds the most relevant chunks.

### Step 7

Relevant context is sent to the LLM.

### Step 8

LLM generates answer using retrieved context.

---

## Sample Use Cases

* Document Question Answering
* Resume Analysis
* Academic Notes Assistant
* Legal Document Assistant
* Research Paper Assistant
* Internal Knowledge Base Chatbot

---

## Future Improvements

* LangGraph-based intelligent routing
* General LLM fallback when document has no answer
* Document summarization feature
* OCR support for scanned documents
* Hybrid retrieval (BM25 + Semantic Search)
* Multi-agent architecture
* Public cloud deployment

---

## Skills Demonstrated

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Databases
* Prompt Engineering
* Large Language Model Integration
* Embedding Generation
* Streamlit Application Development
* Conversational AI
* Git and GitHub Workflow

---

## Author

**Jeyamohan M**

Aspiring Data Scientist | AI Engineer | Machine Learning Enthusiast

GitHub:
https://github.com/mohan23manickam-bot

---

## License

This project is created for learning and portfolio purposes.
