"""X monitoring module for the trading bot."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from typing import Optional, Dict

class XMonitor:
    def __init__(self, browser):
        self.browser = browser
        self.cointelegraph_url = "https://x.com/Cointelegraph"
        self.last_check_time = None
        
    def check_notifications(self) -> Optional[Dict]:
        """
        Check Cointelegraph's X feed for new cryptocurrency listings and news
        Returns a dictionary with coin information if a new listing is found
        """
        try:
            # Navigate to Cointelegraph's X profile
            self.browser.get(self.cointelegraph_url)
            
            # Wait for tweets to load
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tweet']"))
            )
            
            # Get all tweets
            tweets = self.browser.find_elements(By.CSS_SELECTOR, "[data-testid='tweet']")
            
            for tweet in tweets:
                try:
                    # Get tweet timestamp
                    timestamp = tweet.find_element(By.CSS_SELECTOR, "time").get_attribute("datetime")
                    
                    # Skip if we've already seen this tweet
                    if self.last_check_time and timestamp <= self.last_check_time:
                        continue
                    
                    # Get tweet content
                    content = tweet.find_element(By.CSS_SELECTOR, "[data-testid='tweetText']").text
                    
                    # Check for listing announcements or significant news
                    if any(keyword in content.lower() for keyword in [
                        "listing", "inbound", "new asset", "added to", "now available",
                        "launches", "announces", "partnership", "integration"
                    ]):
                        # Extract coin symbols from the tweet
                        # Example: "Coinbase adds $BTC and $ETH to its platform"
                        words = content.split()
                        coins = []
                        for word in words:
                            if word.startswith("$"):
                                coin_symbol = word[1:]  # Remove $ symbol
                                coins.append(coin_symbol)
                        
                        if coins:
                            # Update last check time
                            self.last_check_time = timestamp
                            
                            return {
                                "coins": coins,
                                "content": content,
                                "timestamp": timestamp,
                                "source": "Cointelegraph"
                            }
                except Exception as e:
                    print(f"Error processing tweet: {str(e)}")
                    continue
                    
            return None
            
        except Exception as e:
            print(f"Error checking X feed: {str(e)}")
            return None
            
    def login(self, username: str, password: str) -> bool:
        """
        Login to X account
        """
        try:
            # Navigate to X login page
            self.browser.get("https://x.com/login")
            
            # Wait for login form
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[autocomplete='username']"))
            )
            
            # Enter username
            username_input = self.browser.find_element(By.CSS_SELECTOR, "input[autocomplete='username']")
            username_input.send_keys(username)
            
            # Click next
            next_button = self.browser.find_element(By.CSS_SELECTOR, "[data-testid='LoginForm_Next_Button']")
            next_button.click()
            
            # Wait for password field
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
            )
            
            # Enter password
            password_input = self.browser.find_element(By.CSS_SELECTOR, "input[type='password']")
            password_input.send_keys(password)
            
            # Click login
            login_button = self.browser.find_element(By.CSS_SELECTOR, "[data-testid='LoginForm_Login_Button']")
            login_button.click()
            
            # Wait for login to complete
            time.sleep(5)
            
            return True
            
        except Exception as e:
            print(f"Error logging in to X: {str(e)}")
            return False 