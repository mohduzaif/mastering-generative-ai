from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

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

# create the function that use to count the words in the given text.
def word_counter(text):
    word_list = text.split()
    count = len(word_list)

    return count

# convert the word_counter into a runnable using RunnableLambda.
word_count_runnable = RunnableLambda(word_counter)

# build a chain that generate the joke.
joke_gen_chain = RunnableSequence(prompt, model, parser)

# build a parallel chain. 
parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(), 
    'word_count' : word_count_runnable
})

# merge both the chain. 
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

# trigger the final chain.
result = final_chain.invoke({
    'topic' : 'AI'
})


# final result.
final_result = """{} \nWord count - {}""".format(result['joke'], result['word_count'])

# print the result
print(final_result)