# browser_manager.py
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class BrowserManager:
    def __init__(self):
        self.browser = self._setup_browser()
        
    def _setup_browser(self):
        try:
            options = Options()
            options.add_argument("-profile")
            options.add_argument(r"C:\Users\user\AppData\Roaming\Mozilla\Firefox\Profiles\j71f4oya.default-release")
            firefox_capabilities = DesiredCapabilities.FIREFOX
            firefox_capabilities['marionette'] = True
            browser = webdriver.Firefox(
                capabilities=firefox_capabilities, 
                firefox_options=options
            )
            browser.maximize_window()
            time.sleep(1)
            return browser
        except Exception as e:
            print(f"Browser setup error: {str(e)}")
            raise