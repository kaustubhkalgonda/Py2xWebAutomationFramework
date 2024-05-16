from selenium import webdriver
import pytest

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser------>")
    elif browser == 'safari':
        driver = webdriver.Safari()
        print("Launching Safari Browser------>")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome Browser------>")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")



