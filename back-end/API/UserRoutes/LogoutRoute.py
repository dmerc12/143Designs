from flask import Blueprint, current_app, jsonify, request

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from Entities.CustomError import CustomError

logout_route = Blueprint("logout_route", __name__)

session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@logout_route.route("/api/logout", methods=["DELETE"])
def logout_route():
    try:
        session_id = request.json.get("sessionId")
        current_app.logger.info("Beginning API function logout with session ID: " + str(session_id))
        result = session_sao.delete_session(session_id)
        current_app.logger.info("Finishing API function logout with result: " + str(result))
        return jsonify(result), 200
    except CustomError as error:
        current_app.logger.error("Error with API function logout with error: " + str(error))
        return jsonify({"message": str(error)}), 400
