# Production-Grade GenAI Assistant with RAG

## Project Overview

This project implements a **GenAI-powered Chat Assistant** using **Retrieval-Augmented Generation (RAG)**.
The assistant answers user questions by retrieving relevant information from a document knowledge base and passing it to a Large Language Model.

This prevents hallucinations and ensures that responses are **grounded in actual documents**.

---

# Tech Stack

* **Backend:** Python (FastAPI)
* **Frontend:** HTML + JavaScript
* **LLM API:** Gemini API
* **Embeddings API:** Gemini Embedding Model
* **Vector Storage:** In-memory vector store
* **Similarity Search:** Cosine Similarity

---

# Architecture Diagram

User
↓
Frontend (HTML Chat UI)
↓
FastAPI Backend
↓
Query Embedding
↓
Vector Similarity Search
↓
Retrieve Top Documents
↓
Prompt Construction
↓
LLM (Gemini)
↓
Generated Response

---

# RAG Workflow

1. Documents are stored in `docs.json`.
2. Each document is converted into embeddings using the embedding API.
3. The embeddings are stored in a vector store.
4. When a user asks a question:

   * The query is converted into an embedding.
   * Cosine similarity search retrieves the most relevant document chunks.
5. The retrieved context is inserted into the LLM prompt.
6. The LLM generates an answer based only on the retrieved context.

---

# Embedding Strategy

* Each document is converted into vector embeddings using the **Gemini embedding model**.
* Embeddings represent the semantic meaning of text.
* These embeddings allow the system to retrieve relevant documents even when the query wording is different.

Example:

User Query:
"How do I change my password?"

Retrieved Document:
"Users can reset their password from Settings > Security."

---

# Similarity Search

The system uses **Cosine Similarity** to compare:

Query Embedding vs Document Embeddings

Steps:

1. Convert user query into embedding
2. Compute cosine similarity with all stored embeddings
3. Select top 3 most relevant chunks
4. Apply similarity threshold
5. Pass selected chunks to the LLM

---

# Prompt Design

The prompt structure ensures the model only answers using the retrieved context.

Example prompt:

Context:
Users can reset their password from Settings > Security.

Question:
How can I reset my password?

Instruction:
Answer only using the provided context.

This reduces hallucination and ensures reliable responses.

---

# API Endpoint

POST /api/chat

Request:

{
"sessionId": "abc123",
"message": "How can I reset my password?"
}

Response:

{
"reply": "Users can reset their password from Settings > Security.",
"tokensUsed": 0,
"retrievedChunks": 3
}

---

# Setup Instructions

1. Clone the repository

git clone <repository-link>

2. Install dependencies

pip install -r requirements.txt

3. Add your Gemini API Key

Update the API key in the backend code.

4. Run the backend server

cd backend
uvicorn main:app --reload

5. Open the frontend

Open `frontend/index.html` in a browser.

---

# Project Structure

genai-rag-assistant

backend

* main.py
* rag.py
* embeddings.py
* vector_store.py
* docs.json

frontend

* index.html

requirements.txt
README.md

---

# Features

* Document embedding generation
* Vector similarity retrieval
* Retrieval-Augmented Generation
* Chat interface
* Context-aware responses
* API-based backend

---

# Future Improvements

* Persistent vector database
* Better document chunking
* Conversation memory storage
* UI improvements
* Streaming responses
