from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# load the env variables.
load_dotenv()

# model creation.
model = ChatGroq(
    model = 'llama-3.3-70b-versatile', 
    temperature = 0.7 
)

# parser creation.
parser = StrOutputParser()

# create the prompt.
prompt = PromptTemplate(
    template = 'Write the summary of the following text - \n{text}', 
    input_variables = ['text']
)

# create the textLoader object.
loader = TextLoader('cricket.txt', encoding = 'utf-8', autodetect_encoding = True)

# load the document.
docs = loader.load()

# create the chain.
chain = prompt | model | parser

# trigger the chain.
result = chain.invoke({
    'text' : docs[0].page_content
})

# print the result.
print(result)

# print the document.
# print(docs)

# print the type of the docs.
# print('The type of the document object : ', type(docs))

# print the len of the document.
# print('The length of the list of document', len(docs))

# we can use the indexing here because it is a list of python.
# print(docs[0])

# print(type(docs[0]))

# print(docs[0].metadata)
# print(docs[0].page_content)