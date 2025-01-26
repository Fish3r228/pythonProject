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
