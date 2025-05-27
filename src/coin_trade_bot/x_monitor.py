"""X monitoring module for the trading bot."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class XMonitor:
    def __init__(self, browser):
        self.browser = browser
        
    def check_notifications(self):
        """
        Check X notifications for new Coinbase Pro listings
        """
        try:
            # Navigate to X notifications
            self.browser.get("https://x.com/notifications")
            
            # Wait for notifications to load
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tweet']"))
            )
            
            # Get all tweets
            tweets = self.browser.find_elements(By.CSS_SELECTOR, "[data-testid='tweet']")
            
            for tweet in tweets:
                # Check if tweet is from Coinbase Pro
                try:
                    author = tweet.find_element(By.CSS_SELECTOR, "[data-testid='User-Name']").text
                    if "Coinbase Pro" in author:
                        # Check if it's a new listing announcement
                        content = tweet.find_element(By.CSS_SELECTOR, "[data-testid='tweetText']").text
                        if "listing" in content.lower():
                            return content
                except:
                    continue
                    
            return None
            
        except Exception as e:
            print(f"Error checking X notifications: {str(e)}")
            return None 