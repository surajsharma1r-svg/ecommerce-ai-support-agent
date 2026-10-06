def route_query (query):

    query = query.lower()

    # ==============
    # RAG Queries 
    # =============

    rag_keywords =[
        "policy",
        "refund",
        "return",
        "cancel",
        "cancellation",
        "delivery",
        "payment",
        "rules",
        "eligible",
        "kitne din",
        "how many days"
    ]

    # ===============
    # Tool Queries 
    # ===============
    tool_keywords = [
    "order status",
    "where is my order",
    "track my order",
    "order kaha",
    "order #",
    "order number",
    "order id",
    "cancel my order",
    "cancel order",
    "order"
]

    has_rag = any(
        keyword in query
        for keyword in rag_keywords
    )

    has_tool = any(
        keyword in query
        for keyword in tool_keywords
    )


    # Routing Decision 
    # ===================

    if has_rag and has_tool:
        return "BOTH"

    elif has_tool :
        return "TOOL"

    elif has_rag:
        return "RAG"

    else :
        return "UNKNOWN"