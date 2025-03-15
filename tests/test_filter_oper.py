import unittest
from src.filter_operations_by_description import filter_operations_by_description  # Импортируем функцию

class TestFilterOperationsByDescription(unittest.TestCase):
    def test_basic_filtering(self):
        # Проверка базовой фильтрации
        operations = [
            {'description': 'Grocery Store', 'amount': 50},
            {'description': 'Gas Station', 'amount': 30},
            {'description': 'Restaurant', 'amount': 40},
        ]
        search_string = 'grocery'
        expected_result = [{'description': 'Grocery Store', 'amount': 50}]
        self.assertEqual(filter_operations_by_description(operations, search_string), expected_result)

    def test_case_insensitivity(self):
        # Проверка игнорирования регистра
        operations = [
            {'description': 'Grocery Store', 'amount': 50},
            {'description': 'grocery delivery', 'amount': 20},
            {'description': 'Gas Station', 'amount': 30},
        ]
        search_string = 'GROCERY'
        expected_result = [
            {'description': 'Grocery Store', 'amount': 50},
            {'description': 'grocery delivery', 'amount': 20},
        ]
        self.assertEqual(filter_operations_by_description(operations, search_string), expected_result)

    def test_no_matches(self):
        # Проверка случая, когда совпадений нет
        operations = [
            {'description': 'Grocery Store', 'amount': 50},
            {'description': 'Gas Station', 'amount': 30},
        ]
        search_string = 'Restaurant'
        expected_result = []
        self.assertEqual(filter_operations_by_description(operations, search_string), expected_result)

    def test_empty_operations_list(self):
        # Проверка пустого списка операций
        operations = []
        search_string = 'Grocery'
        expected_result = []
        self.assertEqual(filter_operations_by_description(operations, search_string), expected_result)

    def test_empty_search_string(self):
        # Проверка пустой строки поиска
        operations = [
            {'description': 'Grocery Store', 'amount': 50},
            {'description': 'Gas Station', 'amount': 30},
        ]
        search_string = ''
        expected_result = [
            {'description': 'Grocery Store', 'amount': 50},
            {'description': 'Gas Station', 'amount': 30},
        ]
        self.assertEqual(filter_operations_by_description(operations, search_string), expected_result)

    def test_special_characters_in_search_string(self):
        # Проверка поиска с использованием специальных символов
        operations = [
            {'description': 'Grocery Store (Main)', 'amount': 50},
            {'description': 'Gas Station', 'amount': 30},
        ]
        search_string = '(Main)'
        expected_result = [{'description': 'Grocery Store (Main)', 'amount': 50}]
        self.assertEqual(filter_operations_by_description(operations, search_string), expected_result)

    def test_missing_description_field(self):
        # Проверка случая, когда у некоторых операций отсутствует поле 'description'
        operations = [
            {'description': 'Grocery Store', 'amount': 50},
            {'amount': 30},  # Нет поля 'description'
            {'description': 'Gas Station', 'amount': 25},
        ]
        search_string = 'Grocery'
        expected_result = [{'description': 'Grocery Store', 'amount': 50}]
        self.assertEqual(filter_operations_by_description(operations, search_string), expected_result)

if __name__ == '__main__':
    unittest.main()