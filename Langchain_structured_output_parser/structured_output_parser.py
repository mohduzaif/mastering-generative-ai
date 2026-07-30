# from langchain_groq import ChatGroq
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser


# from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# # load the env variables.
# load_dotenv()

# # create the model object.
# llm = HuggingFaceEndpoint(
#     repo_id = "meta-llama/Llama-3.1-8B-Instruct", 
#     task = "text-generation",
#     temperature = 0.7
# )

# model = ChatHuggingFace(llm = llm)

# create the parser object.


# NOTE : `This parser is deprictated from the latest version of the LANGCHAIN.`