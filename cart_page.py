from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, driver):
        self.driver = driver

    cart_item = (By.CLASS_NAME, "inventory_item_name")

    def get_cart_item_name(self):
        return self.driver.find_element(*self.cart_item).text
