from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from config import *
import time

class epic_games_locators:
    LOCATOR_SEARCH_FIELD = (By.ID, 'searchInput')
    LOCATOR_CLEAR_FIELD_SEARCH = (By.CLASS_NAME, 'css-682sma')
    LOCATOR_SEARCH_RESULT = (By.ID, 'search-bar-autocomplete')

class search_game(BasePage):

    def click_field_search(self, word):
        print("Кликаем на поле поиска и вводим текст")
        field_search = self.find_element(epic_games_locators.LOCATOR_SEARCH_FIELD)
        field_search.click()
        field_search.clear()
        field_search.send_keys(word)
        return field_search

    def clear_field_search(self):
        print("Очищаем поле поиска")
        clear_button = self.find_element(epic_games_locators.LOCATOR_CLEAR_FIELD_SEARCH)
        clear_button.click()

    def check_empty_field(self):
        print("Проверяем что поле поиска пустое")
        text_of_field = self.find_element(epic_games_locators.LOCATOR_SEARCH_FIELD)
        text_of_field=text_of_field.get_attribute('value')
        print('\n' + 'field_search: ' + ' ' + text_of_field)
        assert text_of_field == ''

    def search_result(self, text):
        print("проверяем результаты поиска")
        list_results = self.find_element(epic_games_locators.LOCATOR_SEARCH_RESULT)
        items = list_results.find_elements_by_tag_name("li")
        print("Если в результатах Искать все игры, то ждём, иначе всё ок")
        if items[0].text == 'Искать все игры':
            time.sleep(2)
            #list_results = self.find_element_by_id('search-bar-autocomplete')
            list_results = self.find_element(epic_games_locators.LOCATOR_SEARCH_RESULT)
            items = list_results.find_elements_by_tag_name("li")
            print('В результатах Все игры')
        else:
            True
        for results in items:
            if str(results.text) == text_point5:
                print('\n' + 'Результат поиска: ' + str(results.text))
                results.click()  # open Red Dead Redemption 2
                break
