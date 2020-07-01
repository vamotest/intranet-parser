from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.intranet_page import IntranetPage as intranet_page


class IntranetPage:

	def __init__(self, browser):
		self.driver = browser

	def get_names_list(self):
		names = WebDriverWait(self.driver, 120).until(
			EC.presence_of_all_elements_located(intranet_page.names))
		return names

	def get_jobs_list(self):
		jobs = WebDriverWait(self.driver, 120).until(
			EC.presence_of_all_elements_located(intranet_page.jobs))
		return jobs

	def get_emails_list(self):
		emails = WebDriverWait(self.driver, 120).until(
			EC.presence_of_all_elements_located(intranet_page.emails))

		return emails
