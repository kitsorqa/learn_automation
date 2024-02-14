from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(service=service, options=options)


driver.get("https://demoqa.com/selectable")

CHECKBOX_ACTION = ("xpath", "//li[text()='Cras justo odio']")
before = driver.find_element(*CHECKBOX_ACTION).get_attribute("class")
driver.find_element(*CHECKBOX_ACTION).click()
after_click = driver.find_element(*CHECKBOX_ACTION).get_attribute("class")
print("OK" if "active" in after_click else "TEST IS DOWN") 