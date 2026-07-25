from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

groq_model = ChatGroq(
    model = 'llama-3.3-70b-versatile', 
    temperature = 0.7
)

response = groq_model.invoke('How many hundreds Sachin scored in Test and ODI separately?')

print(response.content)