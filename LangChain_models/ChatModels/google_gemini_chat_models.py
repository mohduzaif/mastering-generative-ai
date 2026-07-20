from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

google_gemini_chat_model = ChatGoogleGenerativeAI(
        model = 'gemini-3.5-flash', 
        temperature = 0.7
    )

response = google_gemini_chat_model.invoke("Gives me brief introduction about Machine Learning.")

print(response.text)