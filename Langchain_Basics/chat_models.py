from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage
)
from utils import llm_azure

print(llm_azure([HumanMessage(content="Translate this sentence from english to french:I love programming.")]))
# messages = [[
#     SystemMessage(content="You are a helpful assistant that translates English to French."),
#     HumanMessage(content="I love programming.")
# ],
# [
#      SystemMessage(content="You are a helpful assistant that translates English to French."),
#         HumanMessage(content="I love artificial intelligence.") 
# ],]
# print(llm_azure.generate(messages))
batch_messages = [
    [
        SystemMessage(content="You are a helpful assistant that translates English to French."),
        HumanMessage(content="I love programming.")
    ],
    [
        SystemMessage(content="You are a helpful assistant that translates English to French."),
        HumanMessage(content="I love artificial intelligence.")
    ],
]
result = llm_azure.generate(batch_messages)
print(result.generations)