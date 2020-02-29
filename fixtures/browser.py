from selenium import webdriver


class Browser:

    def __init__(self, browser, url):
        if browser.lower() == 'chrome':
            self.wd = webdriver.Chrome()
            self.wd.maximize_window()
        else:
            raise ValueError(f'Unrecognized browser: {browser}')
        self.wd.implicitly_wait(20)
        self.url = url

    def open_page(self):
        self.wd.get(self.url)

    def quit(self):
        self.wd.quit()
