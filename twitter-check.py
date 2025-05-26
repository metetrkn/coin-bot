# twitter_monitor.py
from bs4 import BeautifulSoup
import datetime

class TwitterMonitor:
    def __init__(self, browser):
        self.browser = browser
        
    def check_notifications(self):
        self.browser.get("https://twitter.com/notifications")
        time.sleep(2)
        
        try:
            notification = self.browser.find_element_by_xpath(
                "/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[2]/div/article/div[1]/div[2]/div[1]/div"
            )
            notification.click()
            time.sleep(2)
            
            return self._parse_tweet()
        except Exception as e:
            print(f"Notification error: {str(e)}")
            return None
            
    def _parse_tweet(self):
        html = self.browser.page_source
        soup = BeautifulSoup(html, "lxml")
        
        st1 = soup.find("div", attrs={"class": "css-1dbjc4n"})
        st2 = st1.find("div", attrs={"class": "css-1dbjc4n r-1igl3o0 r-qklmqi r-1adg3ll r-1ny4l3l"})
        st5 = st2.find_all("span", attrs={"class": "css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"})
        
        result = [link.get_text() for link in st5]
        account = result[1]
        tweet_content = " ".join(result[3:])
        
        return {
            "account": account,
            "content": tweet_content,
            "time": datetime.datetime.now()
        }