from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POMs for register page
class RegisterPage():

    def __init__(self, driver: WebDriver):
        self.driver = driver
        