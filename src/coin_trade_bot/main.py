"""Main module for the trading bot."""
from .browser_manager import BrowserManager
from .twitter_monitor import TwitterMonitor
from .binance_trader import BinanceTrader
from .trading_strategy import TradingStrategy
import datetime
import time
import os
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()
    
    # Initialize components
    browser_manager = BrowserManager()
    twitter_monitor = TwitterMonitor(browser_manager.browser)
    
    # Initialize Binance trader with API credentials
    binance_trader = BinanceTrader(
        api_key=os.getenv('BINANCE_API_KEY'),
        api_secret=os.getenv('BINANCE_API_SECRET')
    )
    
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
            
            # Extract coin from tweet and format for Binance
            coin = tweet["content"].split()[3]
            binance_symbol = f"{coin}USDT"  # Convert to Binance trading pair format
            print(f"Coin: {coin} (Binance Symbol: {binance_symbol})")
            
            # Get market data
            market_data = binance_trader.get_market_data(binance_symbol)
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
            
            # Execute trade if conditions are met
            if strategy.should_trade():
                # Place market order
                order = binance_trader.place_order(
                    symbol=binance_symbol,
                    side='BUY',
                    quantity=position_size,
                    order_type='MARKET'
                )
                print(f"Order placed: {order}")
                
                # Place take profit order
                if take_profit:
                    tp_order = binance_trader.place_order(
                        symbol=binance_symbol,
                        side='SELL',
                        quantity=position_size,
                        order_type='LIMIT',
                        price=take_profit
                    )
                    print(f"Take profit order placed: {tp_order}")
                
                # Place stop loss order
                if stop_loss:
                    sl_order = binance_trader.place_order(
                        symbol=binance_symbol,
                        side='SELL',
                        quantity=position_size,
                        order_type='STOP_LOSS_LIMIT',
                        price=stop_loss
                    )
                    print(f"Stop loss order placed: {sl_order}")
            
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main() 