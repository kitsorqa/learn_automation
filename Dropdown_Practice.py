from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import time


service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--window-size=1920,1080")
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(service=service, options=options)

#driver.get("https://the-internet.herokuapp.com/dropdown")

SELECT_LOCATOR = ("xpath", "//select[@id='dropdown']")

#How to work with classic dropdown
DROPDOWN_OBJECT = Select(driver.find_element(*SELECT_LOCATOR))

all_options = DROPDOWN_OBJECT.options

#Выбор опций из дропдауна по тексту
for option in all_options:
    time.sleep(1)
    if "Option 1" in option.text:
        print("Option is here")
    DROPDOWN_OBJECT.select_by_visible_text(option.text)

#Выбор опций из дропдауна по индексу
for index_of_option in all_options:
    time.sleep(1)
    DROPDOWN_OBJECT.select_by_index(all_options.index(index_of_option))


driver.get("https://the-internet.herokuapp.com/key_presses")

KEYBOARD_INPUT = ("xpath", "//input[@id='target']")
driver.find_element(*KEYBOARD_INPUT).send_keys("fjsdtmngfjsdowerjr")
time.sleep(1)
driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.CONTROL + "A")
time.sleep(1)
driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.BACKSPACE)
time.sleep(1)



#Работа с современными дропдаунами
DROPDOWN_SELECT = ("xpath", "//div[@id='selectOne']")
PROF_OPTION = ("xpath", "//div[contains(text(), 'Prof.')]")
driver.get("https://demoqa.com/select-menu")

time.sleep(1)

driver.find_element(*DROPDOWN_SELECT).click()
time.sleep(1)
driver.find_element(*PROF_OPTION).click()
time.sleep(2)

#multiselect
driver.get("https://demoqa.com/select-menu")
MULTI_OPTIONS = ("xpath", "//input[@id='react-select-4-input']")

driver.find_element(*MULTI_OPTIONS).send_keys("Green")
driver.find_element(*MULTI_OPTIONS).send_keys(Keys.ENTER)
time.sleep(2)