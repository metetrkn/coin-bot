"""Main module for the trading bot."""
from .browser_manager import BrowserManager
from .x_monitor import XMonitor
from .trading_strategy import TradingStrategy
from .binance_trader import BinanceTrader
import time
import os
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()
    
    # Initialize components
    browser_manager = BrowserManager()
    x_monitor = XMonitor(browser_manager.browser)
    trading_strategy = TradingStrategy()
    binance_trader = BinanceTrader(
        api_key=os.getenv('BINANCE_API_KEY'),
        api_secret=os.getenv('BINANCE_API_SECRET')
    )
    
    # Login to X
    if not x_monitor.login(
        username=os.getenv('X_USERNAME'),
        password=os.getenv('X_PASSWORD')
    ):
        print("Failed to login to X. Exiting...")
        return
    
    try:
        while True:
            # Check X feed for new listings
            tweet_info = x_monitor.check_notifications()
            
            if tweet_info:
                print(f"\nNew cryptocurrency news detected at {tweet_info['timestamp']}")
                print(f"Source: {tweet_info['source']}")
                print(f"Content: {tweet_info['content']}")
                print(f"Coins mentioned: {', '.join(tweet_info['coins'])}")
                
                # Process each mentioned coin
                for coin in tweet_info['coins']:
                    # Process the tweet and execute trading strategy
                    if trading_strategy.should_trade():
                        # Get position size and execute trade
                        position_size = trading_strategy.get_position_size()
                        binance_trader.execute_trade(
                            symbol=f"{coin}USDT",
                            position_size=position_size
                        )
            
            # Wait before next check
            time.sleep(60)  # Check every minute
            
    except KeyboardInterrupt:
        print("Bot stopped by user")
    finally:
        browser_manager.close()

if __name__ == "__main__":
    main() 