from selenium import webdriver


class Browser:

    def __init__(self, browser, url):
        if browser.lower() == 'chrome':
            self.wd = webdriver.Chrome()
            self.wd.maximize_window()
        elif browser.lower() == 'chrome_headless':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('headless')
            self.wd = webdriver.Chrome(options=chrome_options)
        else:
            raise ValueError(f'Unrecognized browser: {browser}') from Exception
        self.wd.implicitly_wait(20)
        self.url = url

    def open_page(self):
        self.wd.get(self.url)

    def quit(self):
        self.wd.quit()
