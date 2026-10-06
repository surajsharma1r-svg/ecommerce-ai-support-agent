import re

from app.tool_executor import execute_tool


def run_tool_agent(query):

    query_lower = query.lower()

    # =========================
    # 1. Extract Order ID
    # =========================

    match = re.search(
        r"order\s*(?:id|number|#)?\s*(\d+)",
        query_lower
    )

    order_id = match.group(1) if match else None

    # =========================
    # 2. Order Status
    # =========================

    status_keywords = [
        "where",
        "kaha",
        "status",
        "track",
        "tracking"
    ]

    if order_id and any(
        keyword in query_lower
        for keyword in status_keywords
    ):

        tool_result = execute_tool(
            "get_order_status",
            {
                "order_id": order_id
            }
        )

        if "error" in tool_result:
            return tool_result["error"]

        return (
            f"Order {tool_result['order_id']} "
            f"({tool_result['product']}) is currently "
            f"{tool_result['status']}. "
            f"Payment method: {tool_result['payment_method']}."
        )

    # =========================
    # 3. Cancel Order
    # =========================

    if order_id and "cancel" in query_lower:

        tool_result = execute_tool(
            "cancel_order",
            {
                "order_id": order_id
            }
        )

        return tool_result["message"]

    # =========================
    # 4. Request Refund
    # =========================

    if order_id and "refund" in query_lower:

        tool_result = execute_tool(
            "request_refund",
            {
                "order_id": order_id
            }
        )

        return tool_result["message"]

    # =========================
    # 5. Unknown Request
    # =========================

    return "Sorry, I could not understand your request."