from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableBranch, RunnableLambda

from dotenv import load_dotenv

# load the env variables.
load_dotenv()

# create the model object.
groq_model = ChatGroq(
    model = 'llama-3.3-70b-versatile',
    temperature = 0.7 
)

# create the parser.
parser = StrOutputParser()

# create the pydantic object.
class Feedback(BaseModel):
    sentiment : Literal['positive', 'negative'] = Field(description = "Generate the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object = Feedback)

# create the first prompt.
prompt1 = PromptTemplate(
    template = "Give the sentiment as positve or negative from the given feedback\n{feedback} \n {format_instruction}",
    input_variables = ['feedback'], 
    partial_variables = {
        'format_instruction' : parser2.get_format_instructions()
    }
)

classifier_chain = prompt1 | groq_model | parser2

# result = classifier_chain.invoke({
#     'feedback' : 'This is smartphone is worst from the entire series.'
# })

# print(result)

# generate the prompt2.
prompt2 = PromptTemplate(
    template = "Write an appropriate response to the positive feedback \n{feedback}"
)

# generate the prompt3.
prompt3 = PromptTemplate(
    template = "Write an appropriate response to the negative feedback \n{feedback}"
)

# build the branch chain.
branch_chain = RunnableBranch(
    (lambda x : x.sentiment == 'positive', prompt2 | groq_model | parser),
    (lambda x : x.sentiment == 'negative', prompt3 | groq_model | parser), 
    (RunnableLambda(lambda x: "could not find sentiment"))
)

# merge both chains to build final chain.
final_chain = classifier_chain | branch_chain

result = final_chain.invoke({
    'feedback' : "This is smartphone is most beautiful from the entire series."
})

print(result)