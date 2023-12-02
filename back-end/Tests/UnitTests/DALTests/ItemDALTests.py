from DAL.ItemDAL.ItemDALImplementation import ItemDALImplementation
from Entities.Item import Item

item_dao = ItemDALImplementation()

test_item = Item(0, "new")
update_item = Item(test_item.item_id, "updated")

def test_create_item_success():
    result = item_dao.create_item(test_item)
    assert result.item_id != 0

def test_get_item_success():
    result = item_dao.get_item(test_item.item_id)
    assert result is not None

def test_get_all_items_success():
    result = item_dao.get_all_items()
    assert len(result) > 0

def test_update_item_success():
    result = item_dao.update_item(update_item)
    assert result

def test_delete_item_success():
    result = item_dao.delete_item(test_item.item_id)
    assert result
