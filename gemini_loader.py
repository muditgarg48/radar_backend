from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from env_loader import API_KEY

def get_embedding_function():
    embedding_function = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", google_api_key=API_KEY)
    # print(embedding_function)
    return embedding_function

def get_chat_model():
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")
    return model