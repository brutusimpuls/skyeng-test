from epicgamesstore import search_game
from config import *
import time
import config

def test_search(browser):
    browser.get(base_url)
    search_page=search_game(browser)
    search_page.click_field_search(text_point2)
    search_page.clear_field_search()
    search_page.check_empty_field()
    time.sleep(1)

def test_redemption(browser):
    search_page=search_game(browser)
    search_page.click_field_search(text_point2)
    search_page.search_result(text_point5)

def test_confirm_age(browser):
    search_page = search_game(browser)
    search_page.adults_page()

def test_add_to_favorite(browser):
    search_page = search_game(browser)
    search_page.choose_version(text_point7)
    search_page.add_to_favorite()

def test_apple_id(browser):
    search_page = search_game(browser)
    search_page.apple_id()
    search_page.driver.switch_to.window(browser.window_handles[1])
    search_page.check_apple()


def test_quit(browser):
    time.sleep(2)
    search_page = search_game(browser)
    search_page.driver.quit()
