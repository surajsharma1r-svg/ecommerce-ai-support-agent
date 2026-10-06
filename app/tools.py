import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "data" / "database" / "orders.json"


def get_order_status(order_id):

    with open(DATABASE_PATH, "r", encoding="utf-8") as file:
        orders = json.load(file)

    for order in orders:

        if order["order_id"] == order_id:

            return {
                "order_id": order["order_id"],
                "product": order["product"],
                "status": order["status"],
                "payment_method": order["payment_method"]
            }

    return {
        "error": "Order not found"
    }

# Cancel order toool 

def cancel_order(order_id):

    with open(DATABASE_PATH, "r", encoding="utf-8") as file:
        orders = json.load(file)

    for order in orders:

        if order["order_id"] == order_id:

            status = order["status"]

            if status == "Cancelled":
                return {
                    "order_id": order_id,
                    "success": False,
                    "message": "Order is already cancelled."
                }

            if status != "Processing":
                return {
                    "order_id": order_id,
                    "success": False,
                    "message": f"Order cannot be cancelled because it is {status}."
                }

            order["status"] = "Cancelled"

            with open(DATABASE_PATH, "w", encoding="utf-8") as file:
                json.dump(orders, file, indent=4)

            return {
                "order_id": order_id,
                "success": True,
                "message": "Order cancelled successfully."
            }

    return {
        "order_id": order_id,
        "success": False,
        "message": "Order not found."
    }

# Refund Request tool 

def request_refund(order_id):

    with open(DATABASE_PATH, "r", encoding="utf-8") as file:
        orders = json.load(file)

    for order in orders:

        if order["order_id"] == order_id:

            if order["status"] == "Cancelled":
                return {
                    "order_id": order_id,
                    "success": False,
                    "message": "Refund cannot be requested for a cancelled order."
                }

            if order["status"] != "Delivered":
                return {
                    "order_id": order_id,
                    "success": False,
                    "message": "Refund can only be requested for delivered orders."
                }

            return {
                "order_id": order_id,
                "success": True,
                "message": "Refund request submitted successfully."
            }

    return {
        "order_id": order_id,
        "success": False,
        "message": "Order not found."
    }