from selenium.webdriver.common.by import By

class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

    add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    title = (By.CLASS_NAME, "title")

    def add_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart_btn).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def get_page_title(self):
        return self.driver.find_element(*self.title).text
