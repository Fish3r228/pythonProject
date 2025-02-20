import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_card_number():
    card_number = "1234567890123456"
    expected_masked_number = "1234 56** **** 3456"
    assert mask_account_card(card_number) == expected_masked_number


def test_mask_account_card_account_number():
    # Номер счета (20 цифр)
    data = "12345678901234567890"
    expected = "**7890"
    assert mask_account_card(data) == expected


def test_mask_account_card_short_account_number():
    # Короткий номер счета (меньше 16 цифр)
    data = "1234567890"
    expected = "**7890"
    assert mask_account_card(data) == expected


def test_mask_account_card_short_input():
    # Слишком короткий ввод
    assert mask_account_card("123") == "123"  # Не маскируется
    assert mask_account_card("12") == "12"


def test_get_data_valid_date():
    # Корректная дата
    date_str = "2023-10-05"
    expected = "05.10.2023"
    assert get_date(date_str) == expected


def test_get_data_leap_year():
    # Корректная дата в високосном году
    date_str = "2020-02-29"
    expected = "29.02.2020"
    assert get_date(date_str) == expected


def test_get_data_single_digit_day_month():
    # Дата с однозначными днем и месяцем
    date_str = "2023-01-01"
    expected = "01.01.2023"
    assert get_date(date_str) == expected


def test_get_date_empty_string():
    # Пустая строка
    with pytest.raises(ValueError, match="Пустая строка. Ожидается дата в формате YYYY-MM-DD."):
        get_date("")
