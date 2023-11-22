from datetime import timedelta, datetime

from flask import Blueprint, current_app, jsonify, request

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from SAL.UserSAL.UserSALImplementation import UserSALImplementation
from Entities.CustomError import CustomError

get_user_route = Blueprint("get_user_route", __name__)

user_dao = UserDALImplementation()
user_sao = UserSALImplementation(user_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@get_user_route.route("/api/get/user", methods=["PATCH"])
def get_user_route():
    try:
        session_id = request.json.get("sessionId")
        current_app.logger.info("Beginning API function get user with session ID: " + str(session_id))
        session = session_sao.get_session(session_id)
        user = user_sao.get_user_by_id(session.user_id)
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        current_app.logger.info("Finishing API function get user with user: " + str(user.convert_to_dictionary()))
        return jsonify(user.convert_to_dictionary()), 200
    except CustomError as error:
        current_app.logger.error("Error with API function get user with error: " + str(error))
        return jsonify({"message": str(error)}), 400
