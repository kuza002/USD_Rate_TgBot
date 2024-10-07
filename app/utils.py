import requests
from typing import Optional
import logging


def get_exchange_rate()-> Optional[float]:
    try:
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        response.raise_for_status()
        data = response.json()
        return data['Valute']['USD']['Value']
    except requests.exceptions.RequestException as e:
        logging.exception(f"Error while requesting API: {e}")
        return None


if __name__ == '__main__':
    print(get_exchange_rate())
