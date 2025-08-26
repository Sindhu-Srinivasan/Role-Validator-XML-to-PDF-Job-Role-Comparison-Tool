import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")

def test_api():
    try:
        # Configure the API
        genai.configure(api_key=API_KEY)
        
        # Initialize the model
        model = genai.GenerativeModel('gemini-pro')
        
        # Make a simple request
        response = model.generate_content("What is 1+1?")
        
        # Print the response
        print("API Response:", response.text)
        print("✅ API key is working!")
        return True
    except Exception as e:
        print("❌ API Error:", str(e))
        return False

if __name__ == "__main__":
    test_api()
