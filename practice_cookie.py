import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
#options.add_argument("--incognito")
options.add_argument("--window-size=1920,1080")
options.page_load_strategy = 'eager'
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

"""Replace some cookie
driver.get("https://www.freeconferencecall.com/en/us/login")
before = driver.get_cookie("split")
print(before)
driver.delete_cookie("split")
driver.add_cookie({
    "name": "split",
    "value": "QWERTY"
})

after = driver.get_cookie("split")
print(after)
"""

"""Download cookies
driver.get("https://www.freeconferencecall.com/en/us/login")
pickle.dump(driver.get_cookies(), open(os.getcwd()+"/cookies.pkl", "wb"))
"""

"""Load cookies from the file
my_cookies = pickle.load(open(os.getcwd()+"/cookies.pkl", "rb"))
driver.delete_all_cookies()

for cookie in my_cookies:
    driver.add_cookie(cookie)

time.sleep(3)
driver.refresh()
"""

"""
task_1, Install and read cookies
my_cookie = {
    "name": "username",
    "value": "user123"
}
driver.get("https://www.labirint.ru/")
driver.add_cookie(my_cookie)
my_cookie = driver.get_cookie("username")
print(my_cookie)
"""

#task_2, Delete any cookies
"""
driver.get("https://www.chitai-gorod.ru/")
print(driver.get_cookie("refresh-token"))
driver.delete_cookie("refresh-token")
driver.refresh()
print(driver.get_cookie("refresh-token"))
"""

#task_3, Add something to cart, save cookies, delete cookies, insert them, refresh page
driver.get("https://www.petshop.ru/catalog/cats/sukhoy-korm-acti-protect-dlya-sterilizovannykh-koshek-s-indeykoy/")

#driver.execute_script("scrollTo(0, 1000)")
time.sleep(2)
driver.find_element("xpath", "(//span[@class='style_button__text__GdrEf'])[1]").click()
time.sleep(2)
APPEAR_TEXT = ("xpath", "//div[@class='notifier_ToastDescription__WO0zi']")
time.sleep(2)
wait.until(EC.invisibility_of_element_located(APPEAR_TEXT))
driver.find_element("xpath", "(//a[contains(@class, 'Link_link__-8H7G')])[3]").click()
cookies = driver.get_cookies()
driver.delete_all_cookies()
#driver.execute_script("scrollTo(0, 0)")
#pickle.dump(driver.get_cookies(), open(os.getcwd()+"/some_cookies.pkl", "wb"))
# = pickle.load(open(os.getcwd()+"/some_cookies.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(5)
driver.refresh()
time.sleep(2)