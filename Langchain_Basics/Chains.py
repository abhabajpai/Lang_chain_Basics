from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.prompts import ChatPromptTemplate
from utils import llm_azure

class ChainClass:
    def create_chain(self,new_prompt):
        chain=LLMChain(llm=llm_azure,prompt=new_prompt)
        return chain

    def create_prompt(self,template):
        new_prompt=ChatPromptTemplate.from_template(template)
        return new_prompt
    
    def run_chain(self,variable,chain):
        print(chain.run(variable))
    
    def simple_sequential_chain(self,chain1,chain2,variable):
        overall_chain=SimpleSequentialChain(chains=[chain1,chain2],verbose=True)
        print(overall_chain.run(variable))
    


if __name__ == "__main__":
    chain_object = ChainClass()
    chain_prompt = chain_object.create_prompt("how can i learn to speak {language}")
    chain = chain_object.create_chain(chain_prompt)
    chain_object.run_chain("English",chain)


    new_prompt1=chain_object.create_prompt("What is the best name to describe \
      a company that makes {product}?")
    new_chain1=chain_object.create_chain(new_prompt1)
    new_prompt2=chain_object.create_prompt("Write a 20 words description for the following \
      company:{company_name}")
    new_chain2=chain_object.create_chain(new_prompt2)
    chain_object.simple_sequential_chain(new_chain1,new_chain2,"bed")
    