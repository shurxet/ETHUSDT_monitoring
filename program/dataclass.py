from dataclasses import dataclass
import marshmallow.exceptions
import marshmallow_dataclass

from config import api_binance, crypto_asset
from program.response import price_response

price_response = price_response(path_api=api_binance, crypto=crypto_asset)


# опишем типы данных которые лежат в ETHUSDT
@dataclass
class EthUsdt:
    name: str
    price: float


# опишем типы данных которые лежат в BTCUSDT
@dataclass
class BtcUsdt:
    name: str
    price: float


# у нас в массиве лежат ключи ETHUSDT и BTCUSDT, их и опишем
@dataclass
class CryptoAsset:
    ETHUSDT: EthUsdt
    BTCUSDT: BtcUsdt


# Таким образом с помощью dataclass мы описали апи который мы используем

class CryptoData:
    def __init__(self):
        self.crypto_asset: CryptoAsset = self._crypto_asset_data()

    def get_all_crypto_asset(self):
        return self.crypto_asset

    def get_eth(self):
        return self.crypto_asset.ETHUSDT

    def get_btc(self):
        return self.crypto_asset.BTCUSDT

    @staticmethod
    def _crypto_asset_data() -> CryptoAsset:
        price_response_schema = marshmallow_dataclass.class_schema(CryptoAsset)
        try:
            return price_response_schema().load(price_response)
        except marshmallow.exceptions.ValidationError:
            raise ValueError
