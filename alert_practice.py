from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.page_load_strategy = "eager"
#options.add_argument("--ignore-certificate-errors")
#options.add_argument(
    #"user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.136 Yowser/2.5 Safari/537.36")
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://demoqa.com/alerts")
BUTTON_1 = ("xpath", "//button[@id='alertButton']")
BUTTON_2 = ("xpath", "//button[@id='confirmButton']")
BUTTON_3 = ("xpath", "//button[@id='promtButton']")

#Click at alert
wait.until(EC.element_to_be_clickable(BUTTON_1)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
alert.accept()


#Press cancel at alert message
wait.until(EC.element_to_be_clickable(BUTTON_2)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
alert.dismiss()


#Send some words at alert box
wait.until(EC.element_to_be_clickable(BUTTON_3)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
time.sleep(3)
alert.send_keys("Hey there")
time.sleep(1)
alert.accept()
time.sleep(1)
