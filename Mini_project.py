from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument("--incognito")
options.add_argument("--window-size=1920,1080")
faker = Faker()

class CheckSiteItems:

    @staticmethod
    def authorization():
        driver.get("https://www.saucedemo.com/")
        driver.find_element("xpath", "//input[@id='user-name']").send_keys('standard_user')
        driver.find_element("xpath", "//input[@id='password']").send_keys('secret_sauce')
        driver.find_element("xpath", "//input[@id='login-button']").click()

    @staticmethod
    def CountIconBasket():
        assert int(driver.find_element("xpath", "//span[@class='shopping_cart_badge']").text) == 1

    @staticmethod
    def BasketIconButton():
        driver.find_element("xpath", "//a[@class='shopping_cart_link']").click()

    @staticmethod
    def CheckoutButton():
        driver.find_element("xpath", "//button[@id='checkout']").click()

    @staticmethod
    def InformationForOrder():
        name = faker.first_name() + str(faker.random_int())
        second_name = faker.last_name() + str(faker.random_int())
        postal_code = faker.postalcode()
        driver.find_element("xpath", "//input[@id='first-name']").send_keys(name)
        driver.find_element("xpath", "//input[@id='last-name']").send_keys(second_name)
        driver.find_element("xpath", "//input[@id='postal-code']").send_keys(postal_code)
        driver.find_element("xpath", "//input[@id='continue']").click()

    @staticmethod
    def PriceCheckCheckout():
        final_price = driver.find_element("xpath", "(//div[@class='summary_subtotal_label'])")
        final_price = final_price.text
        final_price = final_price[final_price.find('$'):]
        return final_price

    @staticmethod
    def FinishButton():
        driver.find_element("xpath", "//button[@id='finish']").click()

    @staticmethod
    def TextAfterOrder():
        assert driver.find_element("xpath", "//h2[@class='complete-header']").text == "Thank you for your order!"
        driver.find_element("xpath", "//button[@id='back-to-products']").click()

    @staticmethod
    def TitleCheck():
        assert driver.title == 'Swag Labs'



class ListOfProducts:
    def __init__(self, option):
        CheckSiteItems.authorization()
        self.option = option
        self.item_price_store = driver.find_element("xpath", f"(//div[@class='inventory_item_price'])[{self.option}]")
        self.item_name_store = driver.find_element("xpath", f"(//div[@class='inventory_item_name '])[{self.option}]")
        self.add_to_cart = driver.find_element("xpath",f"(//button[contains(@class, 'btn')])[{self.option}]")

    def start_test(self):
        print(f"Проверяем товар {self.item_name_store.text}")
        self.add_to_cart.click()
        text_item_name_store = self.item_name_store.text
        text_item_price_store = self.item_price_store.text
        CheckSiteItems.CountIconBasket()
        CheckSiteItems.BasketIconButton()
        assert text_item_name_store == driver.find_element("xpath", "//div[@class='inventory_item_name']").text
        assert text_item_price_store == driver.find_element("xpath", "//div[@class='inventory_item_price']").text
        CheckSiteItems.CheckoutButton()
        CheckSiteItems.InformationForOrder()
        CheckSiteItems.CountIconBasket()
        assert CheckSiteItems.PriceCheckCheckout() == text_item_price_store
        CheckSiteItems.FinishButton()
        CheckSiteItems.TextAfterOrder()
        CheckSiteItems.TitleCheck()
        print(f"Оформление товара {text_item_name_store} успешно завершено")


print("Приветствую вас в нашем интернет-магазине")
product = int(input("""
В данный момент магазин насчитывает 6 позиций, выберите товар, который хотите приобрести:
1. Sauce Labs Backpack
2. Sauce Labs Bike Light
3. Sauce Labs Bolt T-Shirt
4. Sauce Labs Fleece Jacket
5. Sauce Labs Onesie
6. Test.allTheThings() T-Shirt (Red)
"""))


driver = webdriver.Chrome(service=service, options=options)
start_my_test = ListOfProducts(product)
start_my_test.start_test()