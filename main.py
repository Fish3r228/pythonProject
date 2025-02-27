# main.py
from src.logger_masks import mask_card_number
from src.logger_utils import validate_input

if __name__ == "__main__":
    # Пример использования masks.py
    try:
        card_number = "1234567890123456"
        masked = mask_card_number(card_number)
        print(f"Masked card number: {masked}")
    except Exception as e:
        print(f"Error: {e}")

    # Пример использования utils.py
    try:
        data = "example_data"
        if validate_input(data):
            print("Input is valid")
        else:
            print("Input is invalid")
    except Exception as e:
        print(f"Error: {e}")