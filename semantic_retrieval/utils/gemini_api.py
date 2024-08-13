from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Now fetch the API key
api_key = os.getenv('GENAI_API_KEY')

# Ensure you configure your API client with the API key
genai.configure(api_key=api_key)

# The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts
model = genai.GenerativeModel('gemini-1.5-flash')

def gemini_api():
    return model
