def get_mask_account(acc_num: int) -> str:
    """Функция которая преобразует номер счета в строку"""
    account_str = str(acc_num)
    # Проверка что длина номера счета достаточна для маскировки
    if len(account_str) < 4:
        raise ValueError("Номер счета должен содержать как минимум 4 цифры")

    # Маскировка номера счета
    masked_card_number = f"**{account_str[-4:]}"
    return masked_card_number


#  пример использования
acc_num = 123123123
masked_card_number = get_mask_account(acc_num)
print(masked_card_number)



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
