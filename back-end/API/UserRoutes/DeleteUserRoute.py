from flask import Blueprint, current_app, jsonify, request

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from SAL.UserSAL.UserSALImplementation import UserSALImplementation
from Entities.CustomError import CustomError

delete_user_route = Blueprint("delete_user_route", __name__)

user_dao = UserDALImplementation()
user_sao = UserSALImplementation(user_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@delete_user_route.route("/api/delete/user", methods=["DELETE"])
def delete_user():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function delete user with info: " + str(request_info))
        session = session_sao.get_session(request_info["sessionId"])
        session_sao.delete_all_sessions(session.user_id)
        result = user_sao.delete_user(session.user_id)
        current_app.logger.info("Finishing API function delete user with result: " + str(result))
        return jsonify(result), 200
    except CustomError as error:
        current_app.logger.error("Error with API function delete user with error: " + str(error))
        return jsonify({"message": str(error)}), 400
