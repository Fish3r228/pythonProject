import json
from typing import List, Dict


def load_transactions(file_path: str) -> List[Dict]:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.
    """
    try:
        # Открываем файл и загружаем данные
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Проверяем, что данные являются списком
        if isinstance(data, list):
            return data
        else:
            return []

    except (FileNotFoundError, json.JSONDecodeError):
        # Если файл не найден или не удалось декодировать JSON
        return []


# Пример использования
transactions_file_path = 'data/operations.json'  # Переименовали переменную
transactions = load_transactions(transactions_file_path)
print(transactions)