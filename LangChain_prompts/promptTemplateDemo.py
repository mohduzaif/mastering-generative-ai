from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash"
)

template = PromptTemplate.from_template(
    """
        Translate the given sentence
        Language : {language}
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

print(result.content[0]['text'])
