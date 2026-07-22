from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv

load_dotenv()


embedding_model = CohereEmbeddings(
    model = "embed-english-v3.0", 
)

document = [
    "Watching Cricket Match at Lords is Amazing", 
    "Sachin Scored hundred at Lords", 
    "India Chase the highest total at Lords"
]

# vector = embedding_model.embed_query("Generative Ai is next big thing..")
vector = embedding_model.embed_documents(document)

print(vector)
print(len(vector))
print(len(vector[0]))
print(type(vector))