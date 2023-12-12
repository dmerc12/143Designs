from datetime import timedelta, datetime

from flask import Blueprint, current_app, jsonify, request

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from DAL.ItemDAL.ItemDALImplementation import ItemDALImplementation
from SAL.ItemSAL.ItemSALImplementation import ItemSALImplementation
from Entities.CustomError import CustomError

delete_item_route = Blueprint("delete_item_route", __name__)

item_dao = ItemDALImplementation()
item_sao = ItemSALImplementation(item_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@delete_item_route.route("/api/delete/item", methods=["DELETE"])
def delete_item():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function delete item with info: " + str(request_info))
        session = session_sao.get_session(request_info["sessionId"])
        result = item_sao.delete_item(request_info["itemId"])
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        current_app.logger.info("Finishing API function delete item with result: " + str(result))
        return jsonify(result), 200
    except CustomError as error:
        current_app.logger.error("Error with API function delete item with error: " + str(error))
        return jsonify({"message": str(error)}), 400
