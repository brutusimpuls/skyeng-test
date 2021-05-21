from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from config import *
import time

class all_games_pages_loacators:
    LOCATOR_ADD_TO_FAVORITES = (By.CSS_SELECTOR, '.css-2o2uxw-CallToActionText__callToActionText')

class all_games(BasePage):
    def add_to_favorite(self):
        time.sleep(1)
        add_to_favorite = self.find_element(all_games_pages_loacators.LOCATOR_ADD_TO_FAVORITES)
        add_to_favorite.click()