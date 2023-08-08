from langchain.llms import AzureOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os
load_dotenv()

os.environ["OPENAI_API_TYPE"]="azure"
os.environ["OPENAI_API_VERSION"]="2023-03-15"
os.environ["OPENAI_API_BASE"]=os.getenv("OPENAI_API_BASE")
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

BASE_URL=os.getenv("OPENAI_API_BASE")
API_KEY=os.getenv("OPENAI_API_KEY")
DEPLOYMENT_NAME="GPT3-5"

llm=AzureOpenAI(
    openai_api_base=BASE_URL,
    openai_api_version="2023-05-15",
    deployment_name=DEPLOYMENT_NAME,
    openai_api_key=API_KEY,
    openai_api_type="azure",
    temperature=0,
   
)
template = """\
You are a naming consultant for new companies.
What is a good name for a company that makes {product}?
"""
prompt = PromptTemplate.from_template(template)
print(prompt.format(product="colorful socks"))

#llm_result=llm.generate(["tell me a joke","tell me a poem"])
#print(llm_result)
#prompts
# prompt_template_name=PromptTemplate(
#     input_variables=['cuisine'],
#     template="""i want to open a restaurant for {cuisine} food.suggest a fancy name for this. """

# )
# #var1=prompt_template_name.format(cuisine="indian")
# #print(var1)
# name_chain=LLMChain(llm=llm,prompt=prompt_template_name)
# var1=name_chain.run("indian")
# # print(name_chain.run())
# print(var1)



#chain=SimpleSequentialChain(chains=[])

#llm_result = llm.generate(["Tell me a joke", "Tell me a poem"])
#generate_keywords = llm.generate(["Generate a list of specifications for laptop","limit the result to only 10 specifications"])
#print(generate_keywords)