from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_valid_login(setup):
    driver = setup
    login = LoginPage(driver)

    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    products = ProductsPage(driver)
    assert products.get_page_title() == "Products"


def test_invalid_login(setup):
    driver = setup
    login = LoginPage(driver)

    login.enter_username("wrong_user")
    login.enter_password("wrong_pass")
    login.click_login()

    assert "Epic sadface" in login.get_error_message()
