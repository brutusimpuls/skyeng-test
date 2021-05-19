from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from config import *
import time

class epic_games_locators:
    LOCATOR_SEARCH_FIELD = (By.ID, 'searchInput')
    LOCATOR_CLEAR_FIELD_SEARCH = (By.CLASS_NAME, 'css-682sma')
    LOCATOR_SEARCH_RESULT = (By.ID, 'search-bar-autocomplete')
    LOCATOR_ADULTS_PAGE_BUTTON = (By.CSS_SELECTOR, '.css-vjttra-CallToActionText__callToActionText')
    LOCATOR_CHOOSE_VERSION_GAME = (By.CSS_SELECTOR, '#Red\ Dead\ Redemption\ 2_button > span:nth-child(1)')
    LOCATOR_LIST_VERSION_GAME = (By.CSS_SELECTOR, '#Red\ Dead\ Redemption\ 2_menu')
    LOCATOR_ADD_TO_FAVORITES = (By.CSS_SELECTOR, '.css-2o2uxw-CallToActionText__callToActionText')
    LOCATOR_APPLE_ID = (By.ID, 'login-with-apple')
    LOCATOR_CHECK_APPLE = (By.CSS_SELECTOR, '.si-container-title')

class search_game(BasePage):

    def click_field_search(self, word):
        field_search = self.find_element(epic_games_locators.LOCATOR_SEARCH_FIELD)
        field_search.click()
        field_search.clear()
        field_search.send_keys(word)
        return field_search

    def clear_field_search(self):
        clear_button = self.find_element(epic_games_locators.LOCATOR_CLEAR_FIELD_SEARCH)
        clear_button.click()

    def check_empty_field(self):
        text_of_field = self.find_element(epic_games_locators.LOCATOR_SEARCH_FIELD)
        text_of_field=text_of_field.get_attribute('value')
        print('\n' + 'field_search: ' + ' ' + text_of_field)
        assert text_of_field == ''

    def search_result(self, text):
        list_results = self.find_element(epic_games_locators.LOCATOR_SEARCH_RESULT)
        items = list_results.find_elements_by_tag_name("li")
        if items[0].text == 'Искать все игры':
            time.sleep(2)
            #list_results = self.find_element_by_id('search-bar-autocomplete')
            list_results = self.find_element(epic_games_locators.LOCATOR_SEARCH_RESULT)
            items = list_results.find_elements_by_tag_name("li")
            print('all games')
        else:
            True
        for results in items:
            if str(results.text) == text_point5:
                print('\n' + 'Result: ' + str(results.text))
                results.click()  # open Red Dead Redemption 2
                break

    def adults_page(self):
        continue_button = self.find_element(epic_games_locators.LOCATOR_ADULTS_PAGE_BUTTON)
        continue_button.click()

    def choose_version(self, text):
        choose = self.find_element(epic_games_locators.LOCATOR_CHOOSE_VERSION_GAME)
        choose.click()
        list_results = self.find_element(epic_games_locators.LOCATOR_LIST_VERSION_GAME)
        item = list_results.find_elements_by_tag_name("li")
        for result in item:
            if str(result.text) == text_point7:
                print('\n' + 'Result: ' + str(result.text))
                result.click()
                break

    def add_to_favorite(self):
        time.sleep(1)
        add_to_favorite = self.find_element(epic_games_locators.LOCATOR_ADD_TO_FAVORITES)
        add_to_favorite.click()

    def apple_id(self):
        apple_id = self.find_element((epic_games_locators.LOCATOR_APPLE_ID))
        apple_id.click()

    def check_apple(self):
        try:
            apple_text = self.find_element(epic_games_locators.LOCATOR_CHECK_APPLE)
        except NoSuchElementException:
            return False
        return True