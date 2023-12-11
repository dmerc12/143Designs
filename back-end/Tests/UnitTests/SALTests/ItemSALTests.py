from DAL.ItemDAL.ItemDALImplementation import ItemDALImplementation
from Entities.CustomError import CustomError
from SAL.ItemSAL.ItemSALImplementation import ItemSALImplementation
from Entities.Item import Item

item_dao = ItemDALImplementation()
item_sao = ItemSALImplementation(item_dao)

current_item_id = 1
test_item = Item(0, "new")
update_item = Item(current_item_id, "updated")

def test_get_all_items_none_found():
    try:
        item_sao.get_all_items()
        assert False
    except CustomError as error:
        assert str(error) == "No items found, please try again!"

def test_create_item_name_not_string():
    try:
        item = Item(0, 1)
        item_sao.create_item(item)
        assert False
    except CustomError as error:
        assert str(error) == "The item name field must be a string, please try again!"

def test_create_item_name_empty():
    try:
        item = Item(0, "")
        item_sao.create_item(item)
        assert False
    except CustomError as error:
        assert str(error) == "The item name field cannot be left empty, please try again!"

def test_create_item_name_too_long():
    try:
        item = Item(0, "this is too long and so it should raise the desired error and pass the test")
        item_sao.create_item(item)
        assert False
    except CustomError as error:
        assert str(error) == "The item name field cannot exceed 60 characters, please try again!"

def test_create_item_success():
    result = item_sao.create_item(test_item)
    assert result.item_id != 0

def test_get_item_id_not_integer():
    try:
        item_sao.get_item(str(current_item_id))
        assert False
    except CustomError as error:
        assert str(error) == "The item ID field must be an integer, please try again!"

def test_get_item_not_found():
    try:
        item_sao.get_item(-5773732992746849)
        assert False
    except CustomError as error:
        assert str(error) == "Item not found, please try again!"

def test_get_item_success():
    result = item_sao.get_item(current_item_id)
    assert result is not None

def test_get_all_items_success():
    result = item_sao.get_all_items()
    assert len(result) > 0

def test_update_item_id_not_integer():
    try:
        item = Item("", "no")
        item_sao.update_item(item)
        assert False
    except CustomError as error:
        assert str(error) == "The item ID field must be an integer, please try again!"

def test_update_item_not_found():
    try:
        item = Item(-497635728929, "no")
        item_sao.update_item(item)
        assert False
    except CustomError as error:
        assert str(error) == "Item not found, please try again!"

def test_update_item_name_not_string():
    try:
        item = Item(current_item_id, 1)
        item_sao.update_item(item)
        assert False
    except CustomError as error:
        assert str(error) == "The item name field must be a string, please try again!"

def test_update_item_name_empty():
    try:
        item = Item(current_item_id, "")
        item_sao.update_item(item)
        assert False
    except CustomError as error:
        assert str(error) == "The item name field cannot be left empty, please try again!"

def test_update_item_name_too_long():
    try:
        item = Item(0, "this is too long and so it should raise the desired error and pass the test")
        item_sao.update_item(item)
        assert False
    except CustomError as error:
        assert str(error) == "The item name field cannot exceed 60 characters, please try again!"

def test_update_item_nothing_changed():
    try:
        item = Item(-1, "test")
        item_sao.update_item(item)
        assert False
    except CustomError as error:
        assert str(error) == "Nothing changed, please try again!"

def test_update_item_success():
    result = item_sao.update_item(update_item)
    assert result

def test_delete_item_id_not_integer():
    try:
        item_sao.delete_item("")
        assert False
    except CustomError as error:
        assert str(error) == "The item ID field must be an integer, please try again!"

def test_delete_item_not_found():
    try:
        item_sao.delete_item(-5873726829475)
        assert False
    except CustomError as error:
        assert str(error) == "Item not found, please try again!"

def test_delete_item_success():
    result = item_sao.delete_item(test_item.item_id)
    assert result
