import datetime
import pandas as pd

from page_objects.authorization import Authorization
from page_objects.intranet_page import IntranetPage


def authorization(browser, email, password):
    browser.open_page()

    user_authorization = Authorization(browser.wd)
    user_authorization.click_google_login_button()
    user_authorization.fill_email(email)
    user_authorization.fill_password(password)


def parse_info(browser):

    intranet_page = IntranetPage(browser.wd)

    names = intranet_page.get_names_list()
    names_list = []
    for name in names:
        names_list.append(name.text)

    jobs = intranet_page.get_jobs_list()
    jobs_list = []
    for job in jobs:
        jobs_list.append(job.text)

    emails = intranet_page.get_emails_list()
    emails_list = []
    for email in emails:
        lst = email.text.split()
        emails_list.append(lst[-1])

    return names_list, jobs_list, emails_list


def write_results(names_list, jobs_list, emails_list):
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')

    df = pd.DataFrame(list(zip(names_list, jobs_list, emails_list)),
                      columns=['Name', 'Position', 'E-mail'])
    df.to_csv(f'tests/results/{current_date}.csv', index=False)
