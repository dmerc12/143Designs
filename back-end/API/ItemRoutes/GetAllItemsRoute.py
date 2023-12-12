from datetime import timedelta, datetime

from flask import Blueprint, current_app, jsonify, request

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from DAL.ItemDAL.ItemDALImplementation import ItemDALImplementation
from SAL.ItemSAL.ItemSALImplementation import ItemSALImplementation
from Entities.CustomError import CustomError

get_items_route = Blueprint("get_items_route", __name__)

item_dao = ItemDALImplementation()
item_sao = ItemSALImplementation(item_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@get_items_route.route("/api/get/items", methods=["PATCH"])
def get_items():
    try:
        session_id = request.json.get("sessionId")
        current_app.logger.info("Beginning API function get all items with session ID: " + str(session_id))
        session = session_sao.get_session(session_id)
        items = item_sao.get_all_items()
        items = [item.convert_to_dictionary() for item in items]
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        current_app.logger.info("Finishing API function get all items")
        return jsonify(items), 200
    except CustomError as error:
        current_app.logger.error("Error with API function get all items with error: " + str(error))
        return jsonify({"message": str(error)}), 400
