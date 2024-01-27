import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

full_name = driver.find_element("xpath", "//input[contains(@class, 'mr-sm-2') and (@id='userName')]")
full_name.clear()
full_name.send_keys("Valera Goblin")

Email = driver.find_element("xpath", "//input[contains(@class, 'mr-sm-2') and (@id='userEmail')]")
Email.clear()
Email.send_keys("valera@zzz.net")

Current_Address = driver.find_element("xpath", "//textarea[(@class='form-control') and (@id='currentAddress')]")
Current_Address.clear()
Current_Address.send_keys("Serbia, Belgrad, St. Vuchich 22")

Permanent_Address = driver.find_element("xpath", "//textarea[@id='permanentAddress']")
Permanent_Address.clear()
Permanent_Address.send_keys("USA, Washington, third basement")

Submit_button = driver.find_element("xpath", "//button[@id='submit']")
Submit_button.click()

time.sleep(2)