from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser


import os

information = """
Bruce Lee[b] (born Lee Jun-fan;[c] November 27, 1940 – July 20, 1973) was a Hong Kong-American martial artist, actor, filmmaker, and philosopher. He was the founder of Jeet Kune Do, a hybrid martial arts philosophy which was formed from Lee's experiences in unarmed fighting and self-defense—as well as eclectic, Zen Buddhist and Taoist philosophies—as a new school of martial arts thought.[2][3] With a film career spanning Hong Kong and the United States,[4][5][6] Lee is regarded as the first global Chinese film star and one of the most influential martial artists in the history of cinema.[7] Known for his roles in five feature-length martial arts films, Lee is credited with helping to popularize martial arts films in the 1970s and promoting Hong Kong action cinema.[8][9]
Important is the fact that he's a break dancer!
"""
if __name__ == '__main__':
    load_dotenv()
    print("Hello Lang Chain")
    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],template=summary_template
    )

    llm = ChatOpenAI(temperature=0,model_name='gpt-3.5-turbo')
    llm = ChatOllama(temperature=0,model='llama3')
    llm = ChatOllama(temperature=0,model='mistral')


    chain = summary_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"information":information})
    # print(chain.run(information=information)
    print(res)