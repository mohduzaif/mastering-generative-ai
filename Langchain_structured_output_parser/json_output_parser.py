from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# load the env variable.
load_dotenv()

# create the model object.
model = ChatGroq(
    model = 'llama-3.3-70b-versatile', 
    temperature = 0.7 
)

# create the parser.
parser = JsonOutputParser()

# create the template.
template = PromptTemplate(
    template = 'Write the name, age and qualification of any romantic writer \n{format_instruction}',
    input_variables = [],
    partial_variables = {'format_instruction' : parser.get_format_instructions()}
)


# We can merge these three code lines using chain.
# # create the prompt.
# prompt = template.format()

# # get the result.
# result = model.invoke(prompt)

# # parse the result.
# final_result = parser.parse(result.content)

chain = template | model | parser

final_result = chain.invoke({})

print(final_result)
print(type(final_result))

