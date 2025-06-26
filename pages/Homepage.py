from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.Basepage import BasePage
from pages.Cartpage import CartPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    add_one_item_xpath='(//button)[text()="ADD TO CART"][1]'
    add_two_item_xpath='(//button)[text()="ADD TO CART"][2]'
    shopping_cart_xpath='//div[@id="shopping_cart_container"]//descendant::a'
    cart_validation_xpath='//div[text()="Your Cart"]'

    def add_one_item(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.add_one_item_xpath))).click()
        # self.driver.find_element(By.XPATH,self.add_one_item_xpath).click()
    def add_two_item(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.add_two_item_xpath))).click()
        # self.driver.find_element(By.XPATH,self.add_two_item_xpath).click()

    def cart(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.shopping_cart_xpath))).click()
       #self.driver.find_element(By.ID,self.shopping_cart_id).click()
        return CartPage(self.driver)

    def cart_validation(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.cart_validation_xpath))).is_displayed()
        # self.driver.find_element(By.XPATH,self.cart_validation_xpath).is_displayed()

    def all_items(self):
        self.add_one_item()
        self.add_two_item()
        self.cart()
        return CartPage(self.driver)
