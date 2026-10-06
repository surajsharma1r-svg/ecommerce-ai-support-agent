import ollama

MODEL_NAME = "llama3.2:3b"


def generate_answer(query, context):

    prompt = f"""
Answer the customer's question using only the context below.

Context:
{context}

Customer question:
{query}

Rules:
- Use only information explicitly present in the context.
- Do not invent or assume information.
- If the answer is not in the context, say you don't have enough information.
- Answer directly and briefly.

Answer:
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"].strip()