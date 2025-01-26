def get_mask_card_number(card_number: int) -> str:
    """Функция которая преобразует номер карты в строку"""
    card_str = str(card_number)
    # проверяем что длина номера карты корректна
    if len(card_str) != 16:
        raise ValueError("Номер карты должен состоять из 16 цифр")

    # Маскируем номер карты по правилу XXXX XX ** **** XXXX
    masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"

    return masked_card


# Пример использования
card_number = 1234567812345678
masked_card = get_mask_card_number(card_number)
print(masked_card)
