from selenium.webdriver.edge.webdriver import WebDriver
from poms.users.register import RegisterPage
from behave.runner import Context

# Setup for webdriver and POM files before selenium tests
def before_all(context: Context):
    context.driver = WebDriver()

    # Register POM files below
    ## Users POMs
    context.register_poms = RegisterPage(context.driver)

    ## Inventory tracking POMs

    ## Order tracking POMs

    ## Site management POMs

    ## Store POMs

    ## Navigation POMs

    # Implicit wait for elements
    context.driver.implicitly_wait(1)

# Cleanup for webdriver after selenium tests
def after_all(context: Context):
    context.driver.close()
