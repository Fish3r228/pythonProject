from src.generators import filter_by_currency


def test_filter_by_currency():
    # Тестовые данные
    transactions = [
        {"amount": 100, "currency": "USD"},
        {"amount": 200, "currency": "EUR"},
        {"amount": 300, "currency": "USD"},
        {"amount": 400, "currency": "GBP"},
        {"amount": 500, "currency": "USD"},
    ]

    # Ожидаемый результат
    expected_result = [
        {"amount": 100, "currency": "USD"},
        {"amount": 300, "currency": "USD"},
        {"amount": 500, "currency": "USD"},
    ]

    # Вызываем функцию и преобразуем результат в список
    result = list(filter_by_currency(transactions, "USD"))

    # Проверяем, что результат соответствует ожидаемому
    assert result == expected_result


def test_filter_by_currency_with_other_currency():
    # Тестовые данные
    transactions = [
        {"amount": 100, "currency": "USD"},
        {"amount": 200, "currency": "EUR"},
        {"amount": 300, "currency": "GBP"},
    ]

    # Ожидаемый результат для валюты EUR
    expected_result = [
        {"amount": 200, "currency": "EUR"},
    ]

    # Вызываем функцию и преобразуем результат в список
    result = list(filter_by_currency(transactions, "EUR"))

    # Проверяем, что результат соответствует ожидаемому
    assert result == expected_result

def test_empty_transactions():
    # Тестовые данные (пустой список транзакций)
    transactions = []

    # Ожидаемый результат (пустой список)
    expected_result = []

    # Вызываем функцию и преобразуем результат в список
    result = list(filter_by_currency(transactions, 'USD'))

    # Проверяем, что результат пуст
    assert result == expected_result

from src.generators import transaction_descriptions


def test_transaction_descriptions():
    # Тестовые данные
    transactions = [
        {"amount": 100, "currency": "USD", "description": "Покупка в магазине"},
        {"amount": 200, "currency": "EUR", "description": "Оплата ресторана"},
        {"amount": 300, "currency": "USD", "description": "Перевод другу"},
    ]

    # Ожидаемый результат
    expected_descriptions = [
        "Покупка в магазине",
        "Оплата ресторана",
        "Перевод другу",
    ]

    # Вызываем генератор и преобразуем результат в список
    result = list(transaction_descriptions(transactions))

    # Проверяем, что результат соответствует ожидаемому
    assert result == expected_descriptions

def test_transaction_descriptions_empty_list():
    # Тестовые данные (пустой список транзакций)
    transactions = []

    # Ожидаемый результат (пустой список)
    expected_descriptions = []

    # Вызываем генератор и преобразуем результат в список
    result = list(transaction_descriptions(transactions))

    # Проверяем, что результат пуст
    assert result == expected_descriptions


from src.generators import card_number_generator

def test_card_number_generator_basic():
    # Проверяем, что генератор возвращает правильные номера карт
    generator = card_number_generator(1000, 1005)
    expected_numbers = ["0000 0000 0000 1000", "0000 0000 0000 1001", "0000 0000 0000 1002", "0000 0000 0000 1003",
                        "0000 0000 0000 1004"]

    for expected, actual in zip(expected_numbers, generator):
        assert actual == expected

