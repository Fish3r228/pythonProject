# main.py
from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.utils import load_transactions

if __name__ == "__main__":
    try:
        # Пример вызова функции с корректным номером счета
        account_number = 1234567890
        masked_account = get_mask_account(account_number)
        print(f"Замаскированный номер счета: {masked_account}")

        # Пример вызова функции с некорректным номером счета
        invalid_account_number = 123
        masked_invalid_account = get_mask_account(invalid_account_number)
        print(f"Замаскированный номер счета: {masked_invalid_account}")
    except ValueError as e:
        print(f"Ошибка: {e}")
    # Пример использования masks.py
    try:
        card_number = "1234567890123456"
        masked = get_mask_card_number(card_number)
        print(f"Masked card number: {masked}")
    except Exception as e:
        print(f"Error: {e}")

    # Пример использования utils.py
    try:
        data = "example_data"
        if load_transactions(data):
            print("Input is valid")
        else:
            print("Input is invalid")
    except Exception as e:
        print(f"Error: {e}")