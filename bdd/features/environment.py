from examples.fixture_reader import FixtureReader
from examples.login_page import LoginPage
from examples.utils import get_config, get_browser


def before_all(context):
    config = get_config()
    fixtures_path = config.get('fixtures_path')
    context.fixture_reader = FixtureReader(fixtures_path=fixtures_path)
    context.browser_name = config.get('browser_name')
    context.page_url = config.get('page_url')


def before_scenario(context):
    context.driver = get_browser(context.browser_name)
    context.login_page = LoginPage(context.driver, context.page_url)
