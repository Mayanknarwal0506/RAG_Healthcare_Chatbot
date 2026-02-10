import streamlit as st
import os
from rag_pipeline import build_rag_chain

from llama_index.core.readers import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex

rag_chain = None


st.set_page_config(page_title="Healthcare RAG Chatbot")

st.title("🩺 Healthcare RAG Chatbot")
st.write("Upload your healthcare PDFs and ask questions.")

# -------------------------------
# PDF Upload Section
# -------------------------------
uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    if not os.path.exists("uploaded_data"):
        os.makedirs("uploaded_data")

    for file in uploaded_files:
        with open(os.path.join("uploaded_data", file.name), "wb") as f:
            f.write(file.getbuffer())

    st.success(f"✅ {len(uploaded_files)} file(s) uploaded successfully!")

    # Build new RAG chain
    rag_chain = build_rag_chain("uploaded_data")

    st.info("RAG index built from uploaded PDFs.")


# -------------------------------
# Question Input
# -------------------------------
question = st.text_input("Enter your question:")

if question and rag_chain:
    with st.spinner("Thinking..."):
        response = rag_chain.invoke(question)
        st.write("### Answer:")
        st.write(response)

