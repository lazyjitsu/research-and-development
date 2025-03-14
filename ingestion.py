import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

if __name__ == '__main__':
    loader = TextLoader("D://mySource//Training//AI//Udemy//Documents//mediumblog1.txt")
    document = loader.load() # now its a langchain document
    load_dotenv()
    # Now splilt into chunks. CharacterTextSplitter  splits the text into chunks of characters and can use regex
    # it can also use a diff leng fcn to calculate number of tokens. 1000 is a 'hueristic'/rule of thumb to keep
    # the chunks small enough to be processed by the model and fit in the context window. And should be big enough
    # to contain a meaningful amount of information. Overlap 0 when we don't want to use context between chunks.
    text_splitter = CharacterTextSplitter(chunk_size=59,chunk_overlap=0,separator="\n",)

    texts = text_splitter.split_documents(document)
    print(f"created {len(texts)} chunks")
   # print(document)
    # I believe it defaults to text-embedding-ada-002 but we can change the embeddings object of course
    # obviously using OpenAI API to embed our documents
    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))
    print('Ingesting doco...')
    print('idx ',os.environ['INDEX_NAME'])
    PineconeVectorStore.from_documents(texts, embeddings,index_name=os.environ.get("INDEX_NAME"))
    print("Finished ingestion")
    