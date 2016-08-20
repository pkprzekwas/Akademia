from examples.utils import get_browser
from examples.login_page_locators import LOCATORS


class BasePage(object):
    def __init__(self, driver, page_url):
        self.driver = driver
        self.page_url = page_url

    def click_btn(self, locator_name):
        button = self.find_element_by(LOCATORS.get(locator_name))
        button.click()

    def find_element_by(self, locator):
        element = self.driver.find_element(*locator)
        return element

    def fill_in(self, locator, text):
        field = self.find_element_by(locator)
        field.clear()
        field.send_keys(text)