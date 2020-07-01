# Index
1. [Input information](#input-information)
2. [Output information](#output-information)
3. [How to use](#how-to-use)
4. [To Do List](#to-do-list)

## Input information
На странице сотрудников есть 3 класса элементов, которые содержат информацию:

* Имя сотрудника:
```
<div class="profiles-list-item-info-name">с
    <a href="/team/u/name.surname@domain.com/">Name Surname</a>
</div>
```
* Должность сотрудника:
```
<div class="profiles-list-item-info-position">
    Job Position
</div>
```
* E-mail сотрудника:
```
<div class="profiles-list-item-mobile-phone">
+1 234 567-89-00

	<small>
		<a href="mailto:name.surname@domain.com">name.surname@domain.com</a>
	</small>
</div>
```

**[⬆ Back to Index](#index)**
## Output information
Данные со страницы парсим в отдельный `tests/results/{%Y-%m-%d}.csv` файл в таком виде:

|     Name     |   Position   |          E-mail         |
|:------------:|:------------:|:-----------------------:|
| Name Surname | Job Position | name.surname@domain.com |


**[⬆ Back to Index](#index)**
## How to use
* Установите [актуальную](https://chromedriver.chromium.org/downloads) версию ChromeDriver для вашего Chrome
* Создайте виртуальное окружение и активируйте его:
```shell script
~ python3 -m venv env && source env/bin/activate
```
* Обновите pip до последней версии:
```shell script
~ pip install --upgrade pip
```
* Установите зависимости:
```shell script
~ pip install -r requirements.txt
```
* Создайте конфигурационный файл с данными для Google-авторизации в Intranet:
```shell script
~ nano configuration.yml
```
```
intranet:
  base_url: 'https://domain.com/team/members/'
  user_email: ''
  user_password: ''
  
```
* Запустите тесты:
```shell script
~ python3 -m pytest [--verbose] --html=report.html
```
* Arguments:
```
[--verbose]: increase verbosity
[--html]: generate a HTML report for the test results
```

**[⬆ Back to Index](#index)**
## To Do List
- [ ] Обойти двухфаторную аутентиификацию Google
- [x] PageObject
- [ ] Настроить CI/CD
- [ ] Добавить получение `{%Y-%m-%d}.csv` файла с результатами по e-mail