from time import sleep
import re
from selenium.webdriver.common.by import By
from seleniumbase import Driver

class Setup:
    def init(self):
        self.browser = Driver(headless=True)

    def close_browser(self):
        self.browser.quit()