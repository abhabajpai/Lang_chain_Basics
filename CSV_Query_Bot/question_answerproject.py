from langchain.prompts import ChatPromptTemplate
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings import HuggingFaceEmbeddings

from utils import llm_azure
class gptIndexClass:
  
  def getFileLoader(self,file):
    loader=CSVLoader(file_path=file)
    return loader
  
  def ToMakeEmbedding(self):
    embeddings=HuggingFaceEmbeddings()
    return embeddings
  
  def toGetResponse(self,embeddings,loader,query):
    index=VectorstoreIndexCreator(
    vectorstore_cls=DocArrayInMemorySearch,
    embedding=embeddings,
    ).from_loaders([loader])
    response = index.query(query, llm=llm_azure)
    return response
  

if __name__ == "__main__":
  gptIndex = gptIndexClass()

  file="/home/shtlp_0053/Desktop/LangChain/langchain_basics/Employee.csv"
  loader= gptIndex.getFileLoader(file)

  embeddings=gptIndex.ToMakeEmbedding()

  query="List employee name of people who work in software engineer"

  response= gptIndex.toGetResponse(embeddings,loader,query)

  print(response)


