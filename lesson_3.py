import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://the-internet.herokuapp.com/status_codes")
status_200 = driver.find_element("xpath", "//a[contains(@href, '200')]")
status_200.click()
time.sleep(1)
driver.back()

status_301 = driver.find_element("xpath", "//a[contains(@href, '301')]")
status_301.click()
time.sleep(1)
driver.back()

status_404 = driver.find_element("xpath", "//a[contains(@href, '404')]")
status_404.click()
time.sleep(1)
driver.back()

status_500 = driver.find_element("xpath", "//a[contains(@href, '500')]")
status_500.click()
time.sleep(1)
driver.back()