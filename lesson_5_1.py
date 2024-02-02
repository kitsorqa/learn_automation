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
CHANGE_TEXT_BUTTON = ("xpath", "//button[@id='populate-text']")
VISIBLE_TEXT = ("xpath", "//h2[@class='target-text' and text()='Selenium Webdriver']")

driver.find_element(*CHANGE_TEXT_BUTTON).click()
wait.until(EC.visibility_of_element_located(VISIBLE_TEXT))
print("BCE OKEY")







