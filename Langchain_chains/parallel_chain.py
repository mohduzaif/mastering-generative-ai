from langchain_cohere import ChatCohere
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

# load the env variables.
load_dotenv()

# create the prompt.

# prompt1 for generate the notes from the text.
prompt1 = PromptTemplate(
    template = "Generate the short notes from the given text, and the text is {text}",
    input_variables = ['text']
)

# prompt2 for generate the quiz from the text.
prompt2 = PromptTemplate(
    template = "Generate the 7-8 Quiz type question from the given text, and the text is {text}", 
    input_variables = ['text']
)

# create the prompt for merge both short notes and Quiz.
prompt3 = PromptTemplate(
    template = "Merge both of them notes as well as quiz into a single document. \nNotes -> {notes} and \nQuiz -> {quiz}",
    input_variables = ['notes', 'quiz'] 
)

# create the first model.
# groq_model = ChatGroq(
#     model = 'llama-3.3-70b-versatile',
#     temperature = 0.7 
# )

# create the second model.
groq_model = ChatGroq(
    model = 'llama-3.3-70b-versatile',
    temperature = 0.7 
)

# create the parser object.
parser = StrOutputParser()

# build the parallel chain, here the variable name remain same as we mentioned in the prompt.
parallel_chain = RunnableParallel({
    'notes' : prompt1 | groq_model | parser,
    'quiz' : prompt2 | groq_model | parser
})

# build the merge chain.
merge_chain = prompt3 | groq_model | parser

# now build the final chain.
chain = parallel_chain | merge_chain

# text 
text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

# trigger the chain.
result = chain.invoke({
    'text' : text
})

# print the result. 
print(result)

# print the complete chain.
chain.get_graph().print_ascii()