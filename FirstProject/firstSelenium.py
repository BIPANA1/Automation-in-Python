import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get("http://demoblaze.com")
time.sleep(3)

driver.find_element(By.ID,"login2").click()
time.sleep(3)

username= driver.find_element(By.ID,"loginusername")
username.send_keys("testmorning")
driver.click()
password= driver.find_element(By.ID,"loginpassword")
password.send_keys("test123")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]")
driver.click()

time.sleep(5)
driver.click()