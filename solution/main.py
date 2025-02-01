import os
import time
import asyncio
import redis
import alpaca_trade_api as tradeapi
from datetime import datetime

# Load environment variables
ALPACA_API_KEY = os.getenv("APCA_API_KEY_ID")
ALPACA_SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
ALPACA_BASE_URL = "https://paper-api.alpaca.markets"

# Ensure API keys are set
if not ALPACA_API_KEY or not ALPACA_SECRET_KEY:
    raise ValueError("Missing Alpaca API credentials. Set them as environment variables.")

# Redis Configuration
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_STREAM = "nvda"

# Initialize Alpaca API
api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL, api_version="v2")

# Initialize Redis
redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

async def execute_trade(direction: str):
    """Executes a market order for NVDA."""
    try:
        order_side = "buy" if direction == "b" else "sell"
        start_time = time.time()

        # Place market order (1 share for simplicity)
        order = await asyncio.to_thread(
            api.submit_order,
            symbol="NVDA",
            qty=1,
            side=order_side,
            type="market",
            time_in_force="gtc",
        )

        execution_time = time.time() - start_time
        print(f"[{datetime.now()}] Executed {order_side.upper()} order for NVDA - Latency: {execution_time:.6f}s")
        return order

    except Exception as e:
        print(f"Trade execution error: {e}")

async def listen_for_signals():
    """Continuously listens for NVDA trading signals from Redis."""
    print("Listening for NVDA trade signals...")
    redis_cursor = "$"  # Start from the latest entry

    while True:
        try:
            # Read latest signal from Redis stream
            response = redis_client.xread({REDIS_STREAM: redis_cursor}, count=1, block=1000)
            if response:
                stream, signals = response[0]
                redis_cursor = signals[-1][0]  # Update cursor to the last processed signal

                for signal in signals:
                    data = signal[1]
                    direction = data.get("Direction")

                    if direction in ["b", "s"]:
                        print(f"[{datetime.now()}] Signal received: {direction.upper()} - Executing trade...")
                        await execute_trade(direction)

        except Exception as e:
            print(f"Redis stream error: {e}")
        await asyncio.sleep(0.01)  # Prevents CPU overuse

def main():
    """Entry point for the trading bot."""
    asyncio.run(listen_for_signals())

if __name__ == "__main__":
    main()
