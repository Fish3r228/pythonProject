import pytest


# По разделу masks.py
@pytest.fixture
def test_get_mask_card_number_short():
    return "123456"


@pytest.fixture
def test_get_mask_card_number_long():
    return "123456** **** 7890"


@pytest.fixture
def test_get_mask_card_number_empty():
    return ""


@pytest.fixture
def test_get_mask_account_standard():
    return "**3456"


@pytest.fixture
def test_get_mask_account_with_spaces():
    return "**3456"


@pytest.fixture
def test_get_mask_account_long():
    return "**7890"


@pytest.fixture
def test_get_mask_account_four_digits():
    return "**1234"


# По разделу widget.py


@pytest.fixture
def test_mask_account_card_card_number():
    return "1234 56** **** 3456"


@pytest.fixture
def test_mask_account_card_account_number():
    return "**7890"


@pytest.fixture
def test_mask_account_card_short_account_number():
    return "**7890"


@pytest.fixture
def test_mask_account_card_short_input():
    return "12"


@pytest.fixture
def test_get_data_valid_date():
    return "05.10.2023"


@pytest.fixture
def test_get_data_leap_year():
    return "29.02.2020"


@pytest.fixture
def test_get_data_single_digit_day_month():
    return "01.01.2023"


# По разделу processing.py


@pytest.fixture
def test_filter_by_state_active():
    return [
        {"name": "Alice", "state": "active"},
        {"name": "Charlie", "state": "active"},
    ]


@pytest.fixture
def test_filter_by_state_empty_input():
    return []


@pytest.fixture
def test_sort_by_date_ascending():
    return [
        {"name": "Event 4", "date": "2023-01-01"},
        {"name": "Event 2", "date": "2023-09-15"},
        {"name": "Event 1", "date": "2023-10-01"},
        {"name": "Event 3", "date": "2023-12-25"},
    ]


@pytest.fixture
def test_sort_by_date_descending():
    return [
        {"name": "Event 3", "date": "2023-12-25"},
        {"name": "Event 1", "date": "2023-10-01"},
        {"name": "Event 2", "date": "2023-09-15"},
        {"name": "Event 4", "date": "2023-01-01"},
    ]


@pytest.fixture
def test_sort_by_date_ascending_1():
    return [
        {"name": "Event 4", "date": "2023-01-01"},
        {"name": "Event 2", "date": "2023-09-15"},
        {"name": "Event 1", "date": "2023-10-01"},
        {"name": "Event 3", "date": "2023-12-25"},
    ]


@pytest.fixture
def test_sort_by_date_ascending_2():
    return [
        {"name": "Event 4", "date": "2023-01-01"},
        {"name": "Event 2", "date": "2023-09-15"},
        {"name": "Event 1", "date": "2023-10-01"},
        {"name": "Event 3", "date": "2023-12-25"},
    ]


# По разделу generators.py


@pytest.fixture
def test_filter_by_currency():
    return [
        {"amount": 100, "currency": "USD"},
        {"amount": 300, "currency": "USD"},
        {"amount": 500, "currency": "USD"},
    ]


@pytest.fixture
def test_filter_by_currency_with_other_currency():
    return [
        {"amount": 200, "currency": "EUR"},
    ]


@pytest.fixture
def test_empty_transactions():
    return []


@pytest.fixture
def test_transaction_descriptions():
    return [
        "Покупка в магазине",
        "Оплата ресторана",
        "Перевод другу",
    ]


@pytest.fixture
def test_transaction_descriptions_empty_list():
    return []


@pytest.fixture
def test_card_number_generator_basic():
    return [
        "0000 0000 0000 1000",
        "0000 0000 0000 1001",
        "0000 0000 0000 1002",
        "0000 0000 0000 1003",
        "0000 0000 0000 1004",
    ]
