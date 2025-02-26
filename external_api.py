import os
import requests
from typing import Dict

# Загружаем переменные окружения из файла .env
from dotenv import load_dotenv

load_dotenv()

def convert_to_rub(transaction: Dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.
    """
    # Проверяем, что транзакция содержит необходимые ключи
    if not all(key in transaction for key in ['amount', 'currency']):
        raise ValueError("Транзакция должна содержать ключи 'amount' и 'currency'.")

    amount = transaction['amount']
    currency = transaction['currency']

    # Если валюта уже рубли, возвращаем сумму
    if currency == 'RUB':
        return float(amount)

    # Получаем API-ключ из переменных окружения
    api_key = os.getenv('EXCHANGE_RATES_API_KEY')
    if not api_key:
        raise RuntimeError("API-ключ не найден. Убедитесь, что он указан в файле .env.")

    # URL для получения курсов валют
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"

    # Заголовок с API-ключом
    headers = {
        "apikey": api_key
    }

    try:
        # Выполняем запрос к API
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверяем, что запрос успешен
        data = response.json()

        # Получаем курс валюты к рублю
        rub_rate = data['rates']['RUB']
        amount_in_rub = amount * rub_rate
        return float(amount_in_rub)

    except requests.RequestException as e:
        raise RuntimeError(f"Ошибка при получении курса валют: {e}")
    except KeyError:
        raise RuntimeError("Не удалось получить курс для указанной валюты.")