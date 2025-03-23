from dotenv import load_dotenv

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader

from langchain_community.document_loaders import DirectoryLoader
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
load_dotenv()

def ingest_docs():
    # loader = ReadTheDocsLoader("test-flder",features="html.parser")
   # loader = DirectoryLoader("test-flder",glob="**/*.md")
    loader = ReadTheDocsLoader("langchain-docs/api.python.langchain.com/en/latest/",encoding="utf-8")
    raw_docos = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
    documents = text_splitter.split_documents(raw_docos)

    print(f"Loaded {len(raw_docos)}")
    for doc in documents:
        new_url = doc.metadata["source"]
        new_url = new_url.replace("langchiain-docs", "https:/")
        doc.metadata.update({"source":new_url})
    print(f"Going to add {len(documents)}")
    PineconeVectorStore.from_documents(
        documents,embeddings,index_name="marcos-langchain-doc-idx"
    )
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

if __name__ == "__main__":
    print('hi')
    ingest_docs()