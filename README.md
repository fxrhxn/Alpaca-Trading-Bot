# Alpaca Trading Bot

A trading bot that listens for NVDA trade signals from Redis and executes buy/sell orders using the Alpaca API.


# 🚀 Features
- 📡 **Real-Time Signal Processing**: Listens for trade signals (`b` for buy, `s` for sell) in a Redis stream.  
- 📈 **Automated Order Execution**: Executes real-time market orders via Alpaca.  
- ⚡ **Low-Latency Trading**: Optimized for high-speed order execution.  



## 🛠 Installation & Setup

## 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

## 2️⃣ Set Up a Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

## 3️⃣ Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Note: If requirements.txt is missing, install manually:

```bash
pip install redis alpaca-trade-api asyncio python-dotenv
```


## 🔑 API Key Configuration

Set your Alpaca API Keys as environment variables:

### On Mac/Linux (Terminal)
```bash
export APCA_API_KEY_ID="your_api_key_here"
export APCA_API_SECRET_KEY="your_secret_key_here"
```

### On Windows (Command Prompt)
```bash
set APCA_API_KEY_ID=your_api_key_here
set APCA_API_SECRET_KEY=your_secret_key_here
```

### Create a .env (Project Directory)
```bash
APCA_API_KEY_ID=your_api_key_here
APCA_API_SECRET_KEY=your_secret_key_here
```


## 🛠 Running the bot

Ensure Redis is running:

### Terminal
```bash
redis-server
```

Then start the bot:
### Terminal
```bash
python main.py
```


## 📌 Notes
- Ensure your Alpaca API keys are valid.
- Redis must be running before the script starts.
- Only works with Alpaca Paper Trading API (modify `ALPACA_BASE_URL` for live trading).

## 🛠 Troubleshooting

If you encounter errors:

- **ModuleNotFoundError**: Run `pip install -r requirements.txt`
- **Permission Denied**: Use `pip install --user`
- **Redis Connection Issues**: Ensure Redis is running with `redis-server`

