def get_mask_account(acc_num: int) -> str:
    """Функция которая преобразует номер счета в строку"""
    account_str = str(acc_num)
    # Проверка что длина номера счета достаточна для маскировки
    if len(account_str) < 4:
        raise ValueError("Номер счета должен содержать как минимум 4 цифры")

    # Маскировка номера счета
    masked_card_number = f"**{account_str[-4:]}"
    return masked_card_number


def get_mask_card_number(card_number:str) -> str:
    """Функция которая преобразует номер карты"""
    if len(card_number) < 10:
        return card_number  # or handle error
    return f"{card_number[:6]}** **** {card_number[-4:]}"
