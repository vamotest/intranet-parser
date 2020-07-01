from selenium.webdriver.common.by import By


class IntranetPage:

    names = (By.CLASS_NAME, 'profiles-list-item-info-name')
    jobs = (By.CLASS_NAME, 'profiles-list-item-info-position')
    emails = (By.CLASS_NAME, 'profiles-list-item-mobile-phone')
