import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Edge WebDriver
driver = webdriver.Edge()
driver.maximize_window()
driver.get("http://demoblaze.com")

driver.find_element(By.ID, "login2").click()

wait = WebDriverWait(driver, 10)
username = wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))
username.send_keys("testmorning")

password = driver.find_element(By.ID, "loginpassword")
password.send_keys("test123")

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']")))
login_button.click()

time.sleep(5)

driver.quit()
