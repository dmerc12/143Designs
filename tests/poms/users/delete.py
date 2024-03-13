from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POMs for delete user page
class DeleteUserPage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for clicking delete account button
    def click_delete_account_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'deleteUserButton')
        return element.click()
