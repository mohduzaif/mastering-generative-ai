from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct", 
    task = "text-generation",
    temperature = 0.7
)

model = ChatHuggingFace(llm = llm)

template = PromptTemplate.from_template(
    """
        Translate the given sentence to {language} language
        Given sentence is {sentence}

    """
)

prompt = template.invoke(
    {
        "language" : "Hindi", 
        "sentence" : "I Love Cricket alot."
    }
)

result = model.invoke(prompt)

print(result.content)
