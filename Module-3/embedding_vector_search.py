## Sample data
records = [  # Each dict = one Chroma row (id, text, metadata)
    {"id": "doc1", "text": "Customers can return products within 30 days of delivery.", "metadata": {"category": "returns"}},
    {"id": "doc2", "text": "Refunds are processed within 5 to 7 business days after the return is approved.", "metadata": {"category": "returns"}},
    {"id": "doc3", "text": "Orders above 499 rupees qualify for free shipping.", "metadata": {"category": "shipping"}},
    {"id": "doc4", "text": "You can reset your password from the account settings page.", "metadata": {"category": "account"}},
    {"id": "doc5", "text": "Express delivery orders usually arrive within 24 to 48 hours.", "metadata": {"category": "shipping"}},
]


## Create the Chroma Client and Collection
import chromadb # Vector database client
from pprint import pprint  # Readable output for peek() 

client = chromadb.PersistentClient(path="./chroma_store")  # Local disk — survives restarts

collection = client.get_or_create_collection(
    name="support_knowledge_base",  # Collection name — like a table
    embedding_function=None,  # We pass embeddings manually
)

print("Count before upsert:", collection.count())  # Expect 0 on first run


## Add Data to Your Chroma Collection
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")  # Same model for store and query

# Isolate lists for upsert operation
documents = [record["text"] for record in records]
ids = [record["id"] for record in records]
metadatas = [record["metadata"] for record in records]

document_embeddings = model.encode(
    documents, convert_to_numpy=True
).tolist()  # Chroma expects Python lists

# Upsert writes all four parallel lists
collection.upsert(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
    embeddings=document_embeddings,
)

print("Collection:", collection.name)
print("Upsert complete. Total rows:", collection.count())  # Expect 5


## Verify what you stored

print("Peek (first 5 rows):")
pprint(collection.peek())

print("Get specific document (doc4):")
pprint(collection.get(ids=["doc4"]))


def semantic_search(query_text, n_results):
    print(f"\nQuery: {query_text}")

    query_embedding = model.encode([query_text]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=n_results
    )

    for i in range(len(results["ids"][0])):
        print(f"\nRank {i+1}")
        print("ID:", results["ids"][0][i])
        print("Document:", results["documents"][0][i])
        print("Metadata:", results["metadatas"][0][i])

        if "distances" in results:
            print("Distance:", results["distances"][0][i])

    return results

semantic_search(
    "I want to return my shoes and get my money back",
    3
)

semantic_search(
    "How do I change my login password?",
    2
)

results_q3 = semantic_search(
    "Can I pay with UPI?",
    3
)

print("\n--- Gap analysis ---")
top_id = results_q3["ids"][0][0]
top_category = results_q3["metadatas"][0][0]["category"]

print(f"Sentence 1: {top_id} ranked first and belongs to category '{top_category}'.")
print("Sentence 2: This is still a weak answer because no payment or UPI FAQ exists in the knowledge base.")

#Question-1: Why the same embedding model must encode stored FAQs and every user query ?
#Answer- .Same embedding model must encode both stored FAQs and user queries.
        #  .Otherwise vectors will live in different semantic spaces and similarity search breaks.
        
        
#Question-2: The difference between get() and query() in one line each?
#Answer- .get() retrieves documents using exact IDs.
       # .while query() finds semantically similar documents using embeddings.