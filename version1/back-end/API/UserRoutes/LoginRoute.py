from datetime import timedelta, datetime

from flask import Blueprint, current_app, jsonify, request

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from SAL.UserSAL.UserSALImplementation import UserSALImplementation
from Entities.CustomError import CustomError
from Entities.Session import Session

login_route = Blueprint("login_route", __name__)

user_dao = UserDALImplementation()
user_sao = UserSALImplementation(user_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@login_route.route("/api/login", methods=["POST"])
def login():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API functino login with info: " + str(request_info))
        user = user_sao.login(email=request_info["email"], password=request_info["password"])
        session_info = Session("0", user.user_id, datetime.now() + timedelta(minutes=15))
        session = session_sao.create_session(session_info)
        current_app.logger.info("Finishing API function login with session: " + str(session.convert_to_dictionary()))
        return jsonify({"sessionId": session.session_id}), 200
    except CustomError as error:
        current_app.logger.error("Error with API function login with error: " + str(error))
        return jsonify({"message": str(error)}), 400
