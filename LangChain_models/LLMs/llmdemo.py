from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


llm_model = OpenAI(
        model = 'gpt-3.5-turbo-instruct', 
        temperature = 0.1
    )

response = llm_model.invoke('What is the capital of india?')

print(response)
