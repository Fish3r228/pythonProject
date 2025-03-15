import re


def filter_operations_by_description(operations, search_string):
    """
    Фильтрует список словарей с данными о банковских операциях по наличию строки в описании.
    """
    filtered_operations = []
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)  # Игнорируем регистр

    for operation in operations:
        if 'description' in operation and pattern.search(operation['description']):
            filtered_operations.append(operation)

    return filtered_operations