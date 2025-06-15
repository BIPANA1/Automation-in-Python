import time
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get("http://demoblaze.com")

driver.find_element(By.ID, "login2").click()

try:
    simple_nav = driver.find_element(By.ID, "loginusername")
    simple_nav.send_keys("testmorning")

    password = driver.find_element(By.ID, "loginpassword")
    password.send_keys("test123")

    login_button = driver.find_element(By.XPATH, "//button[text()='Log in']")
    login_button.click()

except ElementNotInteractableException:
    print("Element is not interactable")

time.sleep(5)
driver.quit()
