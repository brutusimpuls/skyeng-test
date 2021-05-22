#-*- coding: utf-8 -*-
from selenium import webdriver
import pytest
from config import *


@pytest.fixture(scope="session")
def browser(request):
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(15)
    yield browser
    browser.quit()
    #request.addfinalizer(driver.quit)
    #return driver
