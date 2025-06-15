import time
from selenium.webdriver.common.by import By

from FirstProject.locators.locate import LoginPageLocator

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.lc = LoginPageLocator()

    def get_nav_login(self):
        return self.driver.find_element(By.ID, self.lc.nav_login_id)

    def click_nav_login(self):
        self.get_nav_login().click()

    def get_username(self):
        return self.driver.find_element(By.ID, self.lc.username_id)

    def enter_username(self, username):
        self.get_username().send_keys(username)

    def get_password(self):
        return self.driver.find_element(By.ID, self.lc.pwd_id)

    def enter_password(self, password):
        self.get_password().send_keys(password)

    def get_login_button(self):
        return self.driver.find_element(By.XPATH, self.lc.button_xpath)

    def click_login_button(self):
        self.get_login_button().click()

    def login(self, username, password):
        self.click_nav_login()
        time.sleep(1)  # Give time for modal to load
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        time.sleep(3)  # Wait for login response
