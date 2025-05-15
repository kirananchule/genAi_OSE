# # Streamlit UI
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from chains.query_parser import parse_user_query
from chains.search_chain import search_products

# st.set_page_config(page_title="Laptop Finder")

# def main():
#     st.title("💻 Smart Laptop Search")
    
#     # Dynamic query input
#     query =  st.text_input("Describe your ideal laptop:", 
#                          placeholder="e.g. 'Under $700 for programming with 16GB RAM'")
    
#     if query:
#         with st.spinner("Analyzing your needs..."):
#             try:
#                 # Query parsing
#                 parsed = parse_user_query(query)
#                 st.json(parsed)
                
#                 # Semantic search
#                 results = search_products(parsed)
#                 st.subheader("🔍 Top Matches")
#                 st.write(results)
                
#             except Exception as e:
#                 st.error(f"Error: {str(e)}")

# if __name__ == "__main__":
#     main()
import streamlit as st

def main():
    st.title("🧪 Streamlit is Running!")
    st.write("This is a test.")
    query = st.text_input("Describe your ideal laptop:", placeholder="e.g. 'Under $700 for programming with 16GB RAM'")
    if query:
        with st.spinner("Analyzing your needs..."):
            try:
                # Query parsing
                parsed = parse_user_query(query)
                st.json(parsed)
                
                # Semantic search
                results = search_products(parsed)
                st.subheader("🔍 Top Matches")
                st.write(results)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
         
if __name__ == "__main__":
    main()