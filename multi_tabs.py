from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument('--incognito')
options.add_argument('--window-size=1920,1080')
options.add_argument("--User-agent=	Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0")
driver = webdriver.Chrome(service=service, options=options)



driver.get("https://hyperskill.org/tracks")
first_title = driver.title
driver.switch_to.new_window("window")
driver.get("https://www.avito.ru/")
third_title = driver.title
driver.switch_to.new_window("window")
driver.get("https://tanki.su/ru/content/guide/")
second_title = driver.title
tabs = driver.window_handles

first_locator = ("xpath", "//button[contains(text(), ' Start for free ')]")
second_locator = ("xpath", "//span[contains(text(), 'Разместить объявление')]")
third_locator = ("xpath", "(//span[@class='newcomers-menu_text'])[1]")

driver.switch_to.window(tabs[0])
driver.find_element(*first_locator)
time.sleep(3)
driver.switch_to.window(tabs[1])
driver.find_element(*second_locator)
time.sleep(3)
driver.switch_to.window(tabs[2])
time.sleep(2)
driver.find_element(*third_locator)
time.sleep(3)