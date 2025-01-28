def mask_card_number(card_number: str) -> str:
    # Пример маскировки номера карты: оставляем первые 6 и последние 4 цифры
    return card_number[:6] + "*" * (len(card_number) - 10) + card_number[-4:]


def mask_account_number(account_number: str) -> str:
    # Пример маскировки номера счета: оставляем последние 4 цифры
    return "**" + account_number[-4:]


def mask_card_or_account(input_string: str) -> str:
    # Разделяем строку на тип и номер
    parts = input_string.split()
    type_ = " ".join(parts[:-1])  # Тип может состоять из нескольких слов (например, "Visa Platinum")
    number = parts[-1]  # Последний элемент — это номер карты или счета

    # Определяем тип и применяем соответствующую маскировку
    if "Счет" in type_:
        masked_number = mask_account_number(number)
    else:
        masked_number = mask_card_number(number)

    # Возвращаем строку с замаскированным номером
    return f"{type_} {masked_number}"