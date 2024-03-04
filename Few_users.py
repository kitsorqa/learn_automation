from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
#options.page_load_strategy = 'eager'
options.add_argument('--incognito')
options.add_argument('--window-size=1920,1080')
#options.add_argument("--User-agent=	Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0")
first_user = webdriver.Chrome(service=service, options=options)

LOGIN_FIELD = ("xpath", "//input[@type='email']")
PASSWORD_FIELD = ("xpath", "//input[@type='password']")
SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")


first_user.get("https://hyperskill.org/login")
first_user.find_element(*LOGIN_FIELD).send_keys("testmail_1@ya.ru")
first_user.find_element(*PASSWORD_FIELD).send_keys("Qwerty132!")
first_user.find_element(*SUBMIT_BUTTON).click()

second_user = webdriver.Chrome(service=service, options=options)
second_user.get("https://hyperskill.org/login")
second_user.find_element(*LOGIN_FIELD).send_keys("mailfortest@ya.ru")
second_user.find_element(*PASSWORD_FIELD).send_keys("yaneznaupass")
second_user.find_element(*SUBMIT_BUTTON).click()