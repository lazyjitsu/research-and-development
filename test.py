from dotenv import load_dotenv
from langchain.agents import tool
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import render_text_description
from langchain.agents.output_parsers.react_json_single_input import ReActJsonSingleInputOutputParser
from langchain.schema import AgentAction, AgentFinish
from typing import Union, List
from langchain.tools import Tool, tool

from langchain_openai import ChatOpenAI

load_dotenv()

@tool
def get_text_length(text:str)->int:
    """Returns the length of a text by characters"""
    text  = text.strip("\n").strip('"')
    return len(text)

def find_tool_by_name(tools: List[Tool], tool_name: str) -> Tool:
    for tool in tools:
        if tool.name == tool_name:
            return tool
    raise ValueError(f"Tool wtih name {tool_name} not found")

if __name__ == '__main__':
   # print("hello React LangChain",get_text_length(text="cats"))
   # since get_text_length is no longer a fcn but a structured tool, it can not be called normally. need to do it like below
   # so the way you pass is using input=some dictionary
    print("hello Reacts LangChain",get_text_length.invoke(input={"text":"catss"}))
    tools = [get_text_length]

    # this prompt will be sent to the LLM and this is going to generate the thought of the LLM and 
    # help us select the correct tool
    template = """
        Answer the following questions as best you can. You have access to the following tools:

        {tools}

        Use the following format:

        Question: the input question you must answer
        Thought: you should always think about what to do
        Action: the action to take, should be one of [{tool_names}]
        Action Input: the input to the action
        Observation: the result of the action
        ... (this Thought/Action/Action Input/Observation can repeat N times)
        Thought: I now know the final answer
        Final Answer: the final answer to the original input question

        Begin!

        Question: {input}
        Thought:
        """
    prompt = PromptTemplate.from_template(template=template).partial(tools=render_text_description(tools), tool_names = ", ".join([t.name for t in tools]))
    # stop observation tells the LLM to stop generating text when it sees the word "Observation"
    llm = ChatOpenAI(temperature = 0,stop =["\nObservation"])
    # agent = prompt | llm
    # lambda fcn that is receiving a dictionary and returning the value of the key "input"
    #agent = {"input": lambda x:x["input"]} | prompt | llm | ReActJsonSingleInputOutputParser()
    agent = {"input": lambda x:print("X rated: ",x)} | prompt | llm | ReActJsonSingleInputOutputParser()

    print(agent)
    print('---')
    res = agent.invoke({"input":"What is the length of 'monster' in characters?'"})
