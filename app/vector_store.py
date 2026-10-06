import faiss
import numpy as np

def create_vector_store(embeddings):
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)

    index.add(
        np.asarray(embeddings,dtype="float32")
    )

    return index

# ===============
# top 3 suggestion from the policy query asked by user 
# ============

def search_vector_store(query_embedding,index,chunks,top_k=3):
    query_embedding = np.array(
        [query_embedding],
        dtype="float32"
    )

    scores ,indices = index.search(query_embedding,top_k)

    results = []

    for score,index_position in zip(scores[0],indices[0]):
        results.append({
            "score":float(score),
            "file_name":chunks[index_position]["file_name"],
            "chunk_id":chunks[index_position]["chunk_id"],
            "content":chunks[index_position]["content"]
        })

    return results



