from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os

from dotenv import load_dotenv
load_dotenv()
###load the langchian key
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']="true"
os.environ['LANGCHAIN_PROJECT']='simple Q AND A chatbot'


prompt=ChatPromptTemplate.from_messages(
    [
        ('system','You are a simple Q and A Chatbot'),
        ('user','Question:{question}')
    ]
)

def generate_response(question,engine):

    llm=Ollama(model=engine)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

##streamlit app
engine=st.sidebar.selectbox('select a model',['llama2'])

##main interface for user input
st.write('Go Ahead and ask your question')
user_input=st.text_input('You:')

if user_input:
    response=generate_response(user_input,engine)
    st.write('response',response)

else:
    st.write('Please provide user input')

