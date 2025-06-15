import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


# driver = webdriver.Edge()
#
# driver.maximize_window()
#
# driver.get("https://demo.automationtesting.in/Alerts.html")
# simple_nav = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a')
# simple_nav.click()
#
# button1 = driver.find_element(By.XPATH,'//*[@id="OKTab"]/button')
# button1.click()
# time.sleep(5)
#
# driver.switch_to.alert.accept()
# time.sleep(5)
#
# driver = webdriver.Edge()
#
# driver.maximize_window()
#
# driver.get("https://demo.automationtesting.in/Alerts.html")
# simple_nav = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a')
# simple_nav.click()
#
# button1 = driver.find_element(By.XPATH,'/*[@id="Textbox"]/button')
# button1.click()
# time.sleep(5)
#
# driver.switch_to.alert.dismiss()
# time.sleep(5)


from datetime import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Alerts.html")
# simple_nav = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a')
# simple_nav.click()
# button1 = driver.find_element(By.XPATH, '//*[@id="OKTab"]/button')
# button1.click()
# time.sleep(5)
# Alert = driver.switch_to.alert
# Alert.accept()
# time.sleep(5)

## alert with ok and cancel
##ok
simple_nav = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a')
simple_nav.click()
button1 = driver.find_element(By.XPATH, '//*[@id="CancelTab"]/button')
button1.click()
time.sleep(5)
Alert.accept()
time.sleep(5)
##cancel
simple_nav = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a')
simple_nav.click()
button1 = driver.find_element(By.XPATH, '//*[@id="CancelTab"]/button')
button1.click()
time.sleep(5)
Alert.dismiss()
time.sleep(5)

## Alert with text


simple_nav = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a')
simple_nav.click()
button1 = driver.find_element(By.XPATH, '//*[@id="Textbox"]/button')
button1.click()
time.sleep(5)
Alert.send_keys('Bipana Shrestha')
Alert.accept()

time.sleep(5)



