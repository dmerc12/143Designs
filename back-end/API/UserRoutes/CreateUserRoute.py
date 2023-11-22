from flask import Blueprint, current_app, jsonify, request

from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from SAL.UserSAL.UserSALImplementation import UserSALImplementation
from Entities.CustomError import CustomError
from Entities.User import User

create_user_route = Blueprint("create_user_route", __name__)

user_dao = UserDALImplementation()
user_sao = UserSALImplementation(user_dao)

@create_user_route.route("/api/create/user", methods=["POST"])
def create_user_route():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function create user with info: " + str(request_info))
        new_user = User(user_id=0, email=request_info["email"], password=request_info["password"])
        confirmation_password = request_info["confirmationPassword"]
        user = user_sao.create_user(new_user, confirmation_password)
        current_app.logger.info("Finishing API function create user with user: " + str(user.convert_to_dictionary()))
        return jsonify(user.convert_to_dictionary()), 201
    except CustomError as error:
        current_app.logger.error("Finishing API function create user with error: " + str(error))
        return jsonify({"message": str(error)}), 400
