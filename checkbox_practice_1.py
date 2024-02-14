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


driver.get("https://the-internet.herokuapp.com/checkboxes")

CHECKBOX_1 = ('xpath', "(//input[@type='checkbox'])[1]")

driver.find_element(*CHECKBOX_1).click()

assert driver.find_element(*CHECKBOX_1).get_attribute("checked") == 'true'
assert driver.find_element(*CHECKBOX_1).is_selected() == True