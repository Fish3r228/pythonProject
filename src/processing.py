from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(data, state):
    """
    Фильтрует список словарей по заданному статусу.

    :param data: Список словарей, каждый из которых содержит ключ 'state'.
    :param state: Статус, по которому производится фильтрация.
    :return: Отфильтрованный список словарей.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по ключу 'date'.
    """

    def get_date(item: Dict[str, Any]) -> datetime:
        # Проверяем наличие ключа 'date'
        if "date" not in item:
            raise ValueError("Key 'date' not found in dictionary")

        # Пытаемся преобразовать строку в дату
        try:
            return datetime.strptime(item["date"], "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {item['date']}. Expected format: YYYY-MM-DD") from e

    return sorted(data, key=get_date, reverse=reverse)
