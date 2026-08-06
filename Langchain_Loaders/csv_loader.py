from langchain_community.document_loaders import CSVLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableLambda

# load the env variables. 
load_dotenv() 

# create 
prompt = PromptTemplate(
    template = 'Give the answer of the following question - {question} \n on the basis of given text - {text}', 
    input_variables = ['question', 'text']
)


# create the models. 
model = ChatGroq(
    model = 'llama-3.3-70b-versatile', 
    temperature = 0.7 
)


# create the parser. 
parser = StrOutputParser()

url = 'https://www.amazon.com/Apple-2026-MacBook-13-inch-Laptop/dp/B0GR1BY1SZ?th=1'

loader = CSVLoader('Social_Network_Ads.csv')

docs = loader.load()

# print(len(docs))
# print(docs[0])

# create the chain.
chain = prompt | model | parser 

# function to get all page content.
def page_content_from_docs():
    content = []
    for document in docs:
        content.append(document.page_content)
    return content

# trigger the chain. 
result = chain.invoke({
    'question' : 'Tell me the Age of the person that has a highest salary ?', 
    'text' : RunnableLambda(page_content_from_docs)
})

print(result)