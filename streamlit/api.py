import streamlit as st
import pandas as pd
from langchain.llms import OpenAI
import pandas as pd
from langchain.agents import create_csv_agent
from langchain.agents.agent_types import AgentType 
import os
os.environ["OPENAI_API_KEY"] = st.secrets['path']


st.title('hi')

agent = create_csv_agent(
    OpenAI(temperature=0 , 	model_name="gpt-4"),
    "newTEX.csv",
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)


inp = st.text_input('enter a cars-related search query')

b= st.button('GOO')

if b:
    a = agent.run(inp)
    st.text_area('output' , a)