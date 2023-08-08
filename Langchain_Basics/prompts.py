from langchain.prompts import ChatPromptTemplate
from utils import llm_azure


class gptModelClass:

    def get_response(self, prompt):

        return llm_azure.predict(prompt)



if __name__ == "__main__":

    

    # Run the LLM

    gpt_model = gptModelClass()

    prompt1 = "what is datascience"

    response = gpt_model.get_response(prompt1)

    print(response)
    
