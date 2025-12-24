from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_add_product_to_cart(setup):
    driver = setup

    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    products = ProductsPage(driver)
    products.add_product_to_cart()
    products.go_to_cart()

    cart = CartPage(driver)
    assert cart.get_cart_item_name() == "Sauce Labs Backpack"
