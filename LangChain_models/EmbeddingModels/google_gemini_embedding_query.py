from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(
    model = "gemini-embedding-001", 
    output_dimensionality = 32
)

vector = embedding_model.embed_query("Machine Learning")

print(vector)

