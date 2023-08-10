from langchain.agents.agent_toolkits import create_python_agent
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from utils import llm_azure

tools = load_tools(["llm-math","wikipedia"], llm=llm_azure)

agent= initialize_agent(
    tools, 
    llm_azure, 
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose = True)

print(agent("What is the 25% of 300?"))


result = agent("Tom M. Mitchell is an American computer scientist \
and the Founders University Professor at Carnegie Mellon University (CMU)\
what book did he write?")
print(result) 