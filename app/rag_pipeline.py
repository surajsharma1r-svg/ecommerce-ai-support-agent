# Taking all the RAG flow in one pipeline

from app.data_loader import load_all_documents
from app.text_splitter import split_documents
from app.embedding import create_embeddings, model
from app.vector_store import create_vector_store, search_vector_store
from app.context_builder import build_context
from app.generator import generate_answer

def retrieve_context(query):

    # 1. Load documents
    documents = load_all_documents()

    # 2. Create chunks
    chunks = split_documents(documents)

    # 3. Create document embeddings
    embeddings = create_embeddings(chunks)

    # 4. Create FAISS vector store
    index = create_vector_store(embeddings)

    # 5. Create query embedding
    query_embedding = model.encode(
        query,
        normalize_embeddings=True
    )

    # 6. Retrieve relevant chunks
    results = search_vector_store(
        query_embedding,
        index,
        chunks,
        top_k=3
    )

    # 7. Build context
    context = build_context(results)

    return context

def run_rag(query):

    # =========================
    # 1. Load documents
    # =========================

    documents = load_all_documents()

    # =========================
    # 2. Create chunks
    # =========================

    chunks = split_documents(documents)

    # =========================
    # 3. Create document embeddings
    # =========================

    embeddings = create_embeddings(chunks)

    # =========================
    # 4. Create FAISS vector store
    # =========================

    index = create_vector_store(embeddings)

    # =========================
    # 5. Create query embedding
    # =========================

    query_embedding = model.encode(
        query,
        normalize_embeddings=True
    )

    # =========================
    # 6. Retrieve relevant chunks
    # =========================

    results = search_vector_store(
        query_embedding,
        index,
        chunks,
        top_k=3
    )

    # =========================
    # 7. Build context
    # =========================

    context = build_context(results)

    # =========================
    # DEBUG
    # =========================

    print("\n===== QUERY =====")
    print(query)

    print("\n===== RETRIEVED CONTEXT =====")
    print(context)

    print("\n===== SENDING TO LLM =====")

    # =========================
    # 8. Generate final answer
    # =========================

    answer = generate_answer(
        query,
        context
    )

    return answer

