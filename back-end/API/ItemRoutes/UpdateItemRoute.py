from datetime import timedelta, datetime

from flask import Blueprint, current_app, jsonify, request

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from DAL.ItemDAL.ItemDALImplementation import ItemDALImplementation
from SAL.ItemSAL.ItemSALImplementation import ItemSALImplementation
from Entities.CustomError import CustomError
from Entities.Item import Item

update_item_route = Blueprint("update_item_route", __name__)

item_dao = ItemDALImplementation()
item_sao = ItemSALImplementation(item_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@update_item_route.route("/api/update/item", methods=["PUT"])
def update_item():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function update item with info: " + str(request_info))
        session = session_sao.get_session(request_info["sessionId"])
        item = Item(item_id=request_info["itemId"], item_name=request_info["itemName"])
        result = item_sao.update_item(item)
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        current_app.logger.info("Finishing API function update item with result: " + str(result))
        return jsonify(result), 200
    except CustomError as error:
        current_app.logger.error("Error with API function update item with error: " + str(error))
        return jsonify({"message": str(error)}), 400
