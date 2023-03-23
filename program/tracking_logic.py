import time
from art import tprint
from config import constant_time
from program.unit import BaseUnit


class BaseSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Tracking(metaclass=BaseSingleton):
    ETHUSDT = None
    BTCUSDT = None

    def loading_tracking(self, ETH: BaseUnit, BTC: BaseUnit):
        self.ETHUSDT = ETH
        self.BTCUSDT = BTC

    def get_price_ethusdt(self):
        return self.ETHUSDT.get_price()

    def get_price_btcusdt(self):
        return self.BTCUSDT.get_price()

    def start_tracing(self):
        tprint('<<<ETHUSDT>>>')
        print(self.get_price_btcusdt())
        print(self.get_price_ethusdt())
        time.sleep(constant_time)
        input("Если хотите отслеживать ETHUSDT нажмите ENTER:")
        btc_volatility = self.BTCUSDT.get_tracing_data(name_key='BTCUSDT', price_key='price')
        self.ETHUSDT.save_current_price(btc_volatility)
        self.BTCUSDT.save_current_price(btc_volatility)
        while True:
            btc_volatility = self.BTCUSDT.get_tracing_data(name_key='BTCUSDT', price_key='price')
            self.ETHUSDT.get_tracing_data(name_key='ETHUSDT', price_key='price', btc_volatility=btc_volatility)

            time.sleep(constant_time)

    def stop_tracing(self):
        self._instances = {}



