from collections import Counter


def count_transactions_by_type(transactions, category_dict):
    # Создаем список категорий для каждой транзакции на основе описания
    categories = [category_dict.get(transaction['description'], 'Unknown') for transaction in transactions]

    # Используем Counter для подсчета количества операций по категориям
    category_count = Counter(categories)

    return dict(category_count)


# Пример использования
transactions = [
    {'description': 'Grocery Store', 'amount': 50},
    {'description': 'Gas Station', 'amount': 30},
    {'description': 'Grocery Store', 'amount': 20},
    {'description': 'Restaurant', 'amount': 40},
    {'description': 'Gas Station', 'amount': 25},
]

category_dict = {
    'Grocery Store': 'Food',
    'Restaurant': 'Food',
    'Gas Station': 'Transport',
}

result = count_transactions_by_type(transactions, category_dict)
print(result)