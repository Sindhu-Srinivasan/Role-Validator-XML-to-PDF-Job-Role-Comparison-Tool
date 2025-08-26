import os
from dotenv import load_dotenv

load_dotenv()

# --- Google Gemini API Key ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("No Google API key found. Please set GOOGLE_API_KEY or GEMINI_API_KEY in your .env file")
print("GOOGLE_API_KEY found:", GOOGLE_API_KEY)

# --- Pinecone Configuration ---
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
if not PINECONE_API_KEY:
    raise ValueError("No Pinecone API key found. Please set PINECONE_API_KEY in your .env file")

PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "role-comparison-index")

# IMPORTANT: Pinecone environment value must match Pinecone's expected regions (e.g., "us-east1-gcp" or "us-east-1")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT", "us-east-1")
PINECONE_CLOUD = os.getenv("PINECONE_CLOUD", "aws")

# --- Other Configs ---
PDF_CHUNK_SIZE = int(os.getenv("PDF_CHUNK_SIZE", 1000))
PDF_CHUNK_OVERLAP = int(os.getenv("PDF_CHUNK_OVERLAP", 100))
ROLE_EXTRACTION_PROMPT = os.getenv(
    "ROLE_EXTRACTION_PROMPT",
    "List all the job roles or titles mentioned in the following document. "
    "Provide a comma-separated list of unique roles. If no roles are found, respond with 'None'."
)
FUZZY_MATCH_THRESHOLD = int(os.getenv("FUZZY_MATCH_THRESHOLD", 80))