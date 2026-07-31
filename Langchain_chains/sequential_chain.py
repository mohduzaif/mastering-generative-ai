from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# load the env variables.
load_dotenv()

# create the prompts.
prompt1 = PromptTemplate(
    template = "Generate the detailed report about {topic}",
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = "Generate the 5 pointer summary of the given \n{text}",
    input_variables = ['text']
)

# create the model object.
model = ChatGroq(
    model = 'llama-3.3-70b-versatile',
    temperature = 0.7 
)

# create the object of the parser.
parser = StrOutputParser()

# build the chain.
chain = prompt1 | model | parser | prompt2 | model | parser

# trigger the chain.
result = chain.invoke({
    'topic' : 'Unemployment in India.'
})

# print the result.
print(result)

# print tha chain as well.
chain.get_graph().print_ascii()

# it will also print the graph of the complete chain.
ascii_graph = chain.get_graph().draw_ascii()
print(ascii_graph)