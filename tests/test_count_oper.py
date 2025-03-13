import unittest

from src.filter_operations_by_description import filter_operations_by_description


class TestFilterOperationsByDescription(unittest.TestCase):
    def test_empty_operations(self):
        # Тест с пустым списком операций
        operations = []
        search_string = "магазин"
        result = filter_operations_by_description(operations, search_string)
        expected = []
        self.assertEqual(result, expected)

    def test_no_matching_operations(self):
        # Тест, где в операциях нет совпадений с искомой строкой
        operations = [
            {'description': 'Оплата за телефон'},
            {'description': 'Покупка билетов'},
        ]
        search_string = "магазин"
        result = filter_operations_by_description(operations, search_string)
        expected = []
        self.assertEqual(result, expected)

    def test_matching_operations(self):
        # Тест, где в операциях есть совпадения с искомой строкой
        operations = [
            {'description': 'Покупка в магазине'},
            {'description': 'Оплата за интернет'},
            {'description': 'Перевод другу'},
        ]
        search_string = "магазин"
        result = filter_operations_by_description(operations, search_string)
        expected = [{'description': 'Покупка в магазине'}]
        self.assertEqual(result, expected)

    def test_partial_match(self):
        # Тест на частичное совпадение
        operations = [
            {'description': 'Покупка в магазине электроники'},
            {'description': 'Оплата за интернет'},
            {'description': 'Перевод другу'},
        ]
        search_string = "магазин"
        result = filter_operations_by_description(operations, search_string)
        expected = [{'description': 'Покупка в магазине электроники'}]
        self.assertEqual(result, expected)

    def test_missing_description_field(self):
        # Тест, где в некоторых операциях отсутствует поле 'description'
        operations = [
            {'description': 'Покупка в магазине'},
            {'amount': 100},  # Операция без поля 'description'
            {'description': 'Оплата за интернет'},
        ]
        search_string = "магазин"
        result = filter_operations_by_description(operations, search_string)
        expected = [{'description': 'Покупка в магазине'}]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()