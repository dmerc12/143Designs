import logging
import os
from flask import Flask
from flask_cors import CORS

from API.UserRoutes.CreateUserRoute import create_user_route
from API.UserRoutes.LoginRoute import login_route
from API.UserRoutes.LogoutRoute import logout_route
from API.UserRoutes.GetAllUsersRoute import get_users_route
from API.UserRoutes.UpdateEmailRoute import update_email_route
from API.UserRoutes.ChangePasswordRoute import change_password_route
from API.UserRoutes.DeleteUserRoute import delete_user_route

from API.ItemRoutes.CreateItemRoute import create_item_route
from API.ItemRoutes.GetAllItemsRoute import get_items_route
from API.ItemRoutes.UpdateItemRoute import update_item_route
from API.ItemRoutes.DeleteItemRoute import delete_item_route

def create_back_end_api(config):
    app: Flask = Flask(__name__)
    CORS(app)
    app.config.from_object(config)

    log_level = logging.DEBUG
    for handler in app.logger.handlers:
        app.logger.removeHandler(handler)
    log_directory = os.path.join("Logs")
    os.makedirs(log_directory, exist_ok=True)
    log_file = os.path.join(log_directory, "143DesignsLogs.log")
    handler = logging.FileHandler(log_file)
    handler.setLevel(log_level)
    formatter = logging.Formatter('%s(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)

    app.register_blueprint(create_user_route)
    app.register_blueprint(login_route)
    app.register_blueprint(logout_route)
    app.register_blueprint(get_users_route)
    app.register_blueprint(update_email_route)
    app.register_blueprint(change_password_route)
    app.register_blueprint(delete_user_route)

    app.register_blueprint(create_item_route)
    app.register_blueprint(get_items_route)
    app.register_blueprint(update_item_route)
    app.register_blueprint(delete_item_route)

    return app
    