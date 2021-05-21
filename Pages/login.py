from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class login_locators:
    LOCATOR_APPLE_ID = (By.ID, 'login-with-apple')
    LOCATOR_CHECK_APPLE = (By.CSS_SELECTOR, '.si-container-title')

class login(BasePage):

    def apple_id(self):
        apple_id = self.find_element((login_locators.LOCATOR_APPLE_ID))
        apple_id.click()

    def check_apple(self):
        try:
            apple_text = self.find_element(login_locators.LOCATOR_CHECK_APPLE)
        except NoSuchElementException:
            return False
        return True