import pytest
from selenium import webdriver


def change_browser():
    browser_name = 'Chrome'
    if browser_name == 'Firefox':
        driver = webdriver.Firefox(executable_path='../geckodriver.exe')
    else:
        driver = webdriver.Chrome(executable_path='../chromedriver.exe')
    return driver


@pytest.fixture(scope='session')
def browser():
    driver = change_browser()
    yield driver
    driver.quit()
