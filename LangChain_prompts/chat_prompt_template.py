from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


# this is not working properly in Langchain this is a wierd behavior of langchain.

# chat_template = ChatPromptTemplate([
#     SystemMessage(content = "You are a helpful {domain} expert"), 
#     HumanMessage(content = "Explain me in simple words, what is {topic}")
# ])

# how er write the above code, now it will work fine.
chat_template = ChatPromptTemplate([
    ('system' , 'You are a great {domain} expert'), 
    ('human' , 'Explain me in simple words, what is {topic}')
])

prompt = chat_template.invoke({
    'domain' : 'cricket', 
    'topic' : 'Dusra'
})

print(prompt)

