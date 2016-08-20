import unittest

from examples.login_page import LoginPage
from examples.utils import get_config, get_browser


class TestLoginPage(unittest.TestCase):
    def setUp(self):
        config = get_config()
        _browser_name = config.get('browser_name')
        _page_url = config.get('page_url')
        self.driver = get_browser(_browser_name)
        self.login_page = LoginPage(self.driver, _page_url)

    def test_my_test(self):
        self.assertTrue(True)

    def test_login(self):
        self.login_page.login(username="admin", password="admin")

    def tearDown(self):
        self.driver.quit()
