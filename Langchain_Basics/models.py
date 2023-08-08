from langchain.chat_models import AzureChatOpenAI
from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage
)
from utils import llm_azure
print(llm_azure([HumanMessage(content="translate this sentence from english to french:i love programming")]).content)
print(llm_azure.predict("write a poem on sky"))

#print(llm("write a poem"))
#result=llm.generate(["write a poem about the destructive power of fire that uses the following words: flames, smoke, ash, embers, blaze, inferno, scorch, charred, smoldering, kindling, tinder, conflagration, combustion, and ignite."])
# print(result.generations)
#print(result.generations[0][0].text)
