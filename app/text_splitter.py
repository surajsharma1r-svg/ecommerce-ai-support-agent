
# Text Splitter 
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = []

    for document in documents:
        split_texts = splitter.split_text(document["content"])

        for i, text in enumerate(split_texts):
            chunks.append({
                "file_name": document["file_name"],
                "chunk_id": i,
                "content": text
            })

    return chunks

