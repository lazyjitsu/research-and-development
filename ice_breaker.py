from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from third_parties.linkedin import scrape_linkedin_profile
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

import os

from agents.linkedin_lookup_agent import lookup as linkedin_lookup

def ice_breaker_with(name:str) -> str:
    linkedin_username = linkedin_lookup(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    summary_template = """
        given the Linkedin information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],template=summary_template
    )

    llm = ChatOpenAI(temperature=0,model='gpt-4o')
    chain = summary_prompt_template | llm 
    res = chain.invoke(input={"information":linkedin_data})
    
    llm = ChatOpenAI(temperature=0,model='gpt-4o')

    chain = summary_prompt_template | llm 

    res = chain.invoke(input={"information":linkedin_data})
    print(res)


if __name__ == '__main__':
    load_dotenv()

    print("Hello Ice Breaker")
    ice_breaker_with(name="Marco Perez WellsFargo")