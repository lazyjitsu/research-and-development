import os,sys
from dotenv import load_dotenv
# pythonpath = os.getenv('PYTHONPATH')
# print(pythonpath)
# sys.path.append(pythonpath)
load_dotenv()

print(f"Current sys.path: {sys.path}")

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool

from langchain.agents import (
    create_react_agent,
    AgentExecutor
)

# download premade prompts by the community
from langchain import hub
from tools.tools import get_profile_url_tavily

def lookup(name:str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4-turbo",
    )
    template = """
       given the name {name_of_person} I want you to find a link to their Twitter/ X profile page, and extract from it their username
       In Your Final answer only the person's username
       which is extracted from: https://x.com/USERNAME
       """
    
    prompt_template = PromptTemplate(
        template = template, input_variables=["name_of_person"]
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 Twitter profile page",
            func=get_profile_url_tavily,
            description="useful for when you need to get the Twitter Page URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm,tools=tools_for_agent,prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linked_profile_url = result["output"]
    return linked_profile_url

if __name__ == "__main__":
    # linkedin_url = lookup(name="Eden Marco")
    linkedin_url = lookup(name="Eden Marco")
    print(linkedin_url)
