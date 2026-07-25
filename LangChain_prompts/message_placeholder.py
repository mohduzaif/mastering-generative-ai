from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


# create the chat template.
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'), 
    MessagesPlaceholder(variable_name = 'chat_history'),
    ('human', '{query}')
])

# load the chat history.
chat_history = []
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

# print(chat_history)

# create the template.
prompt = chat_template.invoke({
    'chat_history' : chat_history, 
    'query' : 'Where is my refunded amount?'
})

print(prompt)