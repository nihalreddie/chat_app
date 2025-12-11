import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_classic.prompts import  PromptTemplate
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import LLMChain
import streamlit as st


class Model:
    
    def __init__(self,gender):
        load_dotenv()
        groq_api = os.getenv("GROQ_API_KEY")
    
        llm = ChatGroq(
            api_key = groq_api,
            model =   "openai/gpt-oss-20b",
            temperature=1.7,
            max_tokens= 512
        )

        
        template = f" act as your a {gender}"+""" and 
                reply to the  coversation with in context  under 30 words

                {history}
                Human:{input}
                Maya:
                """
    
        prompt = PromptTemplate(
            input_variables=[gender,'input'],
            template=template
        )
        
        self.memory = ConversationBufferMemory(
            return_messages=True,
            memory_key="history"
        )
        
        self.chain = LLMChain(
            llm=llm,
            memory=self.memory,
            prompt=prompt
        ) 
        
        
    def get_response(self,inputt):
        resp = self.chain.predict(input=inputt)
        
    
    def display_history(self):
        li=[]
        for i in self.memory.chat_memory.messages:
            li.append(i.content)
        return li

_instance = None

def get_instance(gender):
    global _instance
    if _instance is None:
        _instance = Model(gender)
    return _instance

def clear_instance():
    global _instance
    _instance = None


