import unittest

# Импортируем функцию, которую будем тестировать
from src.count_operations_by_category import count_transactions_by_type

class TestCountTransactionsByType(unittest.TestCase):
    def test_basic_functionality(self):
        # Проверка базовой функциональности
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
        expected_result = {'Food': 3, 'Transport': 2}
        self.assertEqual(count_transactions_by_type(transactions, category_dict), expected_result)

    def test_unknown_category(self):
        # Проверка обработки неизвестных категорий
        transactions = [
            {'description': 'Grocery Store', 'amount': 50},
            {'description': 'Unknown Store', 'amount': 100},
        ]
        category_dict = {
            'Grocery Store': 'Food',
        }
        expected_result = {'Food': 1, 'Unknown': 1}
        self.assertEqual(count_transactions_by_type(transactions, category_dict), expected_result)

    def test_empty_transactions(self):
        # Проверка пустого списка транзакций
        transactions = []
        category_dict = {
            'Grocery Store': 'Food',
        }
        expected_result = {}
        self.assertEqual(count_transactions_by_type(transactions, category_dict), expected_result)

    def test_empty_category_dict(self):
        # Проверка пустого словаря категорий
        transactions = [
            {'description': 'Grocery Store', 'amount': 50},
            {'description': 'Gas Station', 'amount': 30},
        ]
        category_dict = {}
        expected_result = {'Unknown': 2}
        self.assertEqual(count_transactions_by_type(transactions, category_dict), expected_result)

    def test_multiple_categories(self):
        # Проверка множества категорий
        transactions = [
            {'description': 'Grocery Store', 'amount': 50},
            {'description': 'Gas Station', 'amount': 30},
            {'description': 'Cinema', 'amount': 15},
            {'description': 'Restaurant', 'amount': 40},
        ]
        category_dict = {
            'Grocery Store': 'Food',
            'Restaurant': 'Food',
            'Gas Station': 'Transport',
            'Cinema': 'Entertainment',
        }
        expected_result = {'Food': 2, 'Transport': 1, 'Entertainment': 1}
        self.assertEqual(count_transactions_by_type(transactions, category_dict), expected_result)

if __name__ == '__main__':
    unittest.main()