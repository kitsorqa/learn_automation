from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.page_load_strategy = 'eager'
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://demoqa.com/selectable")
OPEN_GRID = ("xpath", "//a[@id='demo-tab-grid']")
driver.find_element(*OPEN_GRID).click()


ONE_TAB = ("xpath", "(//li[contains(@class, 'list-group-item')])[5]")
FIVE_TAB = ("xpath", "(//li[contains(@class, 'list-group-item')])[9]")
NINE_TAB = ("xpath", "(//li[contains(@class, 'list-group-item')])[13]")


#Test for first button
assert driver.find_element(*ONE_TAB).is_selected() is False
driver.find_element(*ONE_TAB).click()
assert "active" in driver.find_element(*ONE_TAB).get_attribute("class")
driver.find_element(*ONE_TAB).click()
assert driver.find_element(*ONE_TAB).is_selected() is False


#Test for second button
assert driver.find_element(*FIVE_TAB).is_selected() is False
driver.find_element(*FIVE_TAB).click()
assert "active" in driver.find_element(*FIVE_TAB).get_attribute("class")
driver.find_element(*FIVE_TAB).click()
assert driver.find_element(*FIVE_TAB).is_selected() is False

#Test for third button
assert driver.find_element(*NINE_TAB).is_selected() is False
driver.find_element(*NINE_TAB).click()
assert "active" in driver.find_element(*NINE_TAB).get_attribute("class")
driver.find_element(*NINE_TAB).click()
assert driver.find_element(*NINE_TAB).is_selected() is False