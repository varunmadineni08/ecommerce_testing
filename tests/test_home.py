import time

from pages.Homepage import HomePage
from pages.Loginpage import LoginPage
from tests.Basetest import BaseTest


class TestHome(BaseTest):

    def test_home(self):
        loginpage=LoginPage(self.driver)
        loginpage.enter_all_details("standard_user","secret_sauce")
        home_page=loginpage.click_login()
        home_page.all_items()
        assert home_page.cart_validation()