from examples.utils import get_browser, get_config

if __name__ == "__main__":
    config = get_config()
    browser_name = config.get('browser_name')

    browser = get_browser(browser_name)
    browser.get('http://localhost:8000/shop/login')

    element = browser.find_element_by_id("id_username")
    print('username: ', element.text)

    browser.close()
