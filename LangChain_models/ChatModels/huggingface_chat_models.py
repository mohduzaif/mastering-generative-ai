from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct", 
    task = "text-generation", 
    max_new_tokens=256,
    temperature = 0.7
)

hf_chat_model = ChatHuggingFace(llm = llm)

response = hf_chat_model.invoke("How many hundreds scored by sachin Tendulkar in ODI and Test?")

print(response.content)