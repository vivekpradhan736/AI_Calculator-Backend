from dotenv import load_dotenv
import os
load_dotenv()

SERVER_URL = 'localhost'
PORT = os.getenv("PORT", "8000")
ENV = 'prod'

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")