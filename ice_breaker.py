from typing import Tuple
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from third_parties.linkedin import scrape_linkedin_profile
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
from third_parties.twitter import scrape_user_tweets
from output_parsers import summary_parser
from output_parsers import Summary 
import os

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent

def ice_breaker_with(name:str) -> Tuple[Summary,str]:
    linkedin_username = linkedin_lookup_agent(name=name)
    print('****00000****** Uesr name ',linkedin_username)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username,mock=False)

    # twitter_username = twitter_lookup_agent(name=name)
    # tweets = scrape_user_tweets(username=twitter_username)


    # summary_template = """
    #     given the  information about a person from Linkedin {information},
    #     and twitter posts {twitter_posts} I want you to create:
    #     1. a short summary
    #     2. two interesting facts about them

    #     Use both information from twitter and linkedin to create the summary
    #     \n{format_instructions}
    # """
    summary_template = """
        given the  information about a person from Linkedin {information},
     I want you to create:
        1. a short summary
        2. two interesting facts about them

        Use both information from twitter and linkedin to create the summary
        \n{format_instructions}
    """
    summary_prompt_template = PromptTemplate(
      #  input_variables=["information","twitter_posts"],template=summary_template,
        input_variables=["information"],template=summary_template,
        partial_variables={"format_instructions":summary_parser.get_format_instructions()},
    )

    # res = chain.invoke(input={"information":linkedin_data})
    
    llm = ChatOpenAI(temperature=0,model='gpt-4o')

    # chain = summary_prompt_template | llm 
    # chain = summary_prompt_template | llm | StrOutputParser()
    chain = summary_prompt_template | llm | summary_parser
    # res:Summary  = chain.invoke(input={"information":linkedin_data,"twitter_posts":tweets})
    res:Summary  = chain.invoke(input={"information":linkedin_data})
    print('returning summary')
    print(res,linkedin_data.get("photoUrl"))
    return res, linkedin_data.get("photoUrl")


if __name__ == '__main__':
    load_dotenv()

    print("Hello Ice Breaker")
    ice_breaker_with(name="Marco Perez WellsFargo",mock=True)