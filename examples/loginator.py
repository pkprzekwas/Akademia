from examples.login_page_locators import LOCATORS


class BasePage(object):
    def __init__(self, driver):
        self._driver = driver

    @staticmethod
    def fill_in(field, text):
        field.clear()
        field.send_keys(text)

    def click_submit_btn(self):
        button = self.find_element_by(LOCATORS.get("submit_button"))
        button.click()

    def find_element_by(self, locator):
        element = self._driver.find_element(*locator)
        return element


class Loginator(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        # super(self, Loginator).__init__(driver)
        self._locators = LOCATORS

    def login(self, username, password):
        username_loc = self.find_element_by(self._locators.get("username_input"))
        password_loc = self.find_element_by(self._locators.get("password_input"))

        Loginator.fill_in(username_loc, username)
        Loginator.fill_in(password_loc, password)

        self.click_submit_btn()
