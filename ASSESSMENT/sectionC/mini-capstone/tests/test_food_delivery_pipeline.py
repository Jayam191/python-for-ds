from src.food_delivery_pipeline import Order, calculate_commission


def test_order_to_dict():
    order = Order(1, "Pizza Hunt", 2000, True)

    result = order.to_dict()

    assert result["order_id"] == 1
    assert result["name"] == "Pizza Hunt"
    assert result["amount"] == 2000
    assert result["status"] is True


def test_commission():
    order = Order(1, "Pizza Hunt", 2000, True)

    commission = calculate_commission(order)

    assert commission == 200