from langchain_voyageai import VoyageAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = VoyageAIEmbeddings(
    model = "voyage-3-large"
)

vector = embedding_model.embed_query("Machcine Learning...")

print(vector)