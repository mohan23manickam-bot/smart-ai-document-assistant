import os
from dotenv import load_dotenv

load_dotenv()

# API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Models
LLM_MODEL = "llama-3.1-8b-instant"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Chunking settings
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Retrieval
TOP_K_RESULTS = 3

SIMILARITY_THRESHOLD = 0.35