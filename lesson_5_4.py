from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
CHECK_CHECKBOX_BUTTON = ("xpath", "//button[@id='alert']")

driver.find_element(*CHECK_CHECKBOX_BUTTON).click()
wait.until(EC.alert_is_present())
print("Test successful")