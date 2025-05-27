# Coin Trade Bot

A cryptocurrency trading bot that monitors Coinbase Pro Twitter notifications and executes trades on Binance.

## Features

- Monitors Coinbase Pro Twitter feed for new coin listings
- Automatically executes trades on Binance
- Custom trading strategy implementation
- Secure credential management using environment variables
- Modular and extensible architecture

## Project Structure

```
coin-trade-bot/
├── src/
│   └── coin_trade_bot/
│       ├── __init__.py
│       ├── main.py
│       ├── browser_manager.py
│       ├── trading_strategy.py
│       ├── binance_trader.py
│       └── test_env.py
├── .env.example
├── .env
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Prerequisites

- Python 3.13 or higher
- Poetry (Python package manager)
- Binance account with API access
- Twitter account (for monitoring Coinbase Pro)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/coin-trade-bot.git
cd coin-trade-bot
```

2. Install Poetry (if not already installed):
```bash
# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

# macOS / Linux
curl -sSL https://install.python-poetry.org | python3 -
```

3. Configure Poetry to create virtual environment in the project directory:
```bash
poetry config virtualenvs.in-project true
```

4. Install dependencies using Poetry:
```bash
poetry install
```

5. Set up environment variables:
   - Copy `.env.example` to `.env` and update the values:
```
# X (Twitter) API Credentials
X_API_KEY=your_x_api_key_here
X_API_SECRET=your_x_api_secret_here
X_ACCESS_TOKEN=your_x_access_token_here
X_ACCESS_SECRET=your_x_access_secret_here

# Binance API Credentials
BINANCE_API_KEY=your_binance_api_key_here
BINANCE_API_SECRET=your_binance_api_secret_here

# Trading Configuration
TRADE_AMOUNT_USD=100          # Amount to trade in USD
STOP_LOSS_PERCENTAGE=5        # Stop loss percentage
TAKE_PROFIT_PERCENTAGE=10     # Take profit percentage
MAX_TRADES=3                  # Maximum number of concurrent trades
MIN_VOLUME_USD=1000000       # Minimum 24h volume in USD to consider a coin
PRICE_CHANGE_THRESHOLD=5      # Minimum price change percentage to trigger a trade
COOLDOWN_MINUTES=30          # Minutes to wait between trades
```

## Usage

1. Activate the Poetry shell:
```bash
poetry shell
```

2. Verify your environment setup:
```bash
poetry run python src/coin_trade_bot/test_env.py
```

3. Run the bot:
```bash
poetry run python src/coin_trade_bot/main.py
```

## Configuration

All configuration is done through the `.env` file. No code modification is required. The following parameters can be adjusted:

```env
# X (Twitter) API Credentials
X_API_KEY=your_x_api_key_here
X_API_SECRET=your_x_api_secret_here
X_ACCESS_TOKEN=your_x_access_token_here
X_ACCESS_SECRET=your_x_access_secret_here

# Binance API Credentials
BINANCE_API_KEY=your_binance_api_key_here
BINANCE_API_SECRET=your_binance_api_secret_here

# Trading Configuration
TRADE_AMOUNT_USD=100          # Amount to trade in USD
STOP_LOSS_PERCENTAGE=5        # Stop loss percentage
TAKE_PROFIT_PERCENTAGE=10     # Take profit percentage
MAX_TRADES=3                  # Maximum number of concurrent trades
MIN_VOLUME_USD=1000000       # Minimum 24h volume in USD to consider a coin
PRICE_CHANGE_THRESHOLD=5      # Minimum price change percentage to trigger a trade
COOLDOWN_MINUTES=30          # Minutes to wait between trades
```

Simply copy `.env.example` to `.env` and adjust these values according to your trading preferences. The bot will automatically use these settings without requiring any code changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This bot is for educational purposes only. Use at your own risk. Cryptocurrency trading involves significant risk and can result in the loss of your invested capital. You should not invest more than you can afford to lose. 