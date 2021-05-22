from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

class cookieslocators:
    LOCATOR_COOKIES_POLICY_TEXT = (By.CSS_SELECTOR, '#onetrust-policy-text > a')
    LOCATOR_COOKIES_SETTINGS = (By.CSS_SELECTOR, '#onetrust-pc-btn-handler')
    LOCATOR_COOKIES_AGREE_BUTTON = (By.CSS_SELECTOR, '#onetrust-accept-btn-handler')

class cookies_block(BasePage):
    def agree_button(self):
        try:
            click_button_agree = self.find_element(cookieslocators.LOCATOR_COOKIES_AGREE_BUTTON)
            click_button_agree.click()
        except TimeoutException:
            print('Нет попапа соглашения по кукам')