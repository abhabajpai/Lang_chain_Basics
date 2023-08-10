from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationBufferWindowMemory
from langchain.memory import ConversationTokenBufferMemory
from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage
)
from utils import llm_azure

class ConversationClass:

    def create_conversation(self,memory):
        conversation=ConversationChain(
        llm=llm_azure,
        memory=memory,
        verbose=True
        )
        return conversation
    
    def run_conversation(self,create_conversation,input1):
        print(create_conversation.predict(input=input1))
        

if __name__ == "__main__":
    conversation_object=ConversationClass()
    memory1=ConversationBufferMemory()
    conversation=conversation_object.create_conversation(memory1)
    conversation_object.run_conversation(conversation,"my name is abha bajpai and my age is 23")
    conversation_object.run_conversation(conversation,"what is my name")
    conversation_object.run_conversation(conversation,"what is my age")
    memory2=ConversationBufferWindowMemory(k=2)
    conversation=conversation_object.create_conversation(memory2)
    conversation_object.run_conversation(conversation,"my name is abha bajpai and my age is 23")
    conversation_object.run_conversation(conversation,"what is my name")
    conversation_object.run_conversation(conversation,"what is my age")

    
