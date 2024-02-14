from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--window-size=1920,1080")
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(service=service, options=options)


driver.get("https://demoqa.com/radio-button")

STATUS_YES_RADIO = ("xpath", "//input[@id='yesRadio']")
BUTTON_YES_RADIO = ("xpath", "//label[@for='yesRadio']")
no_radio = ("xpath", "//input[@id='noRadio']")
BUTTON_NO_RADIO = ("xpath", "//label[@for='noRadio']")

print(driver.find_element(*STATUS_YES_RADIO).is_selected())
driver.find_element(*BUTTON_YES_RADIO).click()
print(driver.find_element(*STATUS_YES_RADIO).is_selected())

print(driver.find_element(*no_radio).is_enabled())