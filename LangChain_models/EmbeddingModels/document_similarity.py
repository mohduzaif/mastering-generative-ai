from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding_model = HuggingFaceEndpointEmbeddings(
    model = "sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers.",
    "Zaheer Khan is the bestest Indian Left-Arm fast bowler, that known for his swing bowling.",
    "Chaminda Vas Khan is the bestest World Left-Arm fast bowler, that known for his swing and reverse bowling." 
]

query = "How is the best bowler ?"

doc_embeddings = embedding_model.embed_documents(documents)
query_embedding = embedding_model.embed_query(query)

# print(type(doc_embeddings))
# print(type(query_embedding))
# print(len(doc_embeddings[0]))
# print(len(query_embedding))
# print(doc_embeddings)

# this function required the 2d list of vector thats why we pass query_embedding in list.
similarity_scores = cosine_similarity([query_embedding], doc_embeddings)

# this will convert 2D list into a 1D list.
similarity_scores = np.array(similarity_scores).flatten().tolist()
print(similarity_scores)

# find the similarity and find the maximium similarity score from them.
index, maximum_score = sorted(list(enumerate(similarity_scores)), key = lambda x : x[1])[-1]
# print(maximum_score, index)

print(query)
print(documents[index])
print("Similarity Score : ", maximum_score)