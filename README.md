# 🏥 Healthcare PDF Chatbot – Chat With Medical Documents Using AI

This project enables users to **interact with healthcare PDF documents** using a conversational AI interface.  
Upload any medical PDF and ask questions — the chatbot answers directly from the document using **RAG (Retrieval-Augmented Generation)**.

It leverages **PDF parsing**, **chunking**, **semantic retrieval**, **vector search**, and a **powerful GROQ LLM** to provide accurate, source-based answers.

---

## 🚀 Features

- 📄 Upload any healthcare PDF
- 💬 Ask questions from uploaded document
- 🧠 Semantic search using embeddings
- ⚡ Fast responses via GROQ LLM
- 📚 FAISS vector database storage
- 🔍 Retrieves relevant document chunks
- 🖥️ Clean Streamlit chat interface
- 💾 Automatically saves uploaded PDFs
- 🔄 Real-time indexing and querying
- 📎 Source-based answers from document
- 🧾 Separate PDF upload & indexing module

---

## 🛠️ Tech Stack

| Component        | Technology                          |
|------------------|-------------------------------------|
| UI               | Streamlit                           |
| LLM              | GROQ (Llama3 / Mixtral)             |
| Framework        | LlamaIndex + LangChain              |
| Embeddings       | HuggingFace SentenceTransformers    |
| Vector Store     | FAISS                               |
| PDF Handling     | PyPDF                               |
| Backend          | Python                              |

---

## 🔗 Workflow Overview

### 1️⃣ 📄 PDF Upload → Storage  
- User uploads PDF from Streamlit UI  
- File saved automatically inside `data/` folder  
- Separate upload module ensures persistent storage  

### 2️⃣ 📚 Text Extraction  
- PDF parsed using **PyPDF**  
- Raw text extracted from all pages  

### 3️⃣ ✂️ Text Chunking  
- Text split into smaller chunks  
- Improves retrieval accuracy  
- Optimized for semantic search  

### 4️⃣ 🧠 Embedding Generation  
- Each chunk converted into embeddings  
- Using **HuggingFace SentenceTransformers**  

### 5️⃣ 🗂️ Vector Database Creation  
- Embeddings stored in **FAISS vector store**  
- Enables fast similarity search  

### 6️⃣ ❓ User Question  
- User asks question in chat UI  

### 7️⃣ 🔍 Retrieval  
- Relevant chunks retrieved from FAISS  
- Context passed to LLM  

### 8️⃣ 🤖 Answer Generation  
- GROQ LLM generates final response  
- Uses retrieved document context  
- Ensures source-based answers  

### 9️⃣ 💬 Streamlit Chat UI  
- Chat interface shows answer  
- Continuous conversation supported  
- Clean UI for interaction  

---

## 📁 Project Structure

---

## 🛠️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Mayanknarwal0506/RAG_Healthcare_Chatbot.git
cd RAG_Healthcare_Chatbot
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix/Mac
source venv/bin/activate
```

3. **Install the dependencies:**

```bash
pip install -r requirements.txt
```
4. **Start the Streamlit app:**

```bash
streamlit run app.py
```

5. **Visit in your browser:**

```bash
http://localhost:8501
```

