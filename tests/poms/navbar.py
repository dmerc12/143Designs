from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POMs for navbar
class NavBar():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for clicking navbar dropdown toggle
    def click_navbar_dropdown_toggle(self):
        element: WebElement = self.driver.find_element(By.ID, 'navbarDropdown')
        return element.click()

    ## POM for clicking update account
    def click_update_account(self):
        element: WebElement = self.driver.find_element(By.ID, 'navUpdateUserButton')
        return element.click()

    ## POM for clicking change password
    def click_change_password(self):
        element: WebElement = self.driver.find_element(By.ID, 'navChangePasswordButton')
        return element.click()

    ## POM for clicking logout
    def click_logout(self):
        element: WebElement = self.driver.find_element(By.ID, 'navLogoutButton')
        return element.click()

    ## POM for clicking register
    def click_register(self):
        element: WebElement = self.driver.find_element(By.ID, 'navRegisterButton')
        return element.click()

    ## POM for clicking login
    def click_login(self):
        element: WebElement = self.driver.find_element(By.ID, 'navLoginButton')
        return element.click()

    ## POM for entering search bar input
    def enter_search_input(self, criteria):
        element: WebElement = self.driver.find_element(By.ID, 'navbarSearch')
        return element.send_keys(criteria)

    ## POM for clicking search button
    def click_search_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'btnNavbarSearch')
        return element.click()

    ## POM for clicking side navbar toggle
    def click_side_navbar_toggle(self):
        element: WebElement = self.driver.find_element(By.ID, 'sidebarToggle')
        return element.click()

    ## POM for clicking contact button
    def click_contact_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'navContactButton')
        return element.click()
