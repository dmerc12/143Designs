from datetime import timedelta, datetime

from flask import Blueprint, current_app, jsonify, request

from DAL.ItemDAL.ItemDALImplementation import ItemDALImplementation
from SAL.ItemSAL.ItemSALImplementation import ItemSALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from Entities.CustomError import CustomError
from Entities.Item import Item

create_item_route = Blueprint("create_item_route", __name__)

item_dao = ItemDALImplementation()
item_sao = ItemSALImplementation(item_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@create_item_route.route("/api/create/item", methods=["POST"])
def create_item():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function create item with info: " + str(request_info))
        session = session_sao.get_session(request_info["sessionId"])
        new_item = Item(item_id=0, item_name=request_info["itemName"])
        item = item_sao.create_item(new_item)
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        current_app.logger.info("Finishing API function create item with item: " + str(item.convert_to_dictionary()))
        return jsonify(item.convert_to_dictionary()), 201
    except CustomError as error:
        current_app.logger.error("Finishing API function create item with error: " + str(error))
        return jsonify({"message": str(error)}), 400
