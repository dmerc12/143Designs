from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from Entities.User import User

user_dao = UserDALImplementation()
test_user = User(0, "new@email.com", "test")
updated_user = User(test_user.user_id, "updated@email.com", "updated")

def test_create_user_success():
    result = user_dao.create_user(test_user)
    assert result.user_id != 0

def test_get_user_by_id_success():
    result = user_dao.get_user_by_id(test_user.user_id)
    assert result is not None

def test_get_user_by_email_success():
    result = user_dao.get_user_by_email(test_user.email)
    assert result is not None

def test_login_success():
    result = user_dao.login(test_user.email, test_user.password)
    assert result is not None

def test_update_email_success():
    result = user_dao.update_email(updated_user)
    assert result.user_id == test_user.user_id and result.email != test_user.email

def test_change_password_success():
    result = user_dao.change_password(updated_user)
    assert result

def test_delete_user_success():
    result = user_dao.delete_user(test_user.user_id)
    assert result
