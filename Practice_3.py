from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(service=service, options=options)


driver.get("https://parsinger.ru/methods/3/index.html")
my_cookies = driver.get_cookies()
nums = []
for i in range(len(my_cookies)):
    if 'secret_cookie_' in my_cookies[i]['name']:
        nums.append(int(my_cookies[i]['value']))

print(sum(nums))