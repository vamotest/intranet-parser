from selenium.webdriver.common.by import By


class Authorization:

    login_button = (By.LINK_TEXT, 'Log in with Google')
    email_field = (By.NAME, 'identifier')
    password_field = (By.NAME, 'password')
