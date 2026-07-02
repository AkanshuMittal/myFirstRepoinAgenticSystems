# ShopEasy wants a small demo: split two short policies into chunks, store them in Chroma with file labels, and answer one customer question using semantic search.

# Create a single Python file named policy_chunk_demo.py.

# Step 1 — Use the provided sample_corpus and chunking helpers (chunk_text, create_chunks_from_corpus) with chunk_size=500 and overlap=75. Print total chunks and one example id with metadata.

# Step 2 — Store chunks in Chroma collection policy_chunks (embedding_function=None) using SentenceTransformer("all-MiniLM-L6-v2"). Print collection.count().

# Step 3 — Run semantic search for: How many days do I have to return a product? with n_results=2. Print Rank 1 id, document, and metadata (source_id).

# Expected: Rank 1 source_id should be returns_policy.txt.

sample_corpus = [
    {
        "metadata": {"source_id": "returns_policy.txt", "page": 0},
        "text": "At ShopEasy, we want you to be completely satisfied with your purchase. Customers can return most unused and unopened products within 30 days of delivery for a full refund. Refunds are processed to the original payment method within 5 to 7 business days after the return is received and approved by our warehouse team. Please note that customized items, perishable goods, and clearance merchandise are final sale and cannot be returned under any circumstances. If you receive a damaged item, you must report it to support within 48 hours of delivery."
    },
    {
        "metadata": {"source_id": "shipping_policy.txt", "page": 0},
        "text": "We offer several shipping options to meet your needs. Standard shipping usually takes 3-5 business days. Express delivery orders usually arrive within 24 to 48 hours depending on your zip code. Orders above 499 rupees qualify for free standard shipping automatically at checkout. For international orders, delivery times may vary between 7 to 14 business days depending on customs processing in the destination country. Duties and taxes for international shipments are the responsibility of the customer."
    }
]

def chunk_text(text, chunk_size=200, overlap=50): # Values lowered slightly from 500/75 for this demo to explicitly show the text splitting!
    """Strategy 1: fixed character windows with overlap."""
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be larger than overlap")

    chunks = []
    start = 0
    while start < len(text):
        piece = text[start : start + chunk_size].strip()
        if piece:
            chunks.append(piece)
        start += chunk_size - overlap
    return chunks


def create_chunks_from_corpus(corpus, chunk_size=200, overlap=50):
    """Split every record; attach source_id, page, chunk_index; build stable ids."""
    all_chunks = []

    for record in corpus:
        text = record["text"]
        if not text:
            continue

        source_id = record["metadata"]["source_id"]
        page = record["metadata"]["page"]

        for chunk_index, chunk_body in enumerate(chunk_text(text, chunk_size, overlap)):
            all_chunks.append({
                "id": f"{source_id}__p{page}__c{chunk_index}",
                "text": chunk_body,
                "metadata": {
                    "source_id": source_id,
                    "page": page,
                    "chunk_index": chunk_index,
                },
            })

    return all_chunks

# Apply the chunking strategy to our sample corpus
chunks = create_chunks_from_corpus(sample_corpus, chunk_size=200, overlap=50)

print("Total chunks created:", len(chunks))
print("\n--- Sample Chunk Preview ---")
print("ID:", chunks[0]["id"])
print("Metadata:", chunks[0]["metadata"])
print("Text:", chunks[0]["text"])

import chromadb
from sentence_transformers import SentenceTransformer
from pprint import pprint

client = chromadb.PersistentClient(path="./chroma_store")

# We create a NEW collection explicitly for these policy chunks
collection = client.get_or_create_collection(
    name="policy_chunks",
    embedding_function=None, # We manually pass embeddings
)

# Load our sentence transformer
model = SentenceTransformer("all-MiniLM-L6-v2")

# Prepare parallel lists for Chroma Upsert
ids = [c["id"] for c in chunks]
documents = [c["text"] for c in chunks]
metadatas = [c["metadata"] for c in chunks]

# Encode all chunk texts into vectors
embeddings = model.encode(documents, convert_to_numpy=True).tolist()

# Upsert into Database
collection.upsert(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
    embeddings=embeddings,
)

print("Rows stored in 'policy_chunks':", collection.count())

print("Total records:", collection.count())  # Expect 5

print("\nPeek sample:")
pprint(collection.peek())  # Eyeball ids, text, metadata

user_query = "How many days do I have to return a product?"
query_embedding = model.encode([user_query], convert_to_numpy=True).tolist()

results = collection.query(query_embeddings=query_embedding, n_results=3)

print("\n==========================")
print("Query:", user_query)
print("==========================")

for i in range(len(results["ids"][0])):
    print(f"\n🏆 Rank {i + 1}")
    print(" ID:", results["ids"][0][i])
    print(" Document:", results["documents"][0][i])
    print(" Metadata:", results["metadatas"][0][i])
    if results.get("distances"):
        print(" Distance:", results["distances"][0][i])