from selenium.webdriver.common.by import By

from pages.Basepage import BasePage


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    firstname_id='first-name'
    lastname_id='last-name'
    zipcode_id='postal-code'
    continue_btn_xpath='//input[@value="CONTINUE"]'
    payment_validation_xpath='//div[text()="Payment Information:"]'
    finish_btn_xpath='//a[text()="FINISH"]'
    successfull_validation_xpath='//div[contains(text(),"Your order has been dispatched")]'

    def enter_firstname(self,firstname):
        self.driver.find_element(By.ID,self.firstname_id).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.ID, self.lastname_id).send_keys(lastname)
    def enter_zipcode(self,zipcode):
        self.driver.find_element(By.ID,self.zipcode_id).send_keys(zipcode)

    def click_continue(self):
        self.driver.find_element(By.XPATH,self.continue_btn_xpath).click()

    def payment_validation(self):
        return self.driver.find_element(By.XPATH,self.payment_validation_xpath).is_displayed()

    def click_finish(self):
        self.driver.find_element(By.XPATH,self.finish_btn_xpath).click()

    def successfull_validation(self):
        return self.driver.find_element(By.XPATH,self.successfull_validation_xpath).is_displayed()

    def enter_all_info(self,firstname,lastname,zipcode):
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_zipcode(zipcode)
        self.click_continue()


