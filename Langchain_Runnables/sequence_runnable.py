from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

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
prompt1 = PromptTemplate(
    template = 'Write the joke on the given topic, and the topic is {topic}', 
    input_variables = ['topic']
)

# create the prompt2 using PromptTemplate.
prompt2 = PromptTemplate(
    template = 'Explain the following joke - {joke}', 
    input_variables = ['joke']
)

# create the chain.
chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

result = chain.invoke({
    'topic' : 'AI'
})

print(result)