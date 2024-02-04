from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(service=service, options=options)


my_lst = []
driver.get("https://parsinger.ru/selenium/5.5/3/1.html")
checkbox = driver.find_elements("xpath", "//div[@class='parent']")
for i in range(1, len(checkbox) + 1):
    if driver.find_element("xpath", f"(//input[@type='checkbox'])[{i}]").is_selected():
        num = driver.find_element("xpath", f"(//textarea)[{i}]").text
        my_lst.append(num)

print(sum([int(i) for i in my_lst]))