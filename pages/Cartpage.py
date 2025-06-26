from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.Basepage import BasePage
from pages.Checkoutpage import CheckoutPage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    checkout_btn_xpath='//a[@class="btn_action checkout_button"]'
    checkout_validation_xpath='//div[text()="Checkout: Your Information"]'


    def click_checkout(self):
        self.driver.find_element(By.XPATH,self.checkout_btn_xpath).click()
        return CheckoutPage(self.driver)

    def checkout_validation(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.checkout_validation_xpath))).is_displayed()
        # self.driver.find_element(By.CLASS_NAME,self.checkout_validation_class).is_displayed()