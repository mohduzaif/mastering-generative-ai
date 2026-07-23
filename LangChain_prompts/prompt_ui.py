from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv

import streamlit as st
import time

# load the environement variables.
load_dotenv()

# create the object of the LLM model.
llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct", 
    task = "text-generation",
    temperature = 0.7
)

hf_chat_model = ChatHuggingFace(llm = llm)


# set the header on the frontend.
st.header('Reasearch Tool')


# create the input placeholders for the user input.

# paper input.
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

# style_input
style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

# length_input
length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# load the template from another file.
template = load_prompt("template.json")

prompt = template.invoke({
        'paper_input' : paper_input, 
        'style_input' : style_input,
        'length_input' : length_input
    })

# create the button.
if st.button("Summarize"):
    for attempt in range(3):
        try:
            result = hf_chat_model.invoke(prompt)
            st.write(result.content)
            break

        except Exception as e:
            if attempt < 2:
                st.warning("Model is busy. Retrying...")
                time.sleep(5)
            else:
                st.error(e)