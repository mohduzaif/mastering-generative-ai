from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


# load the env variables.
load_dotenv()

# creeate the model object.
model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature = 0.7
)

# create the object of parser.
parser = StrOutputParser()

template = PromptTemplate(
    template = "Explain 5 points about the {topic}",
    input_variables = ['topic']
)

chain = template | model | parser


result = chain.invoke({
    'topic' : 'black hole'
})

# print the result that are comes from LLM.
print(result)

# we can print the chain as well.
chain.get_graph().print_ascii()