import glob
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": f"{os.getcwd()}\\download_files\\"}
options.page_load_strategy = 'eager'
options.add_argument("--incognito")
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.lambdatest.com/selenium-playground/download-file-demo")
download_button = driver.find_element("xpath", "//button[@type='button']")
download_button.click()
time.sleep(1)

first_check = "Файл имеется" if os.listdir(f"{os.getcwd()}\\download_files\\") else "Файл отсутствует"
assert first_check == "Файл имеется"

downloaded_files = glob.glob(os.path.join("*.pdf"))

for file in downloaded_files:
    size_of_file = os.path.getsize(file)
    assert size_of_file > 10, 'Файл пустой'
    os.remove(file)

