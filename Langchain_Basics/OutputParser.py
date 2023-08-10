from config import llm_azure
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class OutputParsers:
    #to return a list of comma seperated lines
    def get_list_parser(self,output_parser_func):
        
        prompt=PromptTemplate(
            template="""list all the colors in a rainbow""",
            input_variables=[],
            output_parser=output_parser_func
            
        )
        
        llm_chain= LLMChain(prompt=prompt,llm=llm_azure)
        response=llm_chain.predict()
        return response
    

if __name__=="__main__":
    output_parsers=OutputParsers()
    output_parser_func=CommaSeparatedListOutputParser()
    output= output_parsers.get_list_parser(output_parser_func)
    print(output)