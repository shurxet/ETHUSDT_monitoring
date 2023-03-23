from program.crypto_classes import ETHUSDT, BTCUSDT
from program.tracking_logic import Tracking
from program.unit import EthUsdtUnit, BtcUsdtUnit

ethusdt = EthUsdtUnit(ETHUSDT)
btcusdt = BtcUsdtUnit(BTCUSDT)
tracking = Tracking()
tracking.loading_tracking(ethusdt, btcusdt)

print(tracking.start_tracing())
