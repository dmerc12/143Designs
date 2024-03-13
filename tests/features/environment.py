from selenium.webdriver.edge.webdriver import WebDriver
from poms.users.update_user import UpdateUserPage
from .cleanup import cleanup_test_environment
from poms.users.register import RegisterPage
from .setup import setup_test_environment
from poms.users.login import LoginPage
from behave.runner import Context

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

    ## Inventory tracking POMs

    ## Order tracking POMs

    ## Site management POMs

    ## Store POMs

    ## Navigation POMs

    # Implicit wait for elements
    context.driver.implicitly_wait(1)

# Cleanup for webdriver after selenium tests
def after_all(context: Context):
    # Close Webdriver
    context.driver.close()

    # Cleanup test environment
    cleanup_test_environment()
