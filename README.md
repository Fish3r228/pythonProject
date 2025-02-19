# Обработка данных банковских карт 
Этот проект представляет собой набор функций для проверки подлинности банковских карт и их реквизитов. Основное внимание уделено фильтрации и сортировке данных по заданным критериям.

## Цель проекта

Предоставить удобные инструменты для работы с данными, которые позволяют:
- Отфильтровка номера карты и скрытие некоторых данных(get_mask_account.py)
- Сортировка карт и их владельцев по сроку годности карт(get_mask_card_number.py)
- Фильтровать данные по состоянию (`state`).(filter_by_state.py)
- Сортировать данные по дате (`date`) в порядке убывания или возрастания.(filter_by_state.py)

## Пример использования фунции (filter_by_state.py)

data = [
    {'id': 321342341, 'state': 'EXECUTED', 'date': '2021-04-03T15:34:27.234234'},
    {'id': 275235213, 'state': 'PENDING', 'date': '2018-05-04T16:35:28.634634'},
    {'id': 213586794, 'state': 'EXECUTED', 'date': '2017-06-05T17:36:29.123123'},
    {'id': 125425743, 'state': 'CANCELED', 'date': '2011-07-06T18:37:30.585585'},
]

- Фильтрация по умолчанию (state='EXECUTED')
filtered_data = filter_by_state(data)
print(filtered_data)

- Фильтрация по state='PENDING'
filtered_data_pending = filter_by_state(data, 'PENDING')
print(filtered_data_pending)

## Тесты 
- Чтобы запустить все тесты, выполните следующую команду:
pytest
- Измерение покрытия кода
Для измерения покрытия кода тестами используется библиотека pytest-cov. Чтобы измерить покрытие и сгенерировать отчёт в формате HTML, выполните команду:
pytest --cov=your_module --cov-report=html tests/
Замените your_module на имя вашего модуля (например, processing).
- Просмотр отчёта
После выполнения команды отчёт будет сохранён в директории htmlcov. Откройте файл htmlcov/index.html в браузере, чтобы просмотреть результаты.
- Структура тестов
Тесты находятся в директории tests/. Каждый тестовый файл соответствует определённому модулю или функциональности. Например:
tests/test_processing.py: Тесты для модуля processing.py.
- Пример теста
def test_get_mask_account_with_spaces():
    account_number = "1234 5678 9012 3456"
    expected = "**3456"
    assert get_mask_account(account_number) == expected
- Основные команды работы с тестами:
pytest: Фреймворк для написания и запуска тестов.
pytest-cov: Плагин для измерения покрытия кода тестами.

## Generators 
Добавил примеры использования функций filter_by_currency, transaction_descriptions, card_number_generator:
- filter_by_currency
transactions = [
    {"amount": 100, "currency": "USD"},
    {"amount": 200, "currency": "EUR"},
    {"amount": 300, "currency": "USD"},
    {"amount": 400, "currency": "GBP"},
    {"amount": 500, "currency": "USD"},
]
- transaction_descriptions
transactions = [
    {"amount": 100, "currency": "USD", "description": "Покупка в магазине"},
    {"amount": 200, "currency": "EUR", "description": "Оплата ресторана"},
    {"amount": 300, "currency": "USD", "description": "Перевод другу"},
]
- card_number_generator
card_numbers = card_number_generator("0000 0000 0000 0001", "0000 0000 0000 0005")

- Для проверки тестов/ переходите в файл test_generation  и пропишите в консоли команду pytest 

## Установка

1. Склонируйте репозиторий на ваш компьютер:
   ```bash
   git clone git@github.com:Fish3r228/homework_10_1.git
   