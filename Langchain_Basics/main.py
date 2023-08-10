from langchain.agents.agent_toolkits import create_python_agent
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from utils import llm_azure

class LangChainAgent:

    def __init__(self):
        self.tools = load_tools(["llm-math", "wikipedia"], llm=llm_azure)
        self.agent = initialize_agent(
            self.tools,
            llm_azure,
            agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
            handle_parsing_errors=True,
            verbose=True
        )

    def query(self, question):
        result = self.agent(question)
        return result

if __name__ == "__main__":
    lang_chain_agent = LangChainAgent()

    question1 = "What is the 25% of 300?"
    response1 = lang_chain_agent.query(question1)
    print(response1)

    question2 = "Tom M. Mitchell is an American computer scientist \
                and the Founders University Professor at Carnegie Mellon University (CMU)\
                what book did he write?"
    response2 = lang_chain_agent.query(question2)
    print(response2)
