# RAG Concept Notes

Here is the RAG pipeline diagram:

![RAG Pipeline](images\image.png)

This diagram shows the retrieval-augmented generation pipeline...

# 📘 Retrieval Augmented Generation (RAG) — Notes

---

## 🔍 1. What Is RAG?

**Retrieval Augmented Generation (RAG)** is a technique where an LLM retrieves relevant information from an external knowledge source (your documents) and uses it during generation.

RAG improves:
- accuracy  
- reduces hallucinations  
- adds domain-specific knowledge  
- bypasses LLM context & knowledge limitations  

---

## 🧱 2. RAG Pipeline Overview

The RAG workflow consists of **four major stages**:

1. **Data Ingestion (Load)**
2. **Data Transformation (Split)**
3. **Embedding (Vectors)**
4. **Vector Store (Similarity Search)**

---

## 📥 3. Data Ingestion (Load)

Data can come from various sources:

- PDF files  
- Text files  
- Word documents  
- Websites / URLs  
- CSV / JSON  
- APIs, Notion docs, GitHub content  
- Databases  

**Purpose:** Convert raw data → clean text  
**Tools:** LangChain Loaders  
(Example: `PDFLoader`, `WebBaseLoader`, `TextLoader`)

---

## 🧩 4. Data Transformation (Split)

Large documents must be split into smaller chunks before embedding.

Typical settings:
- **Chunk size:** 200–500 tokens  
- **Overlap:** 20–50 tokens  

This ensures:
- Better retrieval  
- Preserved context  
- No abrupt cuts  

**Tools:**  
- `RecursiveCharacterTextSplitter`  
- `MarkdownHeaderTextSplitter`  

**Goal:** TEXT → CHUNKS

---

## 🧠 5. Embedding (Vectorization)

Each chunk is converted into a numerical vector that captures semantic meaning.

Example vector:
```[0.31, 0.04, 1.18, 0.93, ...]```


**Tools:**
- OpenAI Embeddings  
- HuggingFace Embeddings  
- Local models (BGE, Instructor, etc.)  

**Goal:** CHUNKS → VECTORS

---

## 📦 6. Vector Store (Storage)

These embeddings are stored in a **vector database**, enabling fast similarity search.

Popular Vector DBs:
1. **FAISS** (local, fast)  
2. **ChromaDB** (simple, lightweight)  
3. **AstraDB** (cloud-based)  
4. **Pinecone**  
5. **Weaviate**

Each stored item contains:
- the vector  
- associated text  
- metadata  

**Goal:** Store & retrieve relevant vectors efficiently

---

## 🔎 7. Query-Time Retrieval Flow

When a user asks a question:

### **Step 1 — Query Embedding**
Convert the question → vector.

### **Step 2 — Similarity Search**
Find the most relevant chunks from the vector database.

### **Step 3 — Context Augmentation**
Add retrieved text as context to the LLM prompt.

### **Step 4 — Generation**
LLM uses:
- retrieved information  
- internal reasoning  

to produce a grounded, accurate answer.

---

## 🎯 8. Why Use RAG?

RAG solves major LLM limitations:

- ❌ Hallucinations  
- ❌ Outdated/limited knowledge  
- ❌ No private data access  
- ❌ Context window limits  

RAG enables:
- ✔ Domain-specific expertise  
- ✔ Up-to-date answers  
- ✔ Context-rich responses  
- ✔ Safer outputs  

---

## 🧩 9. RAG Component Summary

| Stage | Purpose | Tools |
|-------|---------|--------|
| **Ingestion** | Load raw data | LangChain loaders |
| **Chunking** | Split into smaller parts | Text splitters |
| **Embedding** | Convert chunks to vectors | OpenAI/HF embeddings |
| **Vector Store** | Store + index vectors | FAISS, Chroma, AstraDB |
| **Retrieval** | Find similar chunks | Similarity search |
| **Generation** | Produce answer | LLM (OpenAI/Ollama/etc.) |

---

## ⚠️ 10. Limitations of RAG

- Poor chunking → bad retrieval  
- Weak embeddings → inaccurate answers  
- Retrieval heavily impacts generation  
- LLM context limits still apply  
- Needs high-quality ingestion  

---

## 📊 11. RAG Visual Flow (ASCII Diagram)
```
  ┌────────────────┐
  │   Data Source  │   (PDFs, URLs, Text)
  └───────┬────────┘
          │ Load
          ▼
  ┌────────────────┐
  │   Splitter     │   (Chunks + overlap)
  └───────┬────────┘
          │ Embed
          ▼
  ┌────────────────┐
  │   Vector DB    │   (FAISS / Chroma)
  └───────┬────────┘
          │ Similarity Search
          ▼
  ┌────────────────┐
  │ Retrieved Text │   (Top-k chunks)
  └───────┬────────┘
          │
          ▼
  ┌────────────────┐
  │      LLM       │   (OpenAI/Ollama)
  └────────────────┘
```

---

## 🧠 12. Final Summary

RAG allows LLMs to:

- Use **your** documents  
- Provide **accurate**, **context-aware** answers  
- Reduce hallucinations  
- Work with **large knowledge bases**  
- Access **domain-specific** and **private** information  

RAG is essential for building:
- Chatbots  
- Enterprise assistants  
- Multi-agent workflows  
- Q&A systems  
- LangGraph applications  

---



