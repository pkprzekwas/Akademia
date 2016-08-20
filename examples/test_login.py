import unittest

from examples.utils import get_browser, get_config
from examples.loginator import Loginator


class TestLogin(unittest.TestCase):
    def setUp(self):
        config = get_config()
        browser_name = config.get('browser_name')
        browser_driver = get_browser(browser_name)
        browser_driver.get('http://localhost:8000/shop/login')
        self.loginator = Loginator(browser_driver)

    def test_login(self):
        self.loginator.login(username="admin", password="admin")
