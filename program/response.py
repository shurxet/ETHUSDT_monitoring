from typing import Any

import requests


def price_response(path_api: str, crypto: list) -> str | dict[
    str, dict[str, float | dict[str, float | Any] | Any] | dict[str, float | Any]]:
    data_price = {}

    try:
        for item in range(len(crypto)):
            url = path_api + crypto[item]
            response = requests.get(url)
            data = response.json()
            if data['symbol'] == 'ETHUSDT':
                data_price['ETHUSDT'] = {
                    'name': crypto[item],
                    'price': float(data['price'])
                }
            if data['symbol'] == 'BTCUSDT':
                data_price['BTCUSDT'] = {
                    'name': crypto[item],
                    'price': float(data['price'])
                }

    except Exception as e:
        return f"Error{e}"
    return data_price

