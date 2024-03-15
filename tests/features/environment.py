from poms.users.change_password import ChangePasswordPage
from selenium.webdriver.edge.webdriver import WebDriver
from poms.site_management.contact import ContactPage
from poms.users.update_user import UpdateUserPage
from .cleanup import cleanup_test_environment
from poms.users.register import RegisterPage
from poms.users.delete import DeleteUserPage
from .setup import setup_test_environment
from poms.users.login import LoginPage
from behave.runner import Context
from poms.navbar import NavBar

# Setup for webdriver and POM files before selenium tests
def before_all(context: Context):
    # Setup test environment
    setup_test_environment()

    # Setup webdriver
    context.driver = WebDriver()

    # Register POM files below
    ## Users POMsgit
    context.register_poms = RegisterPage(context.driver)
    context.login_poms = LoginPage(context.driver)
    context.update_user_poms = UpdateUserPage(context.driver)
    context.delete_user_poms = DeleteUserPage(context.driver)
    context.change_password_poms = ChangePasswordPage(context.driver)

    ## Inventory tracking POMs

    ## Order tracking POMs

    ## Site management POMs
    context.contact_poms = ContactPage(context.driver)

    ## Store POMs

    ## Navigation POMs
    context.navbar_poms = NavBar(context.driver)

    # Implicit wait for elements
    context.driver.implicitly_wait(1)

# Cleanup for webdriver after selenium tests
def after_all(context: Context):
    # Close Webdriver
    context.driver.close()

    # Cleanup test environment
    cleanup_test_environment()
