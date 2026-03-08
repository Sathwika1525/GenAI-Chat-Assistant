import json
import faiss
import numpy as np
from embeddings import get_embedding

# Load documents
with open("documents.json", "r") as f:
    docs = json.load(f)

texts = [doc["content"] for doc in docs]

# Convert documents to embeddings
embeddings = [get_embedding(text) for text in texts]

dimension = len(embeddings[0])

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

def search(query):
    query_embedding = get_embedding(query)
    D, I = index.search(np.array([query_embedding]), k=3)
    results = [texts[i] for i in I[0]]
    return results