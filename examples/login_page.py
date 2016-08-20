from examples.login_page_locators import LOCATORS
from examples.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver, page_url):
        super(LoginPage, self).__init__(driver, page_url)
        self.page_url += 'shop/login'
        self._locators = LOCATORS

    def open_page(self):
        self.driver.get(self.page_url)

    def login(self, username, password):
        self.driver.get(self.page_url)
        username_loc = self._locators.get("username_input")
        password_loc = self._locators.get("password_input")

        self.fill_in(username_loc, username)
        self.fill_in(password_loc, password)

        self.click_btn("submit_button")
