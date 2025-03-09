import os,sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Append PYTHONPATH to sys.path
print(f"Current sys.path: {sys.path}")

# Print sys.path for debugging
# print(f"Current sys.path: {sys.path}")
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool


from langchain.agents import (
    create_react_agent,
    AgentExecutor
)

# Download premade prompts by the community
from langchain import hub
from tools.tools import get_profile_url_tavily

def lookup(name: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
    )
    template = """given the full name {name_of_person} I want you to get it me a linke to their Linkedin profile page. 
                    Your answer should contain only a URL"""
    
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linked in profile page",
            func=get_profile_url_tavily,
            description="useful for when you need to get the Linkedin Page URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linked_profile_url = result["output"]
    return linked_profile_url

if __name__ == "__main__":
    linkedin_url = lookup(name="Marco Perez WellsFargo")
    print(linkedin_url)