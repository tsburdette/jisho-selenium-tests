import pytest
import sys
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.utils import ChromeType

sys.path.append('pageobjects')
sys.dont_write_bytecode = True

# add cli options
def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='https://jisho.org/', help='Specify the base URL for testing')
    parser.addoption('--driver', action='store', default='chrome', help='Supported browsers: Firefox, Chrome, Chromium, Edge, and IE')

# driver fixture passed to all tests
@pytest.fixture(scope='session')
def driver(request):
    browserName = request.config.getoption('--driver')
    if browserName == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browserName == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browserName == "chromium":
        driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    elif browserName == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif browserName == "ie":
        driver = webdriver.Ie(IEDriverManager().install())
    else:
        raise ValueError('Invalid browser name: ' + browserName)
    driver.set_window_size(1280, 800)
    driver.base_url = request.config.getoption('--url')
    yield driver
    driver.quit()