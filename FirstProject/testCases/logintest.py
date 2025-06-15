import unittest
from selenium import webdriver
# import pages.LoginPage

from FirstProject.pages.LoginPage import Login
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com")
        self.login_page = Login(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_valid(self):
        self.login_page.login("testmorning", "test123")
        self.assertTrue(self.driver.find_element(By.ID, "logout2").is_displayed())

    def test_login_invalid(self):
        self.login_page.login("testmorning", "wrongpassword")
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "Wrong password.")
        alert.accept()

