from DAL.OrderDAL.OrderDALImplementation import OrderDALImplementation
from Entities.Order import Order

order_dao = OrderDALImplementation()

test_order = Order(0, "test customer", {1: 2, 2: 3}, "test description", False, False)
update_order = Order(test_order.order_id, "updated customer", {1: 1, 2: 5}, "updated description", True, True)

def test_create_order_success():
    result = order_dao.create_order(test_order)
    assert result.order_id != 0

def test_get_order_success():
    result = order_dao.get_order(test_order.order_id)
    assert result is not None

def test_get_all_orders_success():
    result = order_dao.get_all_orders()
    assert len(result) > 0

def test_update_order_success():
    result = order_dao.update_order(update_order)
    assert result

def test_delete_order_success():
    result = order_dao.delete_order(test_order.order_id)
    assert result
