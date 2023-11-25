from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from Entities.CustomError import CustomError
from Entities.User import User
from SAL.UserSAL.UserSALImplementation import UserSALImplementation

user_dao = UserDALImplementation()
user_sao = UserSALImplementation(user_dao)

success_user = User(0, "new@email.com", "test")
update_user = User(success_user.user_id, "updated@email.com", "updated")

def test_create_user_email_not_string():
    try:
        test_user = User(0, 0, "password")
        user_sao.create_user(test_user, test_user.password)
        assert False
    except CustomError as error:
        assert str(error) == "The email field must be a string, please try again!"

def test_create_user_email_too_long():
    try:
        test_user = User(0, "this has too many characters and so it should raise the desired exception", "password")
        user_sao.create_user(test_user, test_user.password)
        assert False
    except CustomError as error:
        assert str(error) == "The email field cannot exceed 60 characters, please try again!"

def test_create_user_email_empty():
    try:
        test_user = User(0, "", "password")
        user_sao.create_user(test_user, test_user.password)
        assert False
    except CustomError as error:
        assert str(error) == "The email field cannot be left empty, please try again!"

def test_create_user_password_not_string():
    try:
        test_user = User(0, "test@email.com", 0)
        user_sao.create_user(test_user, test_user.password)
        assert False
    except CustomError as error:
        assert str(error) == "The password field must be a string, please try again!"

def test_create_user_password_empty():
    try:
        test_user = User(0, "test@email.com", "")
        user_sao.create_user(test_user, test_user.password)
        assert False
    except CustomError as error:
        assert str(error) == "The password field cannot be left  empty, please try again!"

def test_create_user_password_too_long():
    try:
        test_user = User(0, "test@email.com", "this is much too long and so it should fail and get the "
                                              "desired error message")
        user_sao.create_user(test_user, test_user.password)
        assert False
    except CustomError as error:
        assert str(error) == "The password field cannot exceed 60 characters, please try again!"

def test_create_user_confirmation_password_empty():
    try:
        test_user = User(0, "test@email.com", "password")
        user_sao.create_user(test_user, "")
        assert False
    except CustomError as error:
        assert str(error) == "The confirmation password field cannot be left empty, please try again!"

def test_create_user_confirmation_password_not_string():
    try:
        test_user = User(0, "test@email.com", "test")
        user_sao.create_user(test_user, 6)
        assert False
    except CustomError as error:
        assert str(error) == "The confirmation password field must be a string, please try again!"

def test_create_user_confirmation_password_not_matching_password():
    try:
        user_sao.create_user(success_user, "nope")
        assert False
    except CustomError as error:
        assert str(error) == "The passwords do not match, please try again!"

def test_create_user_already_exists():
    try:
        test_user = User(0, "password", "test@email.com")
        user_sao.create_user(test_user, test_user.password)
        assert False
    except CustomError as error:
        assert str(error) == "A user already exists with this email, please log in!"

def test_create_user_success():
    result = user_sao.create_user(success_user, success_user.password)
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
    result = user_sao.get_user_by_id(success_user.user_id)
    assert result is not None

def test_get_user_by_email_not_a_string():
    try:
        user_sao.get_user_by_email(50)
        assert False
    except CustomError as error:
        assert str(error) == "Email field must be a string, please try again!"

def test_get_user_by_email_success():
    result = user_sao.get_user_by_email(success_user.email)
    assert result is not None

def test_login_email_not_string():
    try:
        user_sao.login(0, success_user.password)
        assert False
    except CustomError as error:
        assert str(error) == "The email field must be a string, please try again!"

def test_login_email_empty():
    try:
        user_sao.login("", success_user.password)
        assert False
    except CustomError as error:
        assert str(error) == "The email field cannot be left empty, please try again!"

def test_login_password_not_string():
    try:
        user_sao.login(success_user.email, 0)
        assert False
    except CustomError as error:
        assert str(error) == "The password field must be a string, please try again!"

def test_login_password_empty():
    try:
        user_sao.login(success_user.email, "")
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
    result = user_sao.login("test@email.com", "test")
    assert result is not None

def test_update_email_not_string():
    try:
        test_user = User(success_user.user_id, 0, "password")
        user_sao.update_email(test_user)
        assert False
    except CustomError as error:
        assert str(error) == "The email field must be a string, please try again!"

