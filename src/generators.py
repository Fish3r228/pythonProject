def filter_by_currency(transactions, currency):
    """
    Фильтрует транзакции по заданной валюте и возвращает итератор.
    """
    for transaction in transactions:
        if transaction.get("currency") == currency:
            yield transaction


# Пример использования

transactions = [
    {"amount": 100, "currency": "USD"},
    {"amount": 200, "currency": "EUR"},
    {"amount": 300, "currency": "USD"},
    {"amount": 400, "currency": "GBP"},
    {"amount": 500, "currency": "USD"},
]

usd_transactions = filter_by_currency(transactions, "USD")

for transaction in usd_transactions:
    print(transaction)


def transaction_descriptions(transactions):
    """
    Генератор, который возвращает описание каждой транзакции по очереди.
    """
    for transaction in transactions:
        yield transaction.get("description")


# Пример списка транзакций
transactions = [
    {"amount": 100, "currency": "USD", "description": "Покупка в магазине"},
    {"amount": 200, "currency": "EUR", "description": "Оплата ресторана"},
    {"amount": 300, "currency": "USD", "description": "Перевод другу"},
]

# Используем генератор
descriptions = transaction_descriptions(transactions)

# Выводим описания транзакций по очереди
for desc in descriptions:
    print(desc)


def card_number_generator(start, end):
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.
    """
    # Преобразуем начальное и конечное значения в целые числа
    start = int(start.replace(" ", "")) if isinstance(start, str) else int(start)
    end = int(end.replace(" ", "")) if isinstance(end, str) else int(end)

    # Генерируем номера карт в диапазоне
    for number in range(start, end + 1):
        # Форматируем номер в формат XXXX XXXX XXXX XXXX
        card_number = f"{number:016d}"  # Дополняем нулями до 16 цифр
        formatted_card_number = " ".join([card_number[i: i + 4] for i in range(0, 16, 4)])
        yield formatted_card_number


# Пример использования 1
# Генерируем номера карт от .... ....0000 0001 до .... .... 0000 0005
card_numbers = card_number_generator("0000 0000 0000 0001", "0000 0000 0000 0005")

# Выводим номера карт
for card in card_numbers:
    print(card)

# Пример использования 2
# Генерируем номера карт от .... ....0000 1000 до .... .... 0000 1005
card_numbers = card_number_generator("0000 0000 0000 1000", "0000 0000 0000 1005")
for card in card_numbers:
    print(card)
