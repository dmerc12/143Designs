from DAL.WorkDAL.WorkDALImplementation import WorkDALImplementation
from Entities.Work import Work

work_dao = WorkDALImplementation()

test_work = Work(0, "test name", "test description")
update_work = Work(test_work.work_id, "updated name", "updated description")

def test_create_work_success():
    result = work_dao.create_work(test_work)
    assert result.work_id != 0

def test_get_work_success():
    result = work_dao.get_work(test_work.work_id)
    assert result is not None

def test_get_all_work_success():
    result = work_dao.get_all_work()
    assert len(result) > 0

def test_update_work_success():
    result = work_dao.update_work(update_work)
    assert result

def test_delete_work_success():
    result = work_dao.delete_work(test_work.work_id)
    assert result
