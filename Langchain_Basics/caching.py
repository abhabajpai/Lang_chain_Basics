import langchain
from langchain.cache import InMemoryCache
from utils import llm_azure
langchain.llm_azure_cache=InMemoryCache()
print(llm_azure.predict("Tell me a joke"))