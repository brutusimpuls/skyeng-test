from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class adults_page_locators:
    LOCATOR_ADULTS_PAGE_BUTTON = (By.CSS_SELECTOR, '.css-vjttra-CallToActionText__callToActionText')

class adults_agree(BasePage):

    def adults_page(self):
        continue_button = self.find_element(adults_page_locators.LOCATOR_ADULTS_PAGE_BUTTON)
        continue_button.click()
        print("Соглашаемся, что уже есть 18")