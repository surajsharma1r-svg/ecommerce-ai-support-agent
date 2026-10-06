from app.tools import (
    get_order_status,
    cancel_order,
    request_refund
)


def test_get_order_status():
    result = get_order_status("1001")

    assert result["order_id"] == "1001"
    assert result["status"] == "Out for Delivery"


def test_get_order_not_found():
    result = get_order_status("9999")

    assert result["error"] == "Order not found"


def test_cancel_out_for_delivery():
    result = cancel_order("1001")

    assert result["success"] is False


def test_refund_delivered_order():
    result = request_refund("1003")

    assert result["success"] is True


def test_refund_not_delivered():
    result = request_refund("1001")

    assert result["success"] is False