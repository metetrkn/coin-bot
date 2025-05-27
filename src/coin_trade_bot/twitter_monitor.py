"""Twitter monitoring module for the trading bot."""
from bs4 import BeautifulSoup
import time
from typing import Dict, Optional

class TwitterMonitor:
    def __init__(self, browser):
        self.browser = browser
        self.last_check_time = None
        
    def check_notifications(self) -> Optional[Dict]:
        """
        Check Twitter notifications for new Coinbase Pro listings
        :return: Dictionary containing tweet information if found, None otherwise
        """
        try:
            # Navigate to Twitter notifications
            self.browser.get("https://twitter.com/notifications")
            time.sleep(2)  # Wait for page to load
            
            # Get page source and parse with BeautifulSoup
            html = self.browser.page_source
            soup = BeautifulSoup(html, "lxml")
            
            # Find tweets (this is a simplified example)
            tweets = soup.find_all("article")
            
            for tweet in tweets:
                # Extract tweet information
                account = tweet.find("span", {"class": "css-901oao"})
                content = tweet.find("div", {"class": "css-901oao"})
                time_element = tweet.find("time")
                
                if account and content and time_element:
                    tweet_info = {
                        "account": account.get_text(),
                        "content": content.get_text(),
                        "time": time_element.get("datetime")
                    }
                    
                    # Check if this is a new tweet
                    if self.last_check_time is None or tweet_info["time"] > self.last_check_time:
                        self.last_check_time = tweet_info["time"]
                        return tweet_info
            
            return None
            
        except Exception as e:
            print(f"Error checking Twitter notifications: {str(e)}")
            return None 