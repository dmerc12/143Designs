from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from SAL.UserSAL.UserSALImplementation import UserSALImplementation
from Entities.CustomError import CustomError
from Entities.User import User

user_dao = UserDALImplementation()
user_sao = UserSALImplementation(user_dao)

current_user_id = 1

successful_user = User(0, "another@email.com", "password")
successful_confirmation = "password"
updated_user = User(current_user_id, "updated@email.com", "updated")
updated_confirmation = "updated"

def test_create_user_password_not_string():
    try:
        test_user = User(0, "test@email.com", 0)
        user_sao.create_user(test_user, successful_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "The password field must be a string, please try again!"

def test_create_user_password_empty():
    try:
        test_user = User(0, "test@email.com", "")
        user_sao.create_user(test_user, successful_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "The password field cannot be left  empty, please try again!"

def test_create_user_password_too_long():
    try:
        test_user = User(0, "test@email.com", "this is much too long and so it should fail and get the desired error")
        user_sao.create_user(test_user, successful_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "The password field cannot exceed 60 characters, please try again!"

def test_create_user_confirmation_password_empty():
    try:
        user_sao.create_user(successful_user, "")
        assert False
    except CustomError as error:
        assert str(error) == "The confirmation password field cannot be left empty, please try again!"

def test_create_user_confirmation_password_too_long():
    try:
        user_sao.create_user(successful_user, "this is much too long and so it should fail and get the desired error")
        assert False
    except CustomError as error:
        assert str(error) == "The confirmation password field cannot exceed 60 characters, please try again!"

def test_create_user_confirmation_password_not_string():
    try:
        user_sao.create_user(successful_user, 6)
        assert False
    except CustomError as error:
        assert str(error) == "The confirmation password field must be a string, please try again!"

def test_create_user_email_not_string():
    try:
        test_user = User(0, 0, "password")
        user_sao.create_user(test_user, successful_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "The email field must be a string, please try again!"

def test_create_user_email_too_long():
    try:
        test_user = User(0, "this is much too long and so it should fail and get the desired error", "password")
        user_sao.create_user(test_user, successful_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "The email field cannot exceed 60 characters, please try again!"

def test_create_user_email_empty():
    try:
        test_user = User(0, "", "password")
        user_sao.create_user(test_user, successful_confirmation)
        assert False
    except CustomError as error:
        assert str(error) == "The email field cannot be left empty, please try again!"

def test_create_user_confirmation_password_not_matching_password():
    try:
        user_sao.create_user(successful_user, "not going to work")
        assert False
    except CustomError as error:
        assert str(error) == "The passwords do not match, please try again!"

def test_create_user_already_exists():
    try:
        test_user = User(0, "test@email.com", "password")
        user_sao.create_user(test_user, "password")
        assert False
    except CustomError as error:
        assert str(error) == "A user already exists with this email, please log in!"

def test_create_user_success():
    result = user_sao.create_user(successful_user, successful_confirmation)
    assert result.user_id != 0

def test_get_user_by_id_not_integer():
    try:
        user_sao.get_user_by_id("this won't work")
        assert False
    except CustomError as error:
        assert str(error) == "User ID field must be an integer, please try again!"

def test_get_user_by_id_not_found():
    try:
        user_sao.get_user_by_id(-500000)
        assert False
    except CustomError as error:
        assert str(error) == "This user cannot be found, please try again!"

def test_get_user_by_id_success():
    result = user_sao.get_user_by_id(current_user_id)
    assert result is not None

def test_get_user_by_email_not_a_string():
    try:
        user_sao.get_user_by_email(50)
        assert False
    except CustomError as error:
        assert str(error) == "Email field must be a string, please try again!"

def test_get_user_by_email_success():
    result = user_sao.get_user_by_email(successful_user.email)
    assert result is not None

def test_login_email_not_string():
    try:
        user_sao.login(0, successful_user.password)
        assert False
    except CustomError as error:
        assert str(error) == "The email field must be a string, please try again!"

def test_login_email_empty():
    try:
        user_sao.login("", successful_user.password)
        assert False
    except CustomError as error:
        assert str(error) == "The email field cannot be left empty, please try again!"

def test_login_password_not_string():
    try:
        user_sao.login(successful_user.email, 0)
        assert False
    except CustomError as error:
        assert str(error) == "The password field must be a string, please try again!"

def test_login_password_empty():
    try:
        user_sao.login(successful_user.email, "")
        assert False
    except CustomError as error:
        assert str(error) == "The password field cannot be left empty, please try again!"

def test_login_email_or_password_incorrect():
    try:
        user_sao.login("incorrect", "credentials")
        assert False
    except CustomError as error:
        assert str(error) == "Either the email or password are incorrect, please try again!"

def test_login_success():
    result = user_sao.login("another@email.com", "password")
    assert result is not None

def test_update_email_not_string():
    try:
        test_user = User(current_user_id, 0, "password")
        user_sao.update_email(test_user)
        assert False
    except CustomError as error:
        assert str(error) == "The email field must be a string, please try again!"

def test_update_email_empty():
    try:
        test_user = User(current_user_id, "", "password")
        user_sao.update_email(test_user)
        assert False
    except CustomError as error:
        assert str(error) == "The email field cannot be empty, please try again!"

def test_update_email_too_long():
    try:
        test_user = User(current_user_id, "this is much too long and so it should fail and get the desired error",
                         "password")
        user_sao.update_email(test_user)
        assert False
    except CustomError as error:
        assert str(error) == "The email field cannot exceed 60 characters, please try again!"

def test_update_email_no_info_changed():
    try:
        test_user = User(current_user_id, successful_user.email, successful_user.password)
        user_sao.update_email(test_user)
        assert False
    except CustomError as error:
        assert str(error) == "No information has changed!"

def test_update_email_success():
    result = user_sao.update_email(updated_user)
    assert result

def test_change_password_user_not_found():
    try:
        test_user = User(-4767526382987, "test@email.com", "new")
        user_sao.change_password(test_user, "new")
        assert False
    except CustomError as error:
        assert str(error) == "This user cannot be found, please try again!"

def test_change_password_password_new_password_not_string():
    try:
        test_user = User(0, "test@email.com", 0)
        user_sao.change_password(test_user, "new")
        assert False
    except CustomError as error:
        assert str(error) == "The password field must be a string, please try again!"

def test_change_password_password_new_password_empty():
    try:
        test_user = User(0, "test@email.com", "")
        user_sao.change_password(test_user, "new")
        assert False
    except CustomError as error:
        assert str(error) == "The password field cannot be left empty, please try again!"

def test_change_password_password_new_password_too_long():
    try:
        test_user = User(0, "test@email.com", "this is much too long and so it should fail and get the desired error")
        user_sao.change_password(test_user, "new")
        assert False
    except CustomError as error:
        assert str(error) == "The password field cannot exceed 60 characters, please try again!"

def test_change_password_confirmation_password_not_string():
    try:
        user_sao.change_password(updated_user, -5000000)
        assert False
    except CustomError as error:
        assert str(error) == "The confirmation password field must be a string, please try again!"

def test_change_password_password_confirmation_password_empty():
    try:
        user_sao.change_password(updated_user, "")
        assert False
    except CustomError as error:
        assert str(error) == "The confirmation password cannot be left empty, please try again!"

def test_change_password_password_confirmation_password_too_long():
    try:
        user_sao.change_password(updated_user, "this is much too long and so it should fail and get the desired error")
        assert False
    except CustomError as error:
        assert str(error) == "The confirmation password field cannot exceed 60 characters, please try again!"

def test_change_password_user_id_not_integer():
    try:
        test_user = User("this won't work", updated_user.email, updated_user.password)
        user_sao.change_password(test_user, "new")
        assert False
    except CustomError as error:
        assert str(error) == "The user ID field must be an integer, please try again!"

def test_change_password_new_password_does_not_match_confirmation_password():
    try:
        user_sao.change_password(updated_user, "not matching")
        assert False
    except CustomError as error:
        assert str(error) == "The passwords don't match, please try again!"

def test_change_password_nothing_changed():
    try:
        test_user = User(current_user_id, successful_user.email, "password")
        user_sao.change_password(test_user, "password")
        assert False
    except CustomError as error:
        assert str(error) == "Nothing has changed, please try again!"

def test_change_password_success():
    result = user_sao.change_password(updated_user, "updated")
    assert result

def test_delete_user_not_found():
    try:
        user_sao.delete_user(-500000)
        assert False
    except CustomError as error:
        assert str(error) == "This user cannot be found, please try again!"

def test_delete_user_success():
    result = user_sao.delete_user(current_user_id)
    assert result
