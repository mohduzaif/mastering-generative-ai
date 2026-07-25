from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model = 'llama-3.3-70b-versatile', 
    temperature = 0.7
)

# create the storage for chat history.
chatHistory = [
    SystemMessage(content = "You are a helpful AI assistant")
]

while True:
    user_input = input("You : ")
    chatHistory.append(HumanMessage(content = user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chatHistory)
    chatHistory.append(AIMessage(content = result.content))
    print("AI : ", result.content)

print(chatHistory)