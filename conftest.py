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


def pytest_addoption(parser):
    parser.addoption("--gamename", action="store", default="Red Dead Redemption 2")


def pytest_generate_tests(metafunc):
    option_value = metafunc.config.option.gamename
    if 'gamename' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("gamename", [option_value])
