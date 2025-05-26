# main.py
from browser_manager import BrowserManager
from twitter_monitor import TwitterMonitor
from ftx_trader import FTXTrader
from trading_strategy import TradingStrategy
import datetime

def main():
    # Initialize components
    browser_manager = BrowserManager()
    twitter_monitor = TwitterMonitor(browser_manager.browser)
    ftx_trader = FTXTrader(browser_manager.browser)
    strategy = TradingStrategy()
    
    # Main trading loop
    while True:
        now = datetime.datetime.now()
        print(f"Checking at {now.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Check Twitter notifications
        tweet = twitter_monitor.check_notifications()
        
        if tweet and tweet["account"] == "@CoinbasePro" and "Inbound" in tweet["content"]:
            print(f"\nCoinbase Tweet Detected at {tweet['time']}")
            print(f"User: {tweet['account']}")
            
            # Extract coin from tweet
            coin = tweet["content"].split()[3]
            print(f"Coin: {coin}")
            
            # Get market data
            market_data = ftx_trader.get_market_data(coin)
            current_price = market_data["current_price"]
            current_volume = market_data["current_volume"]
            
            # Update strategy
            strategy.market_analyzer.update_market_state(current_price, current_volume)
            
            # Get trading parameters
            position_size = strategy.get_position_size()
            take_profit = strategy.get_take_profit(current_price)
            stop_loss = strategy.get_stop_loss(current_price)
            
            print(f"\nMarket State: {strategy.market_analyzer.market_state}")
            print(f"Position Size: ${position_size:.2f}")
            print(f"Take Profit: ${take_profit:.2f}")
            print(f"Stop Loss: ${stop_loss:.2f}")
            
            # Execute trade (implementation would go here)
            # ftx_trader.place_order(coin, position_size)
            
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()