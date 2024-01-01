from DAL.OrderDAL.OrderDALImplementation import OrderDALImplementation
from Entities.Item import Item
from SAL.OrderSAL.OrderSALImplementation import OrderSALImplementation
from DAL.ItemDAL.ItemDALImplementation import ItemDALImplementation
from SAL.ItemSAL.ItemSALImplementation import ItemSALImplementation
from Entities.CustomError import CustomError
from Entities.Order import Order

order_dao = OrderDALImplementation()
order_sao = OrderSALImplementation(order_dao)
item_dao = ItemDALImplementation()
item_sao = ItemSALImplementation(item_dao)

current_order_id = 1
test_order = Order(0, "test customer", {1: 2, }, "test description", False, False)
update_order = Order(current_order_id, "updated customer", {1: 1, }, "updated description", True, True)

def test_get_all_orders_not_found():
    try:
        order_sao.get_all_orders()
        assert False
    except CustomError as error:
        assert str(error) == "No orders found, please try again!"

def test_create_order_customer_name_not_string():
    try:
        order = Order(0, 1, {1: 2, }, "test description", False, False)
        order_sao.create_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The customer name field must be a string, please try again!"

def test_create_order_customer_name_too_long():
    try:
        order = Order(0, "this customer name too long test requires this name to be too long to catch the error",
                      {1: 2, }, "test description", False, False)
        order_sao.create_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The customer name field cannot exceed 60 characters, please try again!"

def test_create_order_customer_name_empty():
    try:
        order = Order(0, "", {1: 2, }, "test description", False, False)
        order_sao.create_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The customer name field cannot be left empty, please try again!"

def test_create_order_item_list_not_dictionary():
    try:
        order = Order(0, "test customer", [1, 2, 3, 4], "test description", False, False)
        order_sao.create_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The item list field must be a dictionary, please try again!"

def test_create_order_item_list_item_id_not_integer():
    try:
        order = Order(0, "test customer", {"1": 2, }, "test description", False, False)
        order_sao.create_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The item list item ID field must be an integer, please try again!"

def test_create_order_item_list_item_quantity_not_integer():
    try:
        order = Order(0, "test customer", {1: "2", }, "test description", False, False)
        order_sao.create_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The item list quantity field must be an integer, please try again!"

def test_create_order_item_list_item_not_found():
    try:
        order = Order(0, "test customer", {-8375328192: 2, }, "test description", False, False)
        order_sao.create_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "Item not found, please try again!"

def test_create_order_item_list_quantity_not_positive():
    try:
        order = Order(0, "test customer", {1: -2, }, "test description", False, False)
        order_sao.create_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The item list quantity field must be positive, please try again!"

def test_create_order_item_list_empty():
    try:
        order = Order(0, "test customer", {}, "test description", False, False)
        order_sao.create_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The order item list field cannot be left empty, please try again!"

def test_create_order_description_not_string():
    try:
        order = Order(0, "test customer", {1: 2, }, 1, False, False)
        order_sao.create_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The description field must be a string, please try again!"

def test_create_order_description_empty():
    try:
        order = Order(0, "test customer", {1: 2, }, "", False, False)
        order_sao.create_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The description field cannot be left empty, please try again!"

def test_create_order_description_too_long():
    try:
        order = Order(0, "test customer", {1: 2, }, "this description field is too long and is not going to pass "
                                                    "because it will be caught by the service layer method, it then "
                                                    "make this test pass by throwing the correct error message, it "
                                                    "just cannot be over two hundred and fifty five characters, which "
                                                    "doesn't seem like a lot but really is quite a lot of characters "
                                                    "and is a pretty reasonable cut off length", False, False)
        order_sao.create_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The description field cannot exceed 255 characters, please try again!"

def test_create_order_complete_not_boolean():
    try:
        order = Order(0, "test customer", {1: 2, }, "test description", "False", False)
        order_sao.create_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The complete field must be a boolean, please try again!"

def test_create_order_paid_not_boolean():
    try:
        order = Order(0, "test customer", {1: 2, }, "test description", False, "False")
        order_sao.create_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The paid field must be a boolean, please try again!"

def test_create_order_success():
    item_sao.create_item(Item(0, "test item"))
    result = order_sao.create_order(test_order)
    assert result.order_id != 0

def test_get_order_id_not_integer():
    try:
        order_sao.get_order("")
        assert False
    except CustomError as error:
        assert str(error) == "The order ID field must be an integer, please try again!"

def test_get_order_not_found():
    try:
        order_sao.get_order(-3622819946282012737)
        assert False
    except CustomError as error:
        assert str(error) == "Order not found, please try again!"

