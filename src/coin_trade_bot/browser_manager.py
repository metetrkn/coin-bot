"""Browser management module for the trading bot."""
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

class BrowserManager:
    def __init__(self):
        self.browser = self._setup_browser()
        
    def _setup_browser(self):
        try:
            # Set up Firefox options
            options = Options()
            options.add_argument("-profile")
            options.add_argument(r"C:\Users\user\AppData\Roaming\Mozilla\Firefox\Profiles\j71f4oya.default-release")
            
            # Create a Service object
            service = Service()
            
            # Initialize the browser with the service and options
            browser = webdriver.Firefox(
                service=service,
                options=options
            )
            
            browser.maximize_window()
            time.sleep(1)
            return browser
        except Exception as e:
            print(f"Browser setup error: {str(e)}")
            raise 