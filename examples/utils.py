import os
import json

from selenium import webdriver


def get_config(config_file='config.json'):
    dir_path = os.path.dirname(__file__)
    config_path = os.path.join(dir_path, config_file)
    with open(config_path) as f:
        return json.load(f)


def get_browser(browser_name):
    return webdriver.__dict__.get(browser_name)()


