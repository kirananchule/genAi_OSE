# RAG pipeline
from langchain.chains import RetrievalQA
from vector_db.embeddings import create_vector_db
from chains.query_parser import llm

vector_db = create_vector_db()

def search_products(parsed_query: dict) -> str:
    retriever = vector_db.as_retriever(
        search_kwargs={
            "k": 10,
            "filter": {"price": {"$lte": parsed_query["budget"]}}}
    ),
    
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": "Find laptops for {use_case} with RAM >= {min_RAM}"}
    )
    return qa_chain.invoke(parsed_query)["result"]

