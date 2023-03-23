from dataclasses import dataclass

from program.dataclass import CryptoData

eth = CryptoData().get_eth()
btc = CryptoData().get_btc()


@dataclass
class UnitClass:
    name: str
    price: float


ETHUSDT = UnitClass(
    name='ETHUSDT',
    price=eth.price
)

BTCUSDT = UnitClass(
    name="BTCUSDT",
    price=btc.price

)

classes = {
    ETHUSDT.name: ETHUSDT,
    BTCUSDT.name: BTCUSDT
}
