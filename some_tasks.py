from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=0.5)

#task 1
#Refresh the page until the text switches to a certain number.
driver.get("https://parsinger.ru/methods/1/index.html")
TEXT_PAGE = ("xpath", "//p[@id='result']")
num = ''

while True:
    if driver.find_element(*TEXT_PAGE).text == "refresh page":
        driver.refresh()
    else:
        print(driver.find_element(*TEXT_PAGE).text)
        break


#task 2
#Choose every field and clean it, then copy the number from the alert
driver.get("https://parsinger.ru/selenium/5.5/1/1.html")
all_elements = driver.find_elements("xpath", "//input[@class='text-field']")
for elem in all_elements:
    elem.click()
    elem.clear()
driver.find_element("xpath", "//button[@id='checkButton']").click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)

#task 3
#Get sum of cookies which name has an even number
driver.get("https://parsinger.ru/methods/3/index.html")
cookies = driver.get_cookies()
my_lst = [cookies]
num = []
for i in my_lst:
    for j in i:
        if '_' in str(j['name']):
            fnd = j['name'].rfind('_')
            if j['name'][fnd + 1:].isdigit():
                if int(j['name'][fnd + 1:]) % 2 == 0:
                    num.append(j['value'])

num = [int(i) for i in num]
print(sum(num))


#task 4
#Minefield
driver.get("https://parsinger.ru/selenium/5.5/2/1.html")
elements = driver.find_elements("xpath", "//input[@data-enabled='true']")
for elem in elements:
    elem.click()
    elem.clear()
driver.find_element("xpath", "//button[@id='checkButton']").click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)

#task 5
#Get the number from the page where the cookie lifetime is the longest
cookies_len, count = 0, 0
driver.get("https://parsinger.ru/methods/5/index.html")
urls = driver.find_elements("xpath", "//div[@class='urls']")

for i in range(1, len(urls) + 1):
    driver.get(f"https://parsinger.ru/methods/5/{i}.html")
    my_cock = driver.get_cookies()
    for k in my_cock:
        if cookies_len < (int(k['expiry'])):
            cookies_len = (int(k['expiry']))
            count = i

driver.get(f"https://parsinger.ru/methods/5/{count}.html")
num = driver.find_element("xpath", "//p[@id='result']")
print(num.text)

#task 6
#Scroll the page until the number becomes available
result = []
driver.get("https://parsinger.ru/scroll/4/index.html")
elements = driver.find_elements("xpath", "//button[@class='btn']")
for elem in elements:
    driver.execute_script("return arguments[0].scrollIntoView(true);", elem)
    elem.click()
    some_info = driver.find_element("xpath", "//p[@id='result']").text
    result.append(some_info)

result = [int(i) for i in result]
print(sum(result))