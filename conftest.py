import pytest
import pathlib
from pathlib import Path
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='Chrome')


def change_browser(request):

    browser_name = request.config.getoption('--browser', default="Chrome")
    # browser_name = 'Firefox'
    if browser_name == 'Firefox':
        driver = webdriver.Firefox(executable_path=Path(pathlib.Path.cwd(), 'drivers', 'geckodriver.exe'))
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name == 'Chrome':
        driver = webdriver.Chrome(executable_path=Path(pathlib.Path.cwd(), 'drivers', 'chromedriver.exe'))
        # driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


@pytest.fixture(scope='session')
def browser(request):
    driver = change_browser(request)
    yield driver
    driver.quit()
