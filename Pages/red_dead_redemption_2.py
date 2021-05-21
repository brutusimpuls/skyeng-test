from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from config import *
import time


class redemption_games_locators:
    LOCATOR_CHOOSE_VERSION_GAME = (By.CSS_SELECTOR, '#Red\ Dead\ Redemption\ 2_button > span:nth-child(1)')
    LOCATOR_LIST_VERSION_GAME = (By.CSS_SELECTOR, '#Red\ Dead\ Redemption\ 2_menu')

class redemption_game_page(BasePage):

    def choose_redemption2(self, text):
        choose = self.find_element(redemption_games_locators.LOCATOR_CHOOSE_VERSION_GAME)
        choose.click()
        list_results = self.find_element(redemption_games_locators.LOCATOR_LIST_VERSION_GAME)
        item = list_results.find_elements_by_tag_name("li")
        for result in item:
            if str(result.text) == text_point7:
                print('\n' + 'Result: ' + str(result.text))
                result.click()
                break