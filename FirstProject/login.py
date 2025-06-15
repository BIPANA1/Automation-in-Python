import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com/index.html")

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        nav_login = wait.until(EC.element_to_be_clickable((By.ID, "login2")))
        nav_login.click()

        username_field = wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))
        username_field.send_keys("testmorning")

        password_field = driver.find_element(By.ID, "loginpassword")
        password_field.send_keys("test123")

        button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")))
        button.click()

        time.sleep(2)

        expected_result = "welcome test automation"
        actual_result = driver.find_element(By.ID, "something").text
        self.assertEqual(expected_result, actual_result, "User is not logged in")

if __name__ == '__main__':
    unittest.main()













# import time
# import unittest
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
# from firstSelenium import username
#
#
# class MyTestCase(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get("https://demoblaze.com/index.html")
#
#
#
#     def tearDown(self):
#         self.driver.quit()
#
#    def test_login(self):
#        driver = self.driver
#        wait = WebDriverWait(driver, 10)
#        nav_login = wait.until(EC.element_to_be_clickable((By.ID, "login2")))
#        nav_login.click()
#
#        username = wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))
#        username.send_keys("testmorning")
#
#        password = driver.find_element(By.ID, "loginpassword")
#        password.send_keys("test123")
#
#       button = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]")))
#        self.click();
#
#        time.sleep(2)
#        expected_result = "welcome test automation"
#        actual_result = driver.find_element(By.ID,"something")
#        self.assertEqual(expected_result, actual_result, "User is not logged in")
# if __name__ == '__main__':
#     unittest.main()
