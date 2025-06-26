from selenium.webdriver.common.by import By
from pages.Basepage import BasePage
from pages.Homepage import HomePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    username_id='user-name'
    password_id='password'
    login_btn_id='login-button'
    products_validation_xpath='//div[text()="Products"]'
    warning_one_xpath='//h3[text()="Username and password do not match any user in this service"]'
    warning_two_xpath='//h3[text()="Username is required"]'

    def enter_username(self,username):
        self.enter_text(username,"username_id",self.username_id)
        # self.driver.find_element(By.ID,self.username_id).send_keys(username)

    def enter_password(self,password):
        self.enter_text(password,"password_id",self.password_id)
        # self.driver.find_element(By.ID,self.password_id).send_keys(password)

    def click_login(self):
        self.click_element("login_btn_id",self.login_btn_id)
        # self.driver.find_element(By.ID,self.login_btn_id).click()
        return HomePage(self.driver)

    def products_validation(self):
        return self.display_status("products_validation_xpath",self.products_validation_xpath)
        # return self.driver.find_element(By.XPATH,self.products_validation_xpath).is_displayed()

    def invalid_credits_validation(self):
        return self.display_status(" warning_one_xpath",self.warning_one_xpath)
        # return self.driver.find_element(By.XPATH,self.warning_one_xpath).is_displayed()

    def empty_credits_validation(self):
        return self.display_status("warning_two_xpath",self.warning_two_xpath)
        # return self.driver.find_element(By.XPATH,self.warning_two_xpath).is_displayed()

    def enter_all_details(self,username,password):
        self.enter_username(username)
        self.enter_password(password)















