import datetime
import os

import pandas as pd
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

try:
    from collections.abc import Callable
except ImportError:
    from collections import Callable


def test_parser_info(browser):

    # Загружаем информацию с 'email' и 'password' для авторизации в Intranet:
    conf = yaml.safe_load(open('configuration.yml'))
    email = conf['email']
    password = conf['password']

    try:
        # Открываем страницу с сотрудниками:
        browser.open_page()

        # Ищем кнопку 'Log in with Google' и нажимаем на нее:
        login_google_button = browser.wd.find_element_by_link_text('Log in with Google')
        login_google_button.click()

        # Ожидаем поле 'email', очищаем, вводим данные и нажимаем ENTER:
        email_field = WebDriverWait(browser.wd, 30).until(
            EC.presence_of_element_located((By.NAME, 'identifier')))
        email_field.clear()
        email_field.send_keys(email)
        email_field.send_keys(Keys.ENTER)

        # Ожидаем поле 'password', очищаем, вводим данные и нажимаем ENTER:
        password_field = WebDriverWait(browser.wd, 30).until(
            EC.presence_of_element_located((By.NAME, 'password')))
        browser.wd.implicitly_wait(1)
        browser.wd.find_element_by_name('password').send_keys(password)
        password_field.send_keys(Keys.ENTER)

        # Парсим имена сотрудников:
        names = WebDriverWait(browser.wd, 120).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'profiles-list-item-info-name')))

        # Парсим должности сотрудников:
        jobs = WebDriverWait(browser.wd, 120).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'profiles-list-item-info-position')))

        # Парсим email'ы сотрудников:
        emails = WebDriverWait(browser.wd, 120).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'profiles-list-item-mobile-phone')))

        # Создаем пустой список имен сотрудников:
        names_list = []

        # Добавляем имя каждого сотрудника в список имен:
        for _ in names:
            names_list.append(_.text)

        # Создаем пустой список должностей сотрудников:
        jobs_list = []

        # Добавляем должность каждого сотрудника в список должностей:
        for _ in jobs:
            jobs_list.append(_.text)

        # Создаем пустой список email'ов сотрудников:
        emails_list = []

        # Добавляем email каждого сотрудника в список email'ов:
        for _ in emails:
            lst = _.text.split()
            emails_list.append(lst[-1])

        # Узнаем текущую дату:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')

        # Проверяем если ли папка с результатами, в противном случае создаем:
        try:
            os.stat('results')
        except FileNotFoundError:
            os.mkdir('results')

        # Создаем df с вышеперечисленными списками и записываем его в csv:
        df = pd.DataFrame(list(zip(names_list, jobs_list, emails_list)),
                          columns=['Name', 'Position', 'E-mail'])
        df.to_csv(f'results/{current_date}.csv', index=False)

        # Проверяем, что все списки имеют одинаковую длину:
        assert len(emails_list) == len(names_list) == len(jobs_list)

    finally:

        # Закрываем браузер:
        browser.quit()
