from datetime import datetime, timedelta

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from Entities.CustomError import CustomError
from Entities.Session import Session

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

success_session = Session(0, -1, datetime.now() + timedelta(minutes=15))
update_session = Session(success_session.session_id, success_session.user_id, datetime.now() + timedelta(minutes=15))

def test_create_session_user_id_not_integer():
    try:
        test_session = Session(0, "-1", datetime.now() + timedelta(minutes=15))
        session_sao.create_session(test_session)
        assert False
    except CustomError as error:
        assert str(error) == "The user ID field must be an integer, please try again!"

def test_create_session_user_not_found():
    try:
        test_session = Session(0, -50000000, datetime.now() + timedelta(minutes=15))
        session_sao.create_session(test_session)
        assert False
    except CustomError as error:
        assert str(error) == "This user cannot be found, please try again!"

def test_create_session_expiration_date_time_not_datetime():
    try:
        test_session = Session(0, -1, str(datetime.now() + timedelta(minutes=15)))
        session_sao.create_session(test_session)
        assert False
    except CustomError as error:
        assert str(error) == "The expiration field must be a datetime, please try again!"

def test_update_session_expiration_expired():
    try:
        test_session = Session(success_session.session_id, -1, datetime.now() - timedelta(minutes=15))
        session_sao.create_session(test_session)
        assert False
    except CustomError as error:
        assert str(error) == "The expiration field must be in the future, please try again!"

def test_create_session_success():
    result = session_sao.create_session(success_session)
    assert result.session_id != 0

def test_get_session_id_not_integer():
    try:
        session_sao.get_session("10")
        assert False
    except CustomError as error:
        assert str(error) == "The session ID field must be an integer, please try again!"

def test_get_session_not_found():
    try:
        session_sao.get_session(-500000000000)
        assert False
    except CustomError as error:
        assert str(error) == "No session found, please try again!"

def test_get_session_expired():
    try:
        result = session_sao.get_session(-1)
        print(result)
        assert False
    except CustomError as error:
        assert str(error) == "Session has expired, please log in!"

def test_get_session_success():
    result = session_sao.get_session(success_session.session_id)
    assert result is not None

def test_update_session_session_id_not_integer():
    try:
        test_session = Session("0", -1, datetime.now() + timedelta(minutes=15))
        session_sao.update_session(test_session)
        assert False
    except CustomError as error:
        assert str(error) == "The session ID field must be an integer, please try again!"

def test_update_session_user_id_not_integer():
    try:
        test_session = Session(success_session.session_id, "-1", datetime.now() + timedelta(minutes=15))
        session_sao.update_session(test_session)
        assert False
    except CustomError as error:
        assert str(error) == "The user ID field must be an integer, please try again!"

def test_update_session_expiration_not_datetime():
    try:
        test_session = Session(success_session.session_id, -1, str(datetime.now() + timedelta(minutes=15)))
        session_sao.update_session(test_session)
        assert False
    except CustomError as error:
        assert str(error) == "The expiration field must be a datetime, please try again!"

def test_update_session_expired():
    try:
        test_session = Session(-1, -1, datetime.now() + timedelta(minutes=15))
        session_sao.update_session(test_session)
        assert False
    except CustomError as error:
        assert str(error) == "Session has expired, please log in!"

def test_update_session_session_not_found():
    try:
        test_session = Session(-688085432234567, -1, datetime.now() + timedelta(minutes=15))
        session_sao.update_session(test_session)
        assert False
    except CustomError as error:
        assert str(error) == "No session found, please try again!"

def test_update_session_user_not_found():
    try:
        test_session = Session(-1, -6756432123456789876, datetime.now() + timedelta(minutes=15))
        session_sao.update_session(test_session)
        assert False
    except CustomError as error:
        assert str(error) == "This user cannot be found, please try again!"

def test_update_session_expiration_past():
    try:
        test_session = Session(success_session.session_id, -1, datetime.now() - timedelta(minutes=15))
        session_sao.update_session(test_session)
        assert False
    except CustomError as error:
        assert str(error) == "The expiration field must be in the future, please try again!"

def test_update_session_success():
    result = session_sao.update_session(update_session)
    assert result

def test_delete_session_id_not_integer():
    try:
        session_sao.delete_session("1")
        assert False
    except CustomError as error:
        assert str(error) == "The session ID field must be an integer, please try again!"

def test_delete_session_not_found():
    try:
        session_sao.delete_session(-5000000000)
        assert False
    except CustomError as error:
        assert str(error) == "No session found, please try again!"

def test_delete_session_success():
    result = session_sao.delete_session(success_session.session_id)
    assert result

def test_delete_all_sessions_user_id_not_integer():
    try:
        session_sao.delete_all_sessions("-1")
        assert False
    except CustomError as error:
        assert str(error) == "The user ID field must be an integer, please try again!"

def test_delete_all_sessions_user_not_found():
    try:
        session_sao.delete_all_sessions(-568783909876537892)
        assert False
    except CustomError as error:
        assert str(error) == "This user cannot be found, please try again!"

def test_delete_all_sessions_success():
    result = session_sao.delete_all_sessions(-2)
    assert result
    