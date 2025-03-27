import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ['GEMINI_API_KEY']
PORT = os.environ['PORT']