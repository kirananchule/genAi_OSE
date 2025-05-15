from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from google.generativeai import configure, GenerativeModel
import os
from dotenv import load_dotenv

load_dotenv()

llm = GenerativeModel("gemini-pro")

def parse_user_query(query: str) -> dict:
    prompt = ChatPromptTemplate.from_template("""
    Extract JSON with: budget, use_case, min_RAM from:
    Query: {query}
    Example: {{"budget": 500, "use_case": "gaming", "min_RAM": 16}}
    """)
    chain = prompt | llm
    response = chain.invoke({"query": query})
    return eval(response.content)

