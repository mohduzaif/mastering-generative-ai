from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model = "llama-3.3-70b-versatile", 
    temperature = 0.7
)

messages = [
    SystemMessage(content = "You are a helpful AI assistant"),
    HumanMessage(content = "Explain me about yourself")
]

result = model.invoke(messages)
messages.append(AIMessage(content = result.content))
print(messages)