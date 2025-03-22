import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import FAISS # local vectore db
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv
from langchain import hub
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

load_dotenv()

if __name__ == "__main__":
    print('hi')
    pdf_path='marco.pdf'
    loader = PyPDFLoader(file_path=pdf_path)
    documents = loader.load()
    text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=30, separator="\n")
    doc_chunks = text_splitter.split_documents(documents=documents)

    embeddings = OpenAIEmbeddings()
    vectorestore= FAISS.from_documents(doc_chunks,embedding=embeddings) #stores in RAM IMU
    vectorestore.save_local("faiss_for-marco_idx")

    new_vectorstore = FAISS.load_local(
        "faiss_for-marco_idx", embeddings, allow_dangerous_deserialization=True # not recommended for production systems. see deserialization attacks
    )
    
    # retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat"
    my_custom_retrieval_prompt = """

    """
    messages = [
        ("system", "You are a technology manager"),
        ("human", "Summarize the resume in {sentences} sentences."),
    ]
    formatted_prompt = ChatPromptTemplate.from_messages(messages)
    combine_docs_chain = create_stuff_documents_chain(
        OpenAI(),
        formatted_prompt
    )
    response=formatted_prompt.invoke({'context':4})
    # retrieval_chain = create_retrieval_chain(
    #     new_vectorstore.as_retriever(), combine_docs_chain
    # )

    # # response = retrieval_chain.invoke({"input": "Give me a summary of the resume in 5 sentences"})
    # response = retrieval_chain.invoke({"sentences": "4"})

    print(f"Answer: {response['answer']}")