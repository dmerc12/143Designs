from DAL.WorkDAL.WorkDALImplementation import WorkDALImplementation
from Entities.CustomError import CustomError
from SAL.WorkSAL.WorkSALImplementation import WorkSALImplementation
from Entities.Work import Work

work_dao = WorkDALImplementation()
work_sao = WorkSALImplementation(work_dao)

current_work_id = 1
test_work = Work(0, "test name", "test description")
update_work = Work(current_work_id, "updated name", "updated description")

def test_get_all_work_none_found():
    try:
        work_sao.get_all_work()
        assert False
    except CustomError as error:
        assert str(error) == "No works found, please try again!"

def test_create_work_name_not_string():
    try:
        work = Work(0, 0, "test")
        work_sao.create_work(work)
        assert False
    except CustomError as error:
        assert str(error) == "The name field must be a string, please try again!"

def test_create_work_name_too_long():
    try:
        work = Work(0, "this is too long and so it will fail and raise the desired error message", "test")
        work_sao.create_work(work)
        assert False
    except CustomError as error:
        assert str(error) == "The name field cannot exceed 60 characters, please try again!"

def test_create_work_description_not_string():
    try:
        work = Work(0, "test", 0)
        work_sao.create_work(work)
        assert False
    except CustomError as error:
        assert str(error) == "The description field must be a string, please try again!"

def test_create_work_description_too_long():
    try:
        work = Work(0, "test", "this is too long and so it should get caught and raise the desired error message so "
                               "that this test then passes, this is too long and so it should get caught and raise the "
                               "desired error message so that this test then passes, this is too long and so it should "
                               "get caught and raise the desired error message so that this test then passes")
        work_sao.create_work(work)
        assert False
    except CustomError as error:
        assert str(error) == "The description field cannot exceed 255 characters, please try again!"

def test_create_work_description_empty():
    try:
        work = Work(0, "test", "")
        work_sao.create_work(work)
        assert False
    except CustomError as error:
        assert str(error) == "The description field cannot be left empty, please try again!"

def test_create_work_success():
    result = work_sao.create_work(test_work)
    assert result.work_id != 0

def test_get_work_id_not_integer():
    try:
        work_sao.get_work("")
        assert False
    except CustomError as error:
        assert str(error) == "The work ID field must be an integer, please try again!"

def test_get_work_not_found():
    try:
        work_sao.get_work(-43762899374)
        assert False
    except CustomError as error:
        assert str(error) == "Work not found, please try again!"

def test_get_work_success():
    result = work_sao.get_work(test_work.work_id)
    assert result is not None

def test_get_all_work_success():
    result = work_sao.get_all_work()
    assert len(result) > 0

def test_update_work_id_not_integer():
    try:
        work = Work("0", "test", "test")
        work_sao.update_work(work)
        assert False
    except CustomError as error:
        assert str(error) == "The work ID field must be an integer, please try again!"

def test_update_work_not_found():
    try:
        work = Work(-8764427892653, "test", "test")
        work_sao.update_work(work)
        assert False
    except CustomError as error:
        assert str(error) == "Work not found, please try again!"

def test_update_work_name_not_string():
    try:
        work = Work(current_work_id, 1, "test")
        work_sao.update_work(work)
        assert False
    except CustomError as error:
        assert str(error) == "The name field must be a string, please try again!"

def test_update_work_name_too_long():
    try:
        work = Work(current_work_id, "this is too long and so it should get caught and raise the desired error", "test")
        work_sao.update_work(work)
        assert False
    except CustomError as error:
        assert str(error) == "The name field cannot exceed 60 characters please try again!"

def test_update_work_description_not_string():
    try:
        work = Work(current_work_id, "test", 1)
        work_sao.update_work(work)
        assert False
    except CustomError as error:
        assert str(error) == "The description field must be a string, please try again!"

def test_update_work_description_too_long():
    try:
        work = Work(current_work_id, "test", "this is too long and so it should get caught and raise the desired "
                                             "error, this is too long and so it should get caught and raise the "
                                             "desired error, this is too long and so it should get caught and raise "
                                             "the desired error, this is too long and so it should get caught and "
                                             "raise the desired error")
        work_sao.update_work(work)
        assert False
    except CustomError as error:
        assert str(error) == "The description field cannot exceed 255 characters, please try again!"

def test_update_work_description_empty():
    try:
        work = Work(current_work_id, "test", "")
        work_sao.update_work(work)
        assert False
    except CustomError as error:
        assert str(error) == "The description field cannot be left empty, please try again!"

def test_update_work_success():
    result = work_sao.update_work(update_work)
    assert result

def test_delete_work_id_not_integer():
    try:
        work_sao.delete_work("")
        assert False
    except CustomError as error:
        assert str(error) == "The work ID field must be an integer, please try again!"

def test_delete_work_not_found():
    try:
        work_sao.delete_work(-487662289294874)
        assert False
    except CustomError as error:
        assert str(error) == "Work not found, please try again!"

def test_delete_work_success():
    result = work_sao.delete_work(test_work.work_id)
    assert result
