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
from langchain_openai import ChatOpenAI

load_dotenv()

if __name__ == "__main__":
    print('hi')
    model = ChatOpenAI(model="gpt-4o")

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

    print("\n----- Prompt with System and Human Messages (Tuple) -----\n")

    messages = [
        ("system", "You are an engineer for {context} writers."),
        ("human", "Write a professional summary of this resume in {rescount} sentences."),
    ]
    prompt_template = ChatPromptTemplate.from_messages(messages)

    combine_docs_model = create_stuff_documents_chain(OpenAI(), prompt_template)
    retriever_chain = create_retrieval_chain(
        new_vectorstore.as_retriever(),
        combine_docs_model
    )

    res = retriever_chain.invoke({"input": "resume", "rescount": 5})
    print(res["answer"])