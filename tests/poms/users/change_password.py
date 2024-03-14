from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POMs for change password page
class ChangePasswordPage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for entering password 1 input
    def enter_password1_input(self, password1):
        element: WebElement = self.driver.find_element(By.ID, 'new_password1')
        return element.send_keys(password1)

    ## POM for entering password 2 input
    def enter_password2_input(self, password2):
        element: WebElement = self.driver.find_element(By.ID, 'new_password2')
        return element.send_keys(password2)

    ## POM for clicking change password button
    def click_change_password_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'changePasswordButton')
        return element.click()
