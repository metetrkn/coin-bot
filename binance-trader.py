from binance.client import Client
from binance.exceptions import BinanceAPIException
import time
from typing import Dict, Optional

class BinanceTrader:
    def __init__(self, api_key: str = "", api_secret: str = ""):
        """
        Initialize Binance client
        :param api_key: Binance API key
        :param api_secret: Binance API secret
        """
        self.client = Client(api_key, api_secret)
        
    def get_market_data(self, coin: str) -> Dict[str, float]:
        """
        Get current market data for a specific coin
        :param coin: Trading pair symbol (e.g., 'BTCUSDT')
        :return: Dictionary containing current price and volume
        """
        try:
            # Get 24hr ticker price change statistics
            ticker = self.client.get_ticker(symbol=coin)
            
            return {
                "current_price": float(ticker['lastPrice']),
                "current_volume": float(ticker['volume']),
                "price_change_24h": float(ticker['priceChangePercent']),
                "high_24h": float(ticker['highPrice']),
                "low_24h": float(ticker['lowPrice'])
            }
        except BinanceAPIException as e:
            print(f"Error getting market data: {e}")
            return {
                "current_price": 0.0,
                "current_volume": 0.0,
                "price_change_24h": 0.0,
                "high_24h": 0.0,
                "low_24h": 0.0
            }

    def place_order(self, 
                   symbol: str, 
                   side: str, 
                   quantity: float, 
                   order_type: str = "MARKET",
                   price: Optional[float] = None) -> Dict:
        """
        Place an order on Binance
        :param symbol: Trading pair symbol (e.g., 'BTCUSDT')
        :param side: 'BUY' or 'SELL'
        :param quantity: Amount to trade
        :param order_type: Type of order (MARKET, LIMIT, etc.)
        :param price: Price for limit orders
        :return: Order response from Binance
        """
        try:
            params = {
                'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity
            }
            
            if order_type == "LIMIT" and price:
                params['price'] = price
                params['timeInForce'] = 'GTC'  # Good Till Cancelled
            
            order = self.client.create_order(**params)
            return order
        except BinanceAPIException as e:
            print(f"Error placing order: {e}")
            return {}

    def get_account_balance(self) -> Dict[str, float]:
        """
        Get account balance for all assets
        :return: Dictionary of asset balances
        """
        try:
            account = self.client.get_account()
            balances = {}
            for asset in account['balances']:
                if float(asset['free']) > 0 or float(asset['locked']) > 0:
                    balances[asset['asset']] = {
                        'free': float(asset['free']),
                        'locked': float(asset['locked'])
                    }
            return balances
        except BinanceAPIException as e:
            print(f"Error getting account balance: {e}")
            return {}

    def get_symbol_info(self, symbol: str) -> Dict:
        """
        Get trading pair information
        :param symbol: Trading pair symbol (e.g., 'BTCUSDT')
        :return: Dictionary containing symbol information
        """
        try:
            return self.client.get_symbol_info(symbol)
        except BinanceAPIException as e:
            print(f"Error getting symbol info: {e}")
            return {} 