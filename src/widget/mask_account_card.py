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


# Примеры использования
print(mask_card_or_account("Visa Platinum 7000792289606361"))  # Visa Platinum 700079******6361
print(mask_card_or_account("Maestro 7000792289606361"))  # Maestro 700079******6361
print(mask_card_or_account("Счет 73654108430135874305"))  # Счет **4305


def get_date(date_string: str) -> str:
    # Извлекаем год, месяц и день с помощью срезов
    year = date_string[0:4]
    month = date_string[5:7]
    day = date_string[8:10]

    # Форматируем дату в "ДД.ММ.ГГГГ"
    formatted_date = f"{day}.{month}.{year}"

    return formatted_date


# Пример использования
print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
