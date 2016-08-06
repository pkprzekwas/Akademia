from selenium.webdriver.common.by import By

LOCATORS = {
    "username_input": (By.XPATH, ".//*[@id=\"id_username\"]"),
    "password_input": (By.XPATH, ".//*[@id=\"id_password\"]"),
    "submit_button": (By.XPATH, "html/body/div[1]/div/dir/div/form/button"),
}