def test_update_email_empty():
    try:
        test_user = User(success_user.user_id, "", "password")
        user_sao.update_email(test_user)
        assert False
    except CustomError as error:
        assert str(error) == "The email field cannot be empty, please try again!"

def test_update_email_too_long():
    try:
        test_user = User(success_user.user_id, "this has too many characters so it should raise the desired exception",
                         "password")
        user_sao.update_email(test_user)
        assert False
    except CustomError as error:
        assert str(error) == "The email field cannot exceed 60 characters, please try again!"

def test_update_email_no_info_changed():
    try:
        user_sao.update_email(success_user)
        assert False
    except CustomError as error:
        assert str(error) == "No information has changed!"

def test_update_email_success():
    result = user_sao.update_email(update_user)
    assert result.user_id == success_user.user_id and result.email != success_user.email

def test_change_password_user_not_found():
    try:
        test_user = User(-3768738909834, "test@email.com", "test")
        user_sao.change_password(test_user, "new")
        assert False
    except CustomError as error:
        assert str(error) == "This user cannot be found, please try again!"

def test_change_password_password_new_password_not_string():
    try:
        test_user = User(success_user.user_id, "test@email.com", 548792)
        user_sao.change_password(test_user, "new")
        assert False
    except CustomError as error:
        assert str(error) == "The new password field must be a string, please try again!"

def test_change_password_password_new_password_empty():
    try:
        test_user = User(success_user.user_id, "test@email.com", "")
        user_sao.change_password(test_user, "new")
        assert False
    except CustomError as error:
        assert str(error) == "The new password field cannot be left empty, please try again!"

def test_change_password_password_new_password_too_long():
    try:
        test_user = User(success_user.user_id, "test@email.com", "this is too long and so it should raise the "
                                                                 "desired error message")
        user_sao.change_password(test_user, "new")
        assert False
    except CustomError as error:
        assert str(error) == "The new password field cannot exceed 60 characters, please try again!"

def test_change_password_confirmation_password_not_string():
    try:
        test_user = User(success_user.user_id, "test@email.com", "test")
        user_sao.change_password(test_user, -5000000)
        assert False
    except CustomError as error:
        assert str(error) == "The confirmation password field must be a string, please try again!"

def test_change_password_password_confirmation_password_empty():
    try:
        test_user = User(success_user.user_id, "test@email.com", "test")
        user_sao.change_password(test_user, "")
        assert False
    except CustomError as error:
        assert str(error) == "The confirmation password cannot be left empty, please try again!"

def test_change_password_password_confirmation_password_too_long():
    try:
        test_user = User(success_user.user_id, "test@email.com", "test")
        user_sao.change_password(test_user, "this is too long and so it should raise the desired error message")
        assert False
    except CustomError as error:
        assert str(error) == "The confirmation password field cannot exceed 60 characters, please try again!"

def test_change_password_user_id_not_integer():
    try:
        test_user = User("", "test@email.com", "test")
        user_sao.change_password(test_user, test_user.password)
        assert False
    except CustomError as error:
        assert str(error) == "The user ID field must be an integer, please try again!"

def test_change_password_new_password_does_not_match_confirmation_password():
    try:
        test_user = User(success_user.user_id, "test@email.com", "test")
        user_sao.change_password(test_user, "not matching")
        assert False
    except CustomError as error:
        assert str(error) == "The passwords don't match, please try again!"

def test_change_password_nothing_changed():
    try:
        test_user = User(success_user.user_id, "test@email.com", "password")
        user_sao.change_password(test_user, test_user.password)
        assert False
    except CustomError as error:
        assert str(error) == "Nothing has changed, please try again!"

def test_change_password_success():
    result = user_sao.change_password(update_user, update_user.password)
    assert result

def test_delete_user_id_not_integer():
    try:
        user_sao.delete_user("1")
        assert False
    except CustomError as error:
        assert str(error) == "User ID field must be an integer, please try again!"

def test_delete_user_last_user():
    try:
        user_sao.delete_user(-1)
        user_sao.delete_user(-2)
        assert False
    except CustomError as error:
        assert str(error) == "Please create another account first, then try again!"

def test_delete_user_not_found():
    try:
        user_sao.delete_user(-500000)
        assert False
    except CustomError as error:
        assert str(error) == "This user cannot be found, please try again!"

def test_delete_user_success():
    result = user_sao.delete_user(success_user.user_id)
    assert result