def test_get_order_success():
    result = order_sao.get_order(current_order_id)
    assert result is not None

def test_get_all_orders_success():
    result = order_sao.get_all_orders()
    assert len(result) > 0

def test_update_order_id_not_integer():
    try:
        order = Order(str(current_order_id), "test customer", {1: 2, }, "test description", False, False)
        order_sao.update_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The order ID field must be an integer, please try again!"

def test_update_order_not_found():
    try:
        order = Order(-3657282992836627, "test customer", {1: 2, }, "test description", False, False)
        order_sao.update_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "Order not found, please try again!"

def test_update_order_customer_name_not_string():
    try:
        order = Order(current_order_id, 1, {1: 2, }, "test description", False, False)
        order_sao.update_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The customer name field must be a string, please try again!"

def test_update_order_customer_name_too_long():
    try:
        order = Order(current_order_id, "this customer name too long test requires this name to be too long to catch "
                                        "the error", {1: 2, }, "test description", False, False)
        order_sao.update_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The customer name field cannot exceed 60 characters, please try again!"

def test_update_order_customer_name_empty():
    try:
        order = Order(current_order_id, "", {1: 2, }, "test description", False, False)
        order_sao.update_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The customer name field cannot be left empty, please try again!"

def test_update_order_item_list_not_dictionary():
    try:
        order = Order(current_order_id, "test customer", [1, 2, 3, 4], "test description", False, False)
        order_sao.update_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The item list field must be a dictionary, please try again!"

def test_update_order_item_list_item_id_not_integer():
    try:
        order = Order(current_order_id, "test customer", {"1": 2, }, "test description", False, False)
        order_sao.update_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The item list item ID field must be an integer, please try again!"

def test_update_order_item_list_item_quantity_not_integer():
    try:
        order = Order(current_order_id, "test customer", {1: "2", }, "test description", False, False)
        order_sao.update_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The item list quantity field must be an integer, please try again!"

def test_update_order_item_list_item_not_found():
    try:
        order = Order(current_order_id, "test customer", {-8375328192: 2, }, "test description", False, False)
        order_sao.update_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "Item not found, please try again!"

def test_update_order_item_list_quantity_not_positive():
    try:
        order = Order(current_order_id, "test customer", {1: -2, }, "test description", False, False)
        order_sao.update_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The item list quantity field must be positive, please try again!"

def test_update_order_item_list_empty():
    try:
        order = Order(current_order_id, "test customer", {}, "test description", False, False)
        order_sao.update_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The order item list field cannot be left empty, please try again!"

def test_update_order_description_not_string():
    try:
        order = Order(current_order_id, "test customer", {1: 2, }, 1, False, False)
        order_sao.update_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The description field must be a string, please try again!"

def test_update_order_description_empty():
    try:
        order = Order(current_order_id, "test customer", {1: 2, }, "", False, False)
        order_sao.update_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The description field cannot be left empty, please try again!"

def test_update_order_description_too_long():
    try:
        order = Order(current_order_id, "test customer", {1: 2, }, "this description field is too long and is not "
                                                                   "going to pass because it will be caught by the "
                                                                   "service layer method, it then make this test pass "
                                                                   "by throwing the correct error message, it just "
                                                                   "cannot be over two hundred and fifty five "
                                                                   "characters, which doesn't seem like a lot but "
                                                                   "really is quite a lot of characters and is a "
                                                                   "pretty reasonable cut off length", False, False)
        order_sao.update_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The description field cannot exceed 255 characters, please try again!"

def test_update_order_complete_not_boolean():
    try:
        order = Order(current_order_id, "test customer", {1: 2, }, "test description", "False", False)
        order_sao.update_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The complete field must be a boolean, please try again!"

def test_update_order_paid_not_boolean():
    try:
        order = Order(current_order_id, "test customer", {1: 2, }, "test description", False, "False")
        order_sao.update_order(order)
        assert False
    except CustomError as error:
        assert str(error) == "The paid field must be a boolean, please try again!"

def test_update_order_success():
    result = order_sao.update_order(update_order)
    assert result

def test_delete_order_id_not_integer():
    try:
        order_sao.delete_order("")
        assert False
    except CustomError as error:
        assert str(error) == "The order ID field must be an integer, please try again!"

def test_delete_order_not_found():
    try:
        order_sao.delete_order(-23726522901726)
        assert False
    except CustomError as error:
        assert str(error) == "Order not found, please try again!"

def test_delete_order_success():
    result = order_sao.delete_order(current_order_id)
    item_sao.delete_item(1)
    assert result
