import os
import together
import streamlit as st
from llama_index import SimpleDirectoryReader, ServiceContext, VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.query_engine import CitationQueryEngine
from llama_index.embeddings import TogetherEmbedding
from llama_index.llms import TogetherLLM
from dotenv import load_dotenv

load_dotenv()

st.title("ChainCoder")

together.api_key = os.environ["TOGETHER_API_KEY"]

document_dir = './langchain/docs/docs/get_started'

embedding_model = "togethercomputer/m2-bert-80M-8k-retrieval"
generative_model = "mistralai/Mixtral-8x7B-Instruct-v0.1"
to_llm=TogetherLLM(generative_model)
to_embed_model=TogetherEmbedding(embedding_model)

service_context = ServiceContext.from_defaults(llm=to_llm,embed_model=to_embed_model,chunk_size=1000)

PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    # load the documents and create the index
    documents = SimpleDirectoryReader(document_dir).load_data()
    index = VectorStoreIndex.from_documents(documents, service_context=service_context)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    st.write("loading saved index")
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context, service_context=service_context)

# query_engine = index.as_query_engine(service_context=service_context)
query_engine = CitationQueryEngine.from_args(
    index,
    similarity_top_k=3,
    # here we can control how granular citation sources are, the default is 512
    citation_chunk_size=512,
)
query_text = st.text_input("Enter Question:","How to build a chatbot with langchain")
response = query_engine.query(query_text)

st.write(response.response)

