import unittest
from unittest.mock import patch
from external_api import convert_to_rub

class TestConvertToRub(unittest.TestCase):

    @patch('external_api.requests.get')
    def test_convert_eur_to_rub(self, mock_get):
        # Мок ответа API
        mock_get.return_value.json.return_value = {
            'rates': {'EUR': 0.85, 'RUB': 75.0}
        }
        mock_get.return_value.raise_for_status.return_value = None

        result = convert_to_rub(100, 'EUR')
        self.assertAlmostEqual(result, 8823.53, delta=0.01)

    @patch('external_api.requests.get')
    def test_convert_usd_to_rub(self, mock_get):
        # Мок ответа API
        mock_get.return_value.json.return_value = {
            'rates': {'USD': 1.0, 'RUB': 75.0}
        }
        mock_get.return_value.raise_for_status.return_value = None

        result = convert_to_rub(100, 'USD')
        self.assertAlmostEqual(result, 7500.0, delta=0.01)

    def test_convert_rub_to_rub(self):
        result = convert_to_rub(100, 'RUB')
        self.assertEqual(result, 100.0)

    @patch('external_api.requests.get')
    def test_invalid_transaction(self, mock_get):
        # Мок ответа API с ошибкой
        mock_get.return_value.json.return_value = {
            'rates': {'USD': 1.0, 'RUB': 75.0}
        }
        mock_get.return_value.raise_for_status.return_value = None

        result = convert_to_rub(100, 'INVALID')
        self.assertEqual(result, 0.0)

if __name__ == '__main__':
    unittest.main()