from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel

# load the env variables. 
load_dotenv()

# create the model
model = ChatGroq(
    model = 'llama-3.3-70b-versatile', 
    temperature = 0.7 
)

# create the parser.
parser = StrOutputParser()

# create the template1. 
template1 = PromptTemplate(
    template = 'Generate the tweet about this topic, and the topic is {topic}', 
    input_variables = ['topic']
)

# create the template2. 
template2 = PromptTemplate(
    template = 'Generate the LinkedIn post about the given topic, and the topic is {topic}',
    input_variables = ['topic']
)

# create the parallel chain.
parallel_chain = RunnableParallel({
    'tweet' : RunnableSequence(template1 | model | parser), 
    'linkedin' : RunnableSequence(template2 | model | parser)
})


# trigger the parallel chain.
result = parallel_chain.invoke({
    'topic' : 'AI'
})

# print the result. 
print(result)

# print the type of result and it should be dictionary.
print(type(result))