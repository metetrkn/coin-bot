# market_analyzer.py
import numpy as np
from typing import List

class MarketAnalyzer:
    def __init__(self):
        self.price_history: List[float] = []
        self.volume_history: List[float] = []
        self.market_state = "neutral"  # bull, bear, or neutral
        
    def update_market_state(self, current_price: float, volume: float):
        self.price_history.append(current_price)
        self.volume_history.append(volume)
        
        if len(self.price_history) >= 20:  # Need enough data points
            sma_short = np.mean(self.price_history[-10:])
            sma_long = np.mean(self.price_history[-20:])
            volume_trend = np.mean(self.volume_history[-5:]) > np.mean(self.volume_history[-10:-5])
            
            if sma_short > sma_long and volume_trend:
                self.market_state = "bull"
            elif sma_short < sma_long and not volume_trend:
                self.market_state = "bear"
            else:
                self.market_state = "neutral"
            
            self.price_history = self.price_history[-20:]
            self.volume_history = self.volume_history[-20:]

# trading_strategy.py
class TradingStrategy:
    def __init__(self):
        self.market_analyzer = MarketAnalyzer()
        
    def get_position_size(self, base_amount: float = 11.0) -> float:
        if self.market_analyzer.market_state == "bull":
            return base_amount * 1.5
        elif self.market_analyzer.market_state == "bear":
            return base_amount * 0.5
        return base_amount
    
    def get_take_profit(self, entry_price: float) -> float:
        if self.market_analyzer.market_state == "bull":
            return entry_price * 1.15
        elif self.market_analyzer.market_state == "bear":
            return entry_price * 1.05
        return entry_price * 1.10
    
    def get_stop_loss(self, entry_price: float) -> float:
        if self.market_analyzer.market_state == "bull":
            return entry_price * 0.95
        elif self.market_analyzer.market_state == "bear":
            return entry_price * 0.98
        return entry_price * 0.97