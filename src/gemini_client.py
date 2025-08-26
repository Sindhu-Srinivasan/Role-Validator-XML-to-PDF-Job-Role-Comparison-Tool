import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from config.config import GOOGLE_API_KEY
from typing import List, Union

# Configure the Gemini client with the API key
genai.configure(api_key=GOOGLE_API_KEY)

class GeminiClient:
    def __init__(self, model_name: str = "gemini-1.5-flash"):
        """Initialize the Gemini client with safety settings."""
        self.model = genai.GenerativeModel(
            model_name,
            safety_settings={
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
            }
        )

    def generate_text(self, prompt: str) -> str:
        """Generates text using the Gemini model."""
        try:
            response = self.model.generate_content(prompt)
            if response.text:
                return response.text
            return ""
        except Exception as e:
            print(f"Error generating text with Gemini: {e}")
            return ""

    def embed_text(self, text: str) -> List[float]:
        """Generates embeddings for the given text using Google's embedding model."""
        try:
            # Using the new embedding model name for Gemini 1.5
            result = genai.embed_content(
                model="models/embedding-001",
                content=text,
                task_type="retrieval_document"
            )
            if result and 'embedding' in result:
                return result['embedding']
            return []
        except Exception as e:
            print(f"Error generating embedding: {e}")
            return []

    def batch_embed_texts(self, texts: List[str]) -> List[List[float]]:
        """Generates embeddings for multiple texts at once."""
        try:
            results = genai.embed_content(
                model="models/embedding-001",
                content=texts,
                task_type="retrieval_document"
            )
            if results and 'embedding' in results:
                return results['embedding']
            return []
        except Exception as e:
            print(f"Error generating batch embeddings: {e}")
            return []