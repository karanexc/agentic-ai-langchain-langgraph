# RAG Concept Notes

Here is the RAG pipeline diagram:

![RAG Pipeline](images/image.png)

This diagram shows the retrieval-augmented generation pipeline...

📘 Retrieval Augmented Generation (RAG) — Notes
🔍 1. What Is RAG?

Retrieval Augmented Generation (RAG) is a method that improves LLM responses by letting the model access external knowledge (your documents) during generation.

Instead of relying only on the model’s built-in knowledge (which is limited and can hallucinate), RAG retrieves relevant context and provides it to the LLM to generate accurate, grounded answers.

🧱 2. RAG Pipeline Breakdown

The complete RAG workflow has 4 major stages:

📥 Step 1 — Data Ingestion (Load)

Data can come from multiple sources:

PDFs

Text files

Word documents

Websites / URLs

JSON / CSV

Notion, GitHub, APIs

Databases

Goal: Convert raw data → clean text.
Tool: LangChain Loaders.

🧩 Step 2 — Data Transformation (Split)

LLMs cannot process large documents directly.
We split text into small, meaningful chunks.

Typical chunk size: 200–500 tokens

Overlap: 20–50 tokens (to preserve context)

Goal: Text → Chunks.
Tool: RecursiveCharacterTextSplitter.
