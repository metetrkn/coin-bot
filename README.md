# Coin Trade Bot

An automated cryptocurrency trading bot that monitors Coinbase Pro Twitter notifications and executes trades on FTX based on market analysis.

## Features

- Monitors Coinbase Pro Twitter notifications for new coin listings
- Analyzes market data and trading volumes
- Implements automated trading strategies
- Executes trades on FTX exchange
- Real-time market state monitoring
- Configurable position sizing and risk management

## Prerequisites

- Python 3.7+
- FTX API credentials
- Twitter account access
- Required Python packages (see Installation)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/coin-trade-bot.git
cd coin-trade-bot
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Configure your credentials:
   - Set up your FTX API credentials
   - Configure Twitter access credentials

## Project Structure

- `main.py` - Main application entry point
- `browser_manager.py` - Manages browser automation
- `twitter-check.py` - Twitter notification monitoring
- `ftx-trader.py` - FTX trading functionality
- `market-analyser.py` - Market analysis and strategy implementation

## Usage

1. Configure your trading parameters in the strategy configuration
2. Run the bot:
```bash
python main.py
```

The bot will:
- Monitor Coinbase Pro Twitter notifications
- Analyze market conditions when new coins are listed
- Execute trades based on configured strategies
- Monitor positions and manage risk

## Trading Strategy

The bot implements a strategy that:
- Monitors market state and volume
- Calculates optimal position sizes
- Sets take-profit and stop-loss levels
- Executes trades based on market conditions

## Risk Warning

This bot is for educational purposes only. Cryptocurrency trading involves significant risk. Always:
- Start with small amounts
- Test thoroughly in a paper trading environment
- Monitor the bot's performance
- Never trade with funds you cannot afford to lose
- All risk belongs to user

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 