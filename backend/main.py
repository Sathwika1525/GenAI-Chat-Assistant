from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline import search
import google.generativeai as genai
import os

app = FastAPI()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-pro")


class Question(BaseModel):
    question: str


@app.post("/api/chat")
def chat(q: Question):

    # Get relevant documents from RAG
    context_list = search(q.question)

    # Convert list to string
    context = "\n".join(context_list)

    prompt = f"""
Answer the question using the provided context.

Context:
{context}

Question:
{q.question}
"""

    response = model.generate_content(prompt)

    return {
        "answer": response.text,
        "sources": context_list
    }