"""Market analysis module for the trading bot."""
from typing import List, Dict
import numpy as np

class MarketAnalyzer:
    def __init__(self):
        self.price_history: List[float] = []
        self.volume_history: List[float] = []
        self.market_state = "NEUTRAL"
        self.volume_increasing = False
        
    def update_market_state(self, current_price: float, current_volume: float):
        """
        Update market state based on price and volume data
        """
        self.price_history.append(current_price)
        self.volume_history.append(current_volume)
        
        # Keep only last 100 data points
        if len(self.price_history) > 100:
            self.price_history.pop(0)
        if len(self.volume_history) > 100:
            self.volume_history.pop(0)
            
        # Analyze price trend
        if len(self.price_history) >= 2:
            price_trend = np.mean(np.diff(self.price_history[-10:]))
            if price_trend > 0:
                self.market_state = "BULLISH"
            elif price_trend < 0:
                self.market_state = "BEARISH"
            else:
                self.market_state = "NEUTRAL"
                
        # Analyze volume trend
        if len(self.volume_history) >= 2:
            volume_trend = np.mean(np.diff(self.volume_history[-10:]))
            self.volume_increasing = volume_trend > 0
            
    def get_market_summary(self) -> Dict:
        """
        Get a summary of the current market state
        """
        return {
            "market_state": self.market_state,
            "volume_increasing": self.volume_increasing,
            "price_history_length": len(self.price_history),
            "volume_history_length": len(self.volume_history)
        } 