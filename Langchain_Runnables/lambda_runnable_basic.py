from langchain_core.runnables import RunnableLambda

def count_words(text):
    word_list = text.split()
    return len(word_list)

runnable_count_fun = RunnableLambda(count_words)

count = runnable_count_fun.invoke("Hi, How are you ?")

print(count)