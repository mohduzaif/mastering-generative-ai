from langchain_groq import ChatGroq
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from pydantic import BaseModel, Field

# load the env variables.
load_dotenv()

# create the model object.
# llm = HuggingFaceEndpoint(
#     repo_id = "meta-llama/Llama-3.1-8B-Instruct", 
#     task = "text-generation",
#     temperature = 0.7
# )

# model = ChatHuggingFace(llm = llm)

model = ChatGroq(
    model = 'llama-3.3-70b-versatile', 
    temperature = 0.7 
)

# define the pydantic object.
class Person(BaseModel):

    name : str = Field(description = "Name of the person.")
    age : int = Field(gt = 18, description = "Age of the persoon.")
    city : str = Field(description = "Name of the city to which person is belong.")


# create the parser object.
parser = PydanticOutputParser(pydantic_object = Person)

# create the template.
template = PromptTemplate(
    template = "Provide the name, age and city of the fictional {place} person \n{format_instruction}",
    input_variables = ['place'],
    partial_variables = {'format_instruction' : parser.get_format_instructions()}
)

# # create the prompt.
# prompt = template.invoke({
#     'place' : 'Indian'
# })
# print(prompt)

# # model calling for the result.
# result = model.invoke(prompt)

# # parse the result comes from the model for getting the structured output.
# final_result = parser.parse(result.content)

# # print the result.
# print(final_result)


# NOTE : Do all three steps using chain.

chain = template | model | parser

result = chain.invoke({
    'place' : 'Sri lankan'
})

print(result)