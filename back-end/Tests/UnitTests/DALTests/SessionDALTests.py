from datetime import datetime, timedelta

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from Entities.Session import Session

session_dao = SessionDALImplementation()
test_session = Session(0, -1, datetime.now() + timedelta(minutes=15))
update_session = Session(test_session.session_id, test_session.user_id, datetime.now() + timedelta(15))

def test_create_session_success():
    result = session_dao.create_session(test_session)
    assert result.session_id != 0

def test_get_session_success():
    result = session_dao.get_session(test_session.session_id)
    assert result is not None

def test_update_session_success():
    result = session_dao.update_session(update_session)
    assert result

def test_delete_session_success():
    result = session_dao.delete_session(test_session.session_id)
    assert result

def test_delete_all_sessions_success():
    result = session_dao.delete_all_sessions(-2)
    assert result
