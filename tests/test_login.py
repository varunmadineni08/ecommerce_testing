from pages.Loginpage import LoginPage
import pytest

from tests.Basetest import BaseTest



class TestLogin(BaseTest):

    def test_with_valid_credits(self):
        loginpage=LoginPage(self.driver)
        loginpage.enter_username("standard_user")
        loginpage.enter_password("secret_sauce")
        loginpage.click_login()
        assert loginpage.products_validation()

    def test_with_invalid_credits(self):
        loginpage=LoginPage(self.driver)
        loginpage.enter_username("varun")
        loginpage.enter_password("password")
        loginpage.click_login()
        assert loginpage.invalid_credits_validation()

    def test_with_empty_credits(self):
        loginpage=LoginPage(self.driver)
        loginpage.enter_username("")
        loginpage.enter_password("")
        loginpage.click_login()
        assert loginpage.empty_credits_validation()
