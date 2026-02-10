import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

from llama_index.core.readers import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

# ==============================
# LOAD GROQ API KEY
# ==============================
load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")
if not groq_key:
    raise ValueError("GROQ_API_KEY not found in .env file!")

# ==============================
# EMBEDDING MODEL (LOAD ONCE)
# ==============================
embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ==============================
# LLM (LOAD ONCE)
# ==============================
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# ==============================
# PROMPT
# ==============================
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a healthcare assistant.

Answer only from the context.
If not found, say you don't know.

Context:
{context}

Question:
{question}

Answer:
"""
)

# ==============================
# RAG BUILDER
# ==============================
def build_rag_chain(pdf_folder: str):

    # Load PDFs
    documents = SimpleDirectoryReader(pdf_folder).load_data()

    # Build vector index
    index = VectorStoreIndex.from_documents(
        documents,
        embed_model=embed_model
    )

    retriever = index.as_retriever(similarity_top_k=3)

    def get_context(query):
        nodes = retriever.retrieve(query)
        return "\n\n".join([n.get_content() for n in nodes])

    # LCEL chain
    chain = (
        {"context": get_context, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain
