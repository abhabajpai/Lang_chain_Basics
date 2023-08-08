import json
from config import llm_azure
from langchain.prompts import ChatPromptTemplate


class ProductSpecifications:
    def generate_keywords(self,product_type):
        prompt="generate the 10 product type key for {text}for example if the product type is laptop then the key of laptop are ram,rom,processor etc ( every key should be in new line )"
        prompt_template=ChatPromptTemplate.from_template(prompt)
        messages=prompt_template.format_messages(text=product_type)
        response=llm_azure(messages)
        return response.content
    
    def generate_values(self,product_description,product_keywords):
        prompt="Only Generate values for {items} corresponding to the previously generated keys. The keys we generated are: {keys}. Please ensure that each key and value are on separate lines.don't give number to each line."
        prompt_template=ChatPromptTemplate.from_template(prompt)
        messages=prompt_template.format_messages(items=product_description,keys=product_keywords)
        response=llm_azure(messages)
        return response.content


if __name__ == "__main__":
    product_specification=ProductSpecifications()
    product_type= input("Enter the product type:\n")
    product_keywords=product_specification.generate_keywords(product_type)
    print(product_keywords)
    product_description=input("Enter the product discription:\n")
    product_key_values=product_specification.generate_values(product_description,product_keywords)
     # Parse product key values into a dictionary
    key_value_pairs = product_key_values.strip().split('\n')
    product_dict = {}
    for pair in key_value_pairs:
        key, value = pair.split(':', 1)
        product_dict[key.strip()] = value.strip()
    
    # Convert dictionary to JSON and print
    product_json = json.dumps(product_dict, indent=4)
    print(product_json)
    output_file_name = "product_output.json"
    with open(output_file_name, 'w') as output_file:
        output_file.write(product_json)
    
    print(f"JSON data written to {output_file_name}")







