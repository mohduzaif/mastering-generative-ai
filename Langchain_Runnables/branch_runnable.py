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
prompt1 = PromptTemplate(
    template = 'Write the report on the given topic, and the topic is {topic}', 
    input_variables = ['topic']
)

# create the prompt1 using PromptTemplate.
prompt2 = PromptTemplate(
    template = 'Write the summary on the given text, and the text is {text}', 
    input_variables = ['text']
)


# create the report generated chain.
report_gen_chain = RunnableSequence(prompt1, model, parser)

# generate the branch related chain.
branch_chain = RunnableBranch(
    (lambda x : len(x.split()) > 200, RunnableSequence(prompt2, model, parser)),
    (RunnablePassthrough())
)

# merge both the chains to create final chain.
final_chain = RunnableSequence(report_gen_chain, branch_chain)

# generate the result.
result = final_chain.invoke({
    'topic' : 'Russia VS Ukrain'
})

# print the result.
print(result)