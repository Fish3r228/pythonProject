import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

def convert_to_rub(amount, currency):
    """
    Конвертирует сумму транзакции в рубли.
    """
    if currency == "RUB":
        return float(amount)

    # Получаем API-ключ из переменных окружения
    api_key = os.getenv("EXCHANGE_RATES_API_KEY")
    if not api_key:
        raise ValueError("API key not found in environment variables.")

    # Делаем запрос к API для получения курса валют
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}"
    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch exchange rates: {response.status_code}")

    data = response.json()
    rate = data["rates"]["RUB"]
    return float(amount) * rate