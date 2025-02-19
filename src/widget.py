def mask_account_card(data: str) -> str:
    """
    Маскирует номер счета или карты.
    data: Номер счета или карты.
    return: Замаскированный номер.
    """
    # Оставляем только цифры
    digits = "".join([char for char in data if char.isdigit()])

    # Если это номер карты (16 цифр)
    if len(digits) == 16:
        # Форматируем номер карты с пробелами: "1234 56** **** 3456"
        return f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
    # Если это номер счета (больше 4 цифр)
    elif len(digits) > 4:
        return "**" + digits[-4:]
    # Если данных недостаточно
    else:
        return data


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
        masked_number = mask_account_card(number)

    # Возвращаем строку с замаскированным номером
    return f"{type_} {masked_number}"


def get_date(date_string: str) -> str:
    # Проверка на пустую строку
    if not date_string:
        raise ValueError("Пустая строка. Ожидается дата в формате YYYY-MM-DD.")

    # Проверка длины строки
    if len(date_string) != 10:
        raise ValueError("Некорректная длина строки. Ожидается дата в формате YYYY-MM-DD.")

    # Проверка формата (наличие дефисов на правильных позициях)
    if date_string[4] != "-" or date_string[7] != "-":
        raise ValueError("Некорректный формат даты. Ожидается YYYY-MM-DD.")

    # Извлекаем год, месяц и день с помощью срезов
    year = date_string[0:4]
    month = date_string[5:7]
    day = date_string[8:10]

    # Проверка, что год, месяц и день состоят из цифр
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        raise ValueError("Год, месяц и день должны состоять из цифр.")

    # Форматируем дату в "ДД.ММ.ГГГГ"
    formatted_date = f"{day}.{month}.{year}"

    return formatted_date
