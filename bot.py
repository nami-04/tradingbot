import logging
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException
import time

# Logging Setup
logging.basicConfig(filename='bot.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.api_key = api_key
        self.api_secret = api_secret
        self.testnet = testnet
        self.client = self._init_client()

    def _init_client(self):
        client = Client(self.api_key, self.api_secret)
        if self.testnet:
            client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        return client

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info(f"Market Order: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"Market Order Error: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=str(price)
            )
            logging.info(f"Limit Order: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"Limit Order Error: {e}")
            return None

    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_STOP,
                stopPrice=str(stop_price),
                price=str(limit_price),
                quantity=quantity,
                timeInForce=TIME_IN_FORCE_GTC
            )
            logging.info(f"Stop-Limit Order: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"Stop-Limit Error: {e}")
            return None
