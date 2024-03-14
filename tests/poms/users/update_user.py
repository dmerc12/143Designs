from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POMs for update user page
class UpdateUserPage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for entering username input
    def enter_username_input(self, username):
        element: WebElement = self.driver.find_element(By.ID, 'username')
        return element.send_keys(username)

    ## POM for entering first name input
    def enter_firt_name_input(self, first_name):
        element: WebElement = self.driver.find_element(By.ID, 'first_name')
        return element.send_keys(first_name)

    ## POM for entering last name input
    def enter_last_name_input(self, last_name):
        element: WebElement = self.driver.find_element(By.ID, 'last_name')
        return element.send_keys(last_name)

    ## POM for entering email input
    def enter_email_input(self, email):
        element: WebElement = self.driver.find_element(By.ID, 'email')
        return element.send_keys(email)

    ## POM for entering phone number input
    def enter_phone_number_input(self, phone_number):
        element: WebElement = self.driver.find_element(By.ID, 'phone_number')
        return element.send_keys(phone_number)

    ## POM for clicking update user button
    def click_update_user_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'updateUserButton')
        return element.click()

    ## POM for clicking delete account link
    def click_delete_account_link(self):
        element: WebElement = self.driver.find_element(By.ID, 'deleteUserLink')
        return element.click()
