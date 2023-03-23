from abc import ABC, abstractmethod

from program.crypto_classes import UnitClass

from config import constant_time, api_binance, crypto_asset
from program.response import price_response


class BaseUnit(ABC):
    """
    Базовый класс юнита
    """

    def __init__(self, unit_class: UnitClass):
        self.unit_class = unit_class
        self.name = unit_class.name
        self.price = unit_class.price
        self.percentage_volatility = None
        self._starting_price = None
        self.price_constant_time = None
        self.price_without_influence = None
        self._starting_price_without_influence = None
        self.constant_time = constant_time

    def get_price(self):
        return f"Цена {self.name} на данный момент:  {self.price}"

    @abstractmethod
    def get_price_without_influence(self):
        pass

    def save_current_price(self, btc_volatility=False):
        percentage_starting_price = self.price / 100
        price_difference = percentage_starting_price * btc_volatility
        self._starting_price_without_influence = self.price - price_difference

    def get_tracing_data(self, name_key, price_key, btc_volatility=False):

        current_price = price_response(path_api=api_binance, crypto=crypto_asset)[name_key][price_key]
        percentage_starting_price = self.price / 100
        percentage_current_price = current_price / percentage_starting_price
        self.percentage_volatility = float(percentage_current_price - 100)

        if name_key == "ETHUSDT":
            price_difference = percentage_starting_price * btc_volatility
            self.price_without_influence = current_price - price_difference

            print(f"Цена отслеживания {self.name} без влияния BTCUSDT: {self._starting_price_without_influence}")
            print(f"Текущая цена {self.name}: {current_price}")
            print(f"Текущая цена {self.name} без влияния BTCUSDT: {self.price_without_influence}")
            print(
                f"Процент изменения цены {self.name} за {constant_time} секунд {round(self.percentage_volatility, 5)} %")
            print("=================================================")

            one_percent = self._starting_price_without_influence / 100
            if self._starting_price_without_influence - one_percent > self.price_without_influence:
                print(f"Цена {self.name} упала на 1% или более")
            if self._starting_price_without_influence + one_percent < self.price_without_influence:
                print(f"Цена {self.name} поднялась на 1% или более")

        if name_key == "BTCUSDT":
            return float(self.percentage_volatility)


class EthUsdtUnit(BaseUnit, ABC):

    def get_price_without_influence(self):
        return ""


class BtcUsdtUnit(BaseUnit, ABC):

    def get_price_without_influence(self):
        return ""
