from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpointEmbeddings

load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

document = [
    "Machine Learning", 
    "Deep Learning", 
    "Generative AI", 
    "Agentic AI"
]

vector = embeddings.embed_documents(document)

print(len(vector))
print(vector)
