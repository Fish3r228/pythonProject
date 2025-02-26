import requests

API_KEY = 'kxsl9Rogo3ZzpoEbZaNC4frMXI7soEcl'
BASE_URL = f'http://api.apilayer.com/exchangerates_data/latest?access_key={API_KEY}'

def convert_to_rub(amount, currency):
    """
    Конвертирует сумму в указанной валюте в рубли.
    """
    if currency == 'RUB':
        return float(amount)

    try:
        # Выполняем запрос к API
        response = requests.get(BASE_URL)
        response.raise_for_status()  # Проверяем, что запрос успешен
        data = response.json()

        # Логируем ответ API для отладки
        print("Ответ API:", data)

        # Получаем курс рубля и валюты транзакции
        rub_rate = data['rates'].get('RUB')
        currency_rate = data['rates'].get(currency)

        if not rub_rate or not currency_rate:
            raise ValueError("Курс рубля или валюты не найден в ответе API.")

        # Конвертируем сумму в рубли
        amount_in_rub = (amount / currency_rate) * rub_rate
        return float(amount_in_rub)

    except requests.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return 0.0
    except (KeyError, ValueError) as e:
        print(f"Ошибка при обработке данных: {e}")
        return 0.0