import unittest

from examples.utils import get_config
from examples.login_page import LoginPage


class TestLogin(unittest.TestCase):
    def setUp(self):
        config = get_config()
        browser_name = config.get('browser_name')
        page_url = config.get('page_url')
        self.login_page = LoginPage(browser_name, page_url)

    def test_login(self):
        self.login_page.login(username="admin", password="admin")
