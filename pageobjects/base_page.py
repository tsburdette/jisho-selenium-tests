import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    timeouts = {
        'short': 1,
        'medium': 3,
        'long': 6,
        'very-long': 12
    }

    def __init__(self, driver):
        self.driver = driver
        self.base_url = driver.base_url

    def wait_for_element(self, locator, timeout='long'):
        ''' find and wait for single element via css selector (eg #id) '''
        return WebDriverWait(self.driver, self.timeouts[timeout]).until(lambda x: x.find_element_by_css_selector(locator))

    def wait_for_elements(self, locator, timeout='long'):
        ''' find and wait for multiple elements via css selector (eg .class) '''
        return WebDriverWait(self.driver, self.timeouts[timeout]).until(lambda x: x.find_elements_by_css_selector(locator))

    def get_base_url(self):
        return self.base_url

    def goto(self, url):
        url = self.base_url + url
        self.driver.get(url)
        return url

    def element_exists(self, locator):
        return len(self.driver.find_elements_by_css_selector(locator)) > 0

    def wait(self, seconds):
        ''' Try to avoid manually waiting but sometimes we have to '''
        time.sleep(seconds)