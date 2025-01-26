def filter_by_state(data, state="EXECUTED"):
    """
    Фильтрует список словарей по значению ключа 'state'.

    data: Список словарей для фильтрации.
    state: Значение ключа 'state', по которому производится фильтрация. По умолчанию 'EXECUTED'.
    return: Новый список словарей, содержащий только те, у которых ключ 'state' соответствует указанному значению.
    """
    filtered_data = []
    for item in data:
        if item.get("state") == state:
            filtered_data.append(item)
    return filtered_data


def sort_by_date(data, reverse=True):
    """
    Сортирует список словарей по дате.

    data: Список словарей для сортировки.
    reverse: Если True, сортировка по убыванию (по умолчанию). Если False, сортировка по возрастанию.
    return: Новый список словарей, отсортированный по дате.
    """
    return sorted(data, key=lambda x: x.get("date", ""), reverse=reverse)
