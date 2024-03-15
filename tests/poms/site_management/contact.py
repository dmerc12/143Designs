from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POMs for contact page
class ContactPage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for entering first name input
    def enter_first_name_input(self, first_name):
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

    ## POM for entering title input
    def enter_title_input(self, title):
        element: WebElement = self.driver.find_element(By.ID, 'title')
        return element.send_keys(title)

    ## POM for entering message input
    def enter_message_input(self, message):
        element: WebElement = self.driver.find_element(By.ID, 'message')
        return element.send_keys(message)

    ## POM for clicking submit button
    def click_submit_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'submitMessageButton')
        return element.click()
