from selenium import webdriver


class WebDriverManager:
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.maximize_window()

    def get_webdriver(self):
        return self._driver

    def shutdown_webdriver(self):
        self._driver.quit()
