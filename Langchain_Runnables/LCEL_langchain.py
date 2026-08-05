from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableBranch

# load the env variables. 
load_dotenv() 

# create the models. 
model = ChatGroq(
    model = 'llama-3.3-70b-versatile', 
    temperature = 0.7 
)

# create the parser. 
parser = StrOutputParser()

# create the prompt1 using PromptTemplate.
prompt = PromptTemplate(
    template = 'Write the joke on the given topic, and the topic is {topic}', 
    input_variables = ['topic']
)

chain = prompt | model | parser

result = chain.invoke({
    'topic' : 'Cricket'
})

print(result)
