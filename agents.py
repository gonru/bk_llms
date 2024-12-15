import os

import streamlit as st
from langchain.agents import initialize_agent, AgentType
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_openai import OpenAI

os.environ["OPENAI_API_KEY"] = st.secrets["API_KEY"]

llm = OpenAI(temperature=0.0)

tools = load_tools(['wikipedia', 'llm-math'], llm)
agent = initialize_agent(tools, llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

prompt = input('Input Wikipedia Research Task\n')
agent.run(prompt)