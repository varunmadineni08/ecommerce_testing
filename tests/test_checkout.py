from pages.Cartpage import CartPage
from pages.Checkoutpage import CheckoutPage
from pages.Homepage import HomePage
from pages.Loginpage import LoginPage
from tests.Basetest import BaseTest


class TestCheckout(BaseTest):

    def test_checkout(self):
        loginpage = LoginPage(self.driver)
        loginpage.enter_all_details("standard_user", "secret_sauce")
        home_page=loginpage.click_login()
        cart_page = home_page.all_items()
        checkout_page =cart_page.click_checkout()
        checkout_page.enter_all_info("varun","madineni","500000")
        assert checkout_page.payment_validation()
        checkout_page.click_finish()
        assert checkout_page.successfull_validation()

