from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

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

# create joke generation chain.
joke_gen_chain = RunnableSequence(prompt1, model, parser)

# create the parallel chain for generating explaination and persisting the joke as it is.
parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(), 
    'explaination' : RunnableSequence(prompt2, model, parser)
})

# merge both the chain for creating the complete chain. 
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

# trigger the final_chain.
result = final_chain.invoke({
    'topic' : 'AI'
})

# print the type of result.
print(type(result))

# print the result.
print(result)