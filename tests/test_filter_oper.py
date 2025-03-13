import unittest

from src.count_operations_by_category import count_operations_by_category


class TestCountOperationsByCategory(unittest.TestCase):
    def test_empty_operations(self):
        # Тест с пустым списком операций
        operations = []
        categories = ['магазин', 'интернет', 'перевод']
        result = count_operations_by_category(operations, categories)
        expected = {'магазин': 0, 'интернет': 0, 'перевод': 0}
        self.assertEqual(result, expected)

    def test_no_matching_categories(self):
        # Тест, где в операциях нет совпадений с категориями
        operations = [
            {'description': 'Оплата за телефон'},
            {'description': 'Покупка билетов'},
        ]
        categories = ['магазин', 'интернет', 'перевод']
        result = count_operations_by_category(operations, categories)
        expected = {'магазин': 0, 'интернет': 0, 'перевод': 0}
        self.assertEqual(result, expected)

    def test_single_category_match(self):
        # Тест, где есть совпадения только по одной категории
        operations = [
            {'description': 'Покупка в магазине'},
            {'description': 'Оплата за интернет'},
            {'description': 'Перевод другу'},
        ]
        categories = ['магазин', 'интернет', 'перевод']
        result = count_operations_by_category(operations, categories)
        expected = {'магазин': 1, 'интернет': 1, 'перевод': 1}
        self.assertEqual(result, expected)

    def test_multiple_category_matches(self):
        # Тест, где есть совпадения по нескольким категориям
        operations = [
            {'description': 'Покупка в магазине'},
            {'description': 'Оплата за интернет'},
            {'description': 'Перевод другу'},
            {'description': 'Покупка в магазине электроники'},
            {'description': 'Оплата за интернет и телевидение'},
        ]
        categories = ['магазин', 'интернет', 'перевод']
        result = count_operations_by_category(operations, categories)
        expected = {'магазин': 2, 'интернет': 2, 'перевод': 1}
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()