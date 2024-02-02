from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
ENABLE_BUTTON_AFTER = ("xpath", "//button[@id='enable-button']")
BUTTON_ENABLE_NOW = ("xpath", "//button[@id='disable' and text()='Button']")


driver.find_element(*ENABLE_BUTTON_AFTER).click()
wait.until(EC.element_to_be_clickable(BUTTON_ENABLE_NOW)).click()
print("Test successful")








