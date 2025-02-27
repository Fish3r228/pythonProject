from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    # Стандартный 16-значный номер карты
    card_number = "1234567890123456"
    expected = "123456** **** 3456"
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_short():
    # Короткий номер карты (меньше 10 цифр)
    card_number = "123456"
    expected = "123456"  # или можно ожидать ошибку
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_long():
    # Длинный номер карты (больше 16 цифр)
    card_number = "12345678901234567890"
    expected = "123456** **** 7890"
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_empty():
    # Пустая строка
    card_number = ""
    expected = ""  # или можно ожидать ошибку
    assert get_mask_card_number(card_number) == expected


def test_get_mask_account_standard():
    # Стандартный номер счета
    account_number = "1234567890123456"
    expected = "**3456"
    assert get_mask_account(account_number) == expected


def test_get_mask_account_with_spaces():
    # Номер счета с пробелами
    account_number = "1234 5678 9012 3456"
    expected = "**3456"
    assert get_mask_account(account_number) == expected


def test_get_mask_account_long():
    # Длинный номер счета
    account_number = "12345678901234567890"
    expected = "**7890"
    assert get_mask_account(account_number) == expected


def test_get_mask_account_four_digits():
    # Номер счета из четырех цифр
    account_number = "1234"
    expected = "**1234"
    assert get_mask_account(account_number) == expected
