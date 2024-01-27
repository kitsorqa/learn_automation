import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
username = driver.find_element("xpath", "//input[@id='user-name']")
password = driver.find_element("xpath", "//input[@id='password']")
login_button = driver.find_element("xpath", "//input[contains(@class, 'submit-button')]")
username.click()
username.send_keys("valera@inbox.ru")
print(username.get_attribute("autocapitalize"))
print(username.get_attribute("type"))
"""username.clear()
print(username.get_attribute("value"))"""
"""password.click()
password.send_keys("kek222001")
login_button.click()"""
