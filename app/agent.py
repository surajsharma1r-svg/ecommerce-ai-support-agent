import ollama

from app.rag_pipeline import retrieve_context
from app.tool_executor import execute_tool

MODEL_NAME = "llama3.2:3b"


def run_both_agent(query, order_id):

    # =========================
    # 1. Get live order data
    # =========================

    order_result = execute_tool(
        "get_order_status",
        {
            "order_id": order_id
        }
    )

    # =========================
    # 2. Retrieve policy context
    # =========================

    rag_context = retrieve_context(query)

    # =========================
    # 3. Create final prompt
    # =========================

    final_prompt = f"""
You are a ShopEase customer support assistant.

Answer the customer's question using the information below.

CUSTOMER QUESTION:
{query}

ORDER INFORMATION:
{order_result}

IMPORTANT:
The ORDER INFORMATION contains the actual live order data.
Do not infer or assume any information that is not present in it.

SHOP EASE POLICY:
{rag_context}

Rules:
- Use only the provided information.
- Do not invent information.
- Never assume an order was delivered unless the ORDER INFORMATION explicitly says "Delivered".
- Never assume how many days ago an order was delivered unless that information is explicitly provided.
- Do not convert policy timelines into actual customer/order dates.
- Answer the customer's exact question.
- Be concise and professional.
- Do not add greetings or unnecessary closing statements.
FINAL ANSWER:
"""

    # =========================
    # 4. Ask LLM
    # =========================

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ]
    )

    return response["message"]["content"].strip()

import re


def extract_order_id(query):

    match = re.search(
        r"order\s*(?:id|number|#)?\s*(\d+)",
        query.lower()
    )

    if match:
        return match.group(1)

    return None

from app.router import route_query
from app.rag_pipeline import run_rag
from app.tool_agent import run_tool_agent

def run_agent(query):

    route = route_query(query)

    if route == "RAG":
        return run_rag(query)

    elif route == "TOOL":
        return run_tool_agent(query)

    elif route == "BOTH":
        order_id = extract_order_id(query)

        if not order_id:
            return "Please provide your order ID."

        return run_both_agent(query, order_id)

    else:
        return "Sorry, I could not understand your request."


    