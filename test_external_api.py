# test_external_api.py
import unittest
from unittest.mock import patch, Mock
from external_api import convert_to_rub

class TestConvertToRub(unittest.TestCase):
    @patch('external_api.requests.get')
    def test_convert_usd_to_rub(self, mock_get):
        """
        Тестируем конвертацию USD в RUB.
        """
        # Мокируем ответ API
        mock_response = Mock()
        mock_response.json.return_value = {
            "rates": {
                "RUB": 75.0
            }
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Транзакция в USD
        transaction = {"amount": 100, "currency": "USD"}
        result = convert_to_rub(transaction)

        # Проверяем результат
        self.assertEqual(result, 7500.0)

        # Проверяем, что запрос был выполнен с правильными параметрами
        expected_url = "https://api.apilayer.com/exchangerates_data/latest?base=USD&symbols=RUB"
        expected_headers = {"apikey": "kxsl9Rogo3ZzpoEbZaNC4frMXI7soEcl"}
        mock_get.assert_called_once_with(expected_url, headers=expected_headers)


    @patch('external_api.requests.get')
    def test_convert_eur_to_rub(self, mock_get):
        """
        Тестируем конвертацию EUR в RUB.
        """
        # Мокируем ответ API
        mock_response = Mock()
        mock_response.json.return_value = {
            "rates": {
                "RUB": 90.0
            }
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Транзакция в EUR
        transaction = {"amount": 50, "currency": "EUR"}
        result = convert_to_rub(transaction)

        # Проверяем результат
        self.assertEqual(result, 4500.0)

        # Проверяем, что запрос был выполнен с правильными параметрами
        expected_url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&symbols=RUB"
        expected_headers = {"apikey": "kxsl9Rogo3ZzpoEbZaNC4frMXI7soEcl"}
        mock_get.assert_called_once_with(expected_url, headers=expected_headers)

    def test_convert_rub_to_rub(self):
        """
        Тестируем конвертацию RUB в RUB.
        """
        # Транзакция в RUB
        transaction = {"amount": 5000, "currency": "RUB"}
        result = convert_to_rub(transaction)

        # Проверяем результат
        self.assertEqual(result, 5000.0)


    def test_invalid_transaction(self):
        """
        Тестируем обработку некорректной транзакции.
        """
        # Транзакция без ключа 'currency'
        transaction = {"amount": 100}

        # Проверяем, что исключение выбрасывается
        with self.assertRaises(ValueError):
            convert_to_rub(transaction)

if __name__ == '__main__':
    unittest.main()