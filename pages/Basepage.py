from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self,driver):
        self.driver=driver

    def get_element(self,locator_name,locator_value):
        element=None
        if locator_name.endswith("_id"):
            element=self.driver.find_element(By.ID,locator_value)
        elif locator_name.endswith("_xpath"):
            element=self.driver.find_element(By.XPATH,locator_value)
        elif locator_name.endswith("_class"):
            element=self.driver.find_element(By.CLASS_NAME,locator_value)
        elif locator_name.endswith("_tagname"):
            element=self.driver.find_element(By.TAG_NAME,locator_value)
        elif locator_name.endswith("_name"):
            element=self.driver.find_element(By.NAME,locator_value)
        elif locator_name.endswith("_link_text"):
            element=self.driver.find_element(By.LINK_TEXT,locator_value)
        elif locator_name.endswith("_css"):
            element=self.driver.find_element(By.CSS_SELECTOR,locator_value)
        return element

    def enter_text(self,text,locator_name,locator_value):
        element=self.get_element(locator_name,locator_value)
        element.send_keys(text)

    def click_element(self,locator_name,locator_value):
        element=self.get_element(locator_name,locator_value)
        element.click()

    def display_status(self,locator_name,locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.is_displayed()

