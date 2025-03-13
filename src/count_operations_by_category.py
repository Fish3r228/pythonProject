def count_operations_by_category(operations, categories):
    """
    Подсчитывает количество операций по категориям.
    """
    category_count = {category: 0 for category in categories}  # Инициализация словаря с нулевыми значениями

    for operation in operations:
        description = operation.get('description', '').lower()  # Приводим описание к нижнему регистру
        for category in categories:
            if category.lower() in description:  # Проверяем, содержится ли категория в описании
                category_count[category] += 1

    return category_count