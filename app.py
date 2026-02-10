import streamlit as st
from rag_pipeline import qa_chain

st.set_page_config(page_title="Healthcare RAG Chatbot")

st.title("🩺Healthcare RAG Question-Answer Bot")
st.write("Ask questions from your healthcare PDFs")

question = st.text_input("Enter your question:")

if question:
    with st.spinner("Thinking..."):
        response = qa_chain.run(question)
        st.write("### Answer:")
        st.write(response)
