import os

import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

options = webdriver.ChromeOptions()

options.page_load_strategy = "eager"

# Задание 1

prefs = {
    "download.default_directory": f"{os.getcwd()}",
    "safebrowsing.enabled": False
}

options.add_experimental_option("prefs", prefs)

driver.get("https://demoqa.com/upload-download")
upload_file = driver.find_element("xpath", "//input[@id='uploadFile']")
upload_file.send_keys(f"{os.getcwd()}/PhotoWorld.jpg")

# Задание 2

options = webdriver.ChromeOptions()

prefs = {
    "download.default_directory": f"{os.getcwd()}" + "\downloads",
    "safebrowsing.enabled": True
}
options.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://the-internet.herokuapp.com/download")
elements = driver.find_elements("xpath", "//a[contains(@href, 'download')]")
for elem in elements:
    elem.click()