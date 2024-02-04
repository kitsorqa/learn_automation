from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(service=service, options=options)


driver.get("https://parsinger.ru/selenium/5.5/4/1.html")
all_divs = driver.find_elements("xpath", "//div[@class='parent']")
for i in range(1, len(all_divs) + 1):
     info = driver.find_element("xpath", f"(//textarea[@color='gray'])[{i}]")
     nums = info.text
     info.clear()
     driver.find_element("xpath", f"(//textarea[@color='blue'])[{i}]").send_keys(nums)
     driver.find_element("xpath", f"(//button)[{i}]").click()
driver.find_element("xpath", "//button[@id='checkAll']").click()
final = driver.find_element("xpath", "//p[@id='congrats']")
final = final.text
print(final)