from pages.Cartpage import CartPage
from pages.Homepage import HomePage
from pages.Loginpage import LoginPage
from tests.Basetest import BaseTest


class TestCart(BaseTest):

    def test_cart(self):
        loginpage = LoginPage(self.driver)
        loginpage.enter_all_details("standard_user", "secret_sauce")
        home_page=loginpage.click_login()
        cart_page=home_page.all_items()
        cart_page.click_checkout()
        assert cart_page.checkout_validation()