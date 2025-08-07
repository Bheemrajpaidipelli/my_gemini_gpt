import os
from dotenv import load_dotenv

# Load from .env file
load_dotenv()

# Fetch API key from environment
API_KEY = os.getenv("GEMINI_API_KEY")
