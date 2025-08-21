import chromadb
from sentence_transformers import SentenceTransformer
from chromadb.utils.embedding_functions import EmbeddingFunction

# Step 1: Load a Hugging Face embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Step 2: Define a custom embedding function class
class MyEmbeddingFunction(EmbeddingFunction):
    def __call__(self, texts):
        return embedder.encode(texts).tolist()

# Step 3: Initialize Chroma client (in-memory, no server needed for demo)
client = chromadb.Client()

# Step 4: Create a collection with custom embedding function
collection = client.create_collection(
    name="my_collection",
    embedding_function=MyEmbeddingFunction()
)

# Step 5: Add some documents with unique IDs and metadata
collection.add(
    documents=[
        "AI is the future",
        "Python is great for Machine Learning",
        "FastAPI is used to build APIs quickly",
        "Git helps in version control and collaboration"
    ],
    ids=["1", "2", "3", "4"],
    metadatas=[
        {"topic": "AI"},
        {"topic": "ML"},
        {"topic": "APIs"},
        {"topic": "Git"}
    ]
)

# Step 6: Query the collection (semantic search by meaning)
results = collection.query(
    query_texts=["Tell me about ML and Python"],
    n_results=2
)

print("🔍 Query Results:")
print(results)

# Step 7: Metadata Filtering Example
filtered_results = collection.query(
    query_texts=["Explain APIs"],
    n_results=2,
    where={"topic": "APIs"}  # Only search documents with topic=APIs
)
print("\n Filtered Query Results (topic=APIs):")
print(filtered_results)
