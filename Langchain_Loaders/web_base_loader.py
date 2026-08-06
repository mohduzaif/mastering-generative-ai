from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 

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

loader = WebBaseLoader(url)

docs = loader.load()

# create the chain.
chain = prompt | model | parser 

# trigger the chain. 
result = chain.invoke({
    'question' : 'Tell me the product name about which we are talking about ?', 
    'text' : docs[0].page_content
})

print(result)