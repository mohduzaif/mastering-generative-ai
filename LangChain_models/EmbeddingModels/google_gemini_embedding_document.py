from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(
    model = "gemini-embedding-001", 
    output_dimensionality = 32
)

document = [
    "Hey everyone, My name is Smith", 
    "I belong to Australia",
    "I am a Cricketer and also represent my country in other sports also"
]

vector = embedding_model.embed_documents(document)

print(vector)

