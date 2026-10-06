def route_query(query):

    query = query.lower()

    rag_keywords = [
    "refund",
    "return",
    "policy",
    "delivery",
    "payment",
    "rules",
    "eligible",
    "how many days",
    "kitne din"
]

    tool_keywords = [
        "order status",
        "where is my order",
        "track my order",
        "order kaha",
        "order id",
        "order number",
        "order #"
    ]

    has_rag = any(
        keyword in query
        for keyword in rag_keywords
    )

    has_tool = any(
        keyword in query
        for keyword in tool_keywords
    )

    # Explicit order ID detection
    import re

    has_order_id = bool(
        re.search(r"order\s*(?:id|number|#)?\s*\d+", query)
    )

    if has_rag and (has_tool or has_order_id):
        return "BOTH"

    elif has_tool or has_order_id:
        return "TOOL"

    elif has_rag:
        return "RAG"

    else:
        return "UNKNOWN"