"""Trading strategy module for the trading bot."""
import os
from dotenv import load_dotenv
from .market_analyzer import MarketAnalyzer
from typing import Dict, Optional

class TradingStrategy:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        self.market_analyzer = MarketAnalyzer()
        
        # Read configuration from environment variables with defaults
        self.position_size_multiplier = float(os.getenv('POSITION_SIZE_MULTIPLIER', '0.1'))  # Default 10% of available balance
        self.take_profit_percentage = float(os.getenv('TAKE_PROFIT_PERCENTAGE', '5')) / 100  # Convert percentage to decimal
        self.stop_loss_percentage = float(os.getenv('STOP_LOSS_PERCENTAGE', '2')) / 100  # Convert percentage to decimal
        self.max_trades = int(os.getenv('MAX_TRADES', '3'))
        self.min_volume_usd = float(os.getenv('MIN_VOLUME_USD', '1000000'))
        self.price_change_threshold = float(os.getenv('PRICE_CHANGE_THRESHOLD', '5')) / 100
        self.cooldown_minutes = int(os.getenv('COOLDOWN_MINUTES', '30'))
        
    def get_position_size(self) -> float:
        """
        Calculate the position size based on available balance and risk parameters
        """
        # This would typically use the account balance from Binance
        # For now, we'll use a fixed amount for testing
        return 100.0  # $100 position size
        
    def get_take_profit(self, current_price: float) -> Optional[float]:
        """
        Calculate take profit price
        """
        if current_price <= 0:
            return None
        return current_price * (1 + self.take_profit_percentage)
        
    def get_stop_loss(self, current_price: float) -> Optional[float]:
        """
        Calculate stop loss price
        """
        if current_price <= 0:
            return None
        return current_price * (1 - self.stop_loss_percentage)
        
    def should_trade(self) -> bool:
        """
        Determine if we should enter a trade based on market conditions
        """
        # Check market state from analyzer
        market_state = self.market_analyzer.market_state
        
        # Example conditions for trading
        if market_state == "BULLISH":
            return True
        elif market_state == "NEUTRAL" and self.market_analyzer.volume_increasing:
            return True
            
        return False
        
    def update_parameters(self, 
                         position_size_multiplier: Optional[float] = None,
                         take_profit_percentage: Optional[float] = None,
                         stop_loss_percentage: Optional[float] = None):
        """
        Update strategy parameters
        """
        if position_size_multiplier is not None:
            self.position_size_multiplier = position_size_multiplier
        if take_profit_percentage is not None:
            self.take_profit_percentage = take_profit_percentage
        if stop_loss_percentage is not None:
            self.stop_loss_percentage = stop_loss_percentage 