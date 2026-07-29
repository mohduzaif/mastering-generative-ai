from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

# load the env variable.
load_dotenv()

# create the template1.
template1 = PromptTemplate(
    template = "Write the detail report about the {topic}", 
    input_variables = ["topic"] 
)

# create the template2.
template2 = PromptTemplate(
    template = "Write a 5 line summary from the text given as {text}", 
    input_variables = ["text"]
)

model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature = 0.7
)

# create the first prompt.
prompt1 = template1.invoke({'topic' : 'black hole'})

# calling the API for the resultant prompt.
result = model.invoke(prompt1)

# create the second prompt.
prompt2 = template2.invoke({'text' : result.content})

# calling the API for the final result.
result = model.invoke(prompt2)

# print the final result.
print(result.content)