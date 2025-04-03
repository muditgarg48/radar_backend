import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ['GEMINI_API_KEY']
PORT = os.environ['PORT']
LOGO_CLIENT_ID = os.environ['LOGO_CLIENT_ID']

def get_client_id():
    return LOGO_CLIENT_ID