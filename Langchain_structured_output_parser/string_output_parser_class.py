from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


# load the env variables.
load_dotenv()

# create the model object.
model = ChatGroq(
    model = 'llama-3.3-70b-versatile', 
    temperature = 0.7 
)

# create the template1 for generating the detailed report.
template1 = PromptTemplate(
    template = "Write the detail report about the {topic}", 
    input_variables = ["topic"] 
)

# create the template2 for creating 5 line summary.
template2 = PromptTemplate(
    template = "Write a 5 line summary from the text given as {text}", 
    input_variables = ["text"]
)

str_output_parser = StrOutputParser()

chain = template1 | model | str_output_parser | template2 | model | str_output_parser

result = chain.invoke({
    'topic' : 'black hole'
})

print(result)