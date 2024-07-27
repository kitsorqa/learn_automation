from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Login_page():
    def __init__(self, driver):
        self.driver = driver

    def get_usernames(self):
        credentials = self.driver.find_elements("xpath", "//div[@id='login_credentials']")
        credentials = credentials[0].text.split('\n')
        credentials.remove("Accepted usernames are:")
        return credentials

    def authorization(self, user_name, user_password):
        print(f"Начинается проверка для юзера {user_name}")
        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((
            "xpath", "//input[@id='user-name']"))).send_keys(user_name)
        print("Input login")

        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((
            "xpath", "//input[@id='password']"))).send_keys(user_password)
        print("Input Password")

        button_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", "//input[@id='login-button']")))
        button_login.click()

        products_text = self.driver.find_element("xpath", "//span[@class='title']").text
        print("Succes Authorization")
        assert products_text == 'Products'
        print("Вы на странице выбора товаров")

        burger_menu = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", "//button[@id='react-burger-menu-btn']")))
        burger_menu.click()
        print("Бургер меню открыто")

        logout = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", "//a[@id='logout_sidebar_link']")))
        logout.click()
        print("Вы разлогинились\n")


class Test():
    def test_select_product(self):
        options = webdriver.ChromeOptions()
        service = Service(executable_path=ChromeDriverManager().install())
        base_url = 'https://www.saucedemo.com/'
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--incognito')
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(base_url)

        login = Login_page(driver)
        list_of_names = login.get_usernames()
        for user in list_of_names:
            try:
                login.authorization(user, user_password='secret_sauce')
            except NoSuchElementException as e:
                print("Для данного юзера авторизация невозможна\n")
                driver.refresh()
        print("Поздравляю, тест успешно пройден")


Test_1 = Test()
Test_1.test_select_product()