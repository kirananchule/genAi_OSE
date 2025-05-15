# Embedding logic herefrom langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import pandas as pd

def create_vector_db():
    df = pd.read_csv("data/laptops.csv")
    
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    vector_db = Chroma.from_texts(
        texts=df.apply(lambda x: f"{x['name']} {x['specs']}", axis=1).tolist(),
        embedding=embeddings,
        metadatas=df.to_dict('records'),
        persist_directory="vector_db/chroma_db"
    )
    return vector_db

if __name__ == "__main__":
    create_vector_db()