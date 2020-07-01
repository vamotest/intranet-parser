from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from locators.authorization import Authorization as authorization


class Authorization:

	def __init__(self, browser):
		self.driver = browser

	def click_google_login_button(self):
		login_google_button = self.driver.find_element(
			*authorization.login_button)
		login_google_button.click()

	def fill_email(self, email):
		email_field = WebDriverWait(self.driver, 30).until(
			EC.presence_of_element_located(authorization.email_field))
		email_field.clear()
		email_field.send_keys(email)
		email_field.send_keys(Keys.ENTER)

	def fill_password(self, password):
		password_field = WebDriverWait(self.driver, 30).until(
			EC.presence_of_element_located(authorization.password_field))
		self.driver.implicitly_wait(1)
		password_field.send_keys(password)
		password_field.send_keys(Keys.ENTER)
