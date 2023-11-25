from datetime import timedelta, datetime

from flask import Blueprint, current_app, jsonify, request

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from SAL.UserSAL.UserSALImplementation import UserSALImplementation
from Entities.CustomError import CustomError
from Entities.User import User

update_email_route = Blueprint("update_email_route", __name__)

user_dao = UserDALImplementation()
user_sao = UserSALImplementation(user_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@update_email_route.route("/api/update/email", methods=["PUT"])
def update_email_route():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function update email with info: " + str(request_info))
        session = session_sao.get_session(request_info["sessionId"])
        user = User(user_id=session.user_id, email=request_info["email"], password="null")
        result = user_sao.update_email(user)
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        current_app.logger.info("Finishing API function update email with result: " + str(result))
        return jsonify(result), 200
    except CustomError as error:
        current_app.logger.error("Error with API function update email with error: " + str(error))
        return jsonify({"message": str(error)}), 400
