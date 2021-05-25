from Pages.epicgamesstore import search_game
from Pages.cookies import *
from Pages.adults import *
from Pages.red_dead_redemption_2 import *
from Pages.all_games_pages import *
from Pages.login import *
from config import *
import time


def test_search(browser, gamename):
    browser.get(base_url)
    time.sleep(1)

    search_page=search_game(browser)
    search_page.click_field_search(gamename)
    search_page.clear_field_search()
    search_page.check_empty_field()

    cookies = cookies_block(browser)
    cookies.agree_button()
    time.sleep(1)

def test_redemption(browser, gamename):
    search_page=search_game(browser)
    search_page.click_field_search(gamename)
    search_page.search_result(text_point5)

def test_confirm_age(browser):
    continue_button = adults_agree(browser)
    continue_button.adults_page()

def test_add_to_favorite(browser):
    redemption2 = redemption_game_page(browser)
    redemption2.choose_redemption2(text_point7)
    add_button=all_games(browser)
    add_button.add_to_favorite()

def test_apple_id(browser):
    login_page = login(browser)
    login_page.apple_id()
    login_page.driver.switch_to.window(browser.window_handles[1])
    login_page.check_apple()



def test_quit(browser):
    time.sleep(2)
    search_page = search_game(browser)
    search_page.driver.quit()
