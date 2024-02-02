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
DISPLAY_BUTTON = ("xpath", "//button[@id='display-other-button']")
DISPLAY_ENABLE_BUTTON = ("xpath", "//button[@id='hidden' and contains(text(), 'Enabled')]")

driver.find_element(*DISPLAY_BUTTON).click()
wait.until(EC.visibility_of_element_located(DISPLAY_ENABLE_BUTTON)).click()
wait.until(EC.invisibility_of_element_located(DISPLAY_ENABLE_BUTTON))
print("BCE OKEY")







