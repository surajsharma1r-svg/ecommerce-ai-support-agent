# First we will create data file & load it

# ==============
# Loading refund policy
# ==============

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

KNOWDLEDGE_BASE_DIR = BASE_DIR / "data" / "knowledge_base"


def load_document(file_name):
    file_path = KNOWDLEDGE_BASE_DIR / file_name

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    return content


# ==============
# Load All Documents
# ==============

def load_all_documents():
    documents = []

    for path in KNOWDLEDGE_BASE_DIR.glob("*.txt"):
        content = load_document(path.name)

        documents.append({
            "file_name": path.name,
            "content": content
        })

    return documents