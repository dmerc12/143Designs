from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POMs for login page
class LoginPage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for clicking register link
    def click_register_link(self):
        element: WebElement = self.driver.find_element(By.ID, 'registerLink')
        return element.click()
        
    ## POM for entering username input
    def enter_username_input(self, username):
        element: WebElement = self.driver.find_element(By.ID, 'username')
        return element.send_keys(username)

    ## POM for entering password input
    def enter_password2_input(self, password):
        element: WebElement = self.driver.find_element(By.ID, 'password')
        return element.send_keys(password)

    ## POM for clicking login button
    def click_login_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'loginButton')
        return element.click()
