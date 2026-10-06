import ollama

from app.tool_executor import execute_tool


MODEL_NAME = "llama3.2:3b"


TOOL_DEFINITIONS = [
{
    "type": "function",
    "function": {
        "name": "request_refund",
        "description": "Submit a refund request for a ShopEase order.",
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "The ShopEase order ID."
                }
            },
            "required": ["order_id"]
        }
    }
}
]


def run_tool_agent(query):

    # =========================
    # 1. Ask LLM
    # =========================

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": query
            }
        ],
        tools=TOOL_DEFINITIONS
    )

    # =========================
    # 2. Check tool call
    # =========================

    tool_calls = response["message"].get("tool_calls")

    if not tool_calls:
        return response["message"]["content"]

    # =========================
    # 3. Get tool call details
    # =========================

    tool_call = tool_calls[0]

    tool_name = tool_call["function"]["name"]
    arguments = tool_call["function"]["arguments"]

    # =========================
    # 4. Execute tool
    # =========================

    tool_result = execute_tool(
        tool_name,
        arguments
    )

    # =========================
    # 5. Ask LLM to create
    #    final answer
    # =========================

    final_prompt = f"""
You are a ShopEase customer support assistant.

The customer asked:
{query}

A tool was executed to get the required information.

Tool result:
{tool_result}

Answer the customer's question directly using the tool result.

Do not ask for more information.
Do not invent information.

Final answer:
"""

    final_response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ]
    )

    return final_response["message"]["content"].strip()