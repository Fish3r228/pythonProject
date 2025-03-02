import unittest
from unittest.mock import Mock, patch

from external_api import convert_to_rub


class TestConvertToRub(unittest.TestCase):

    @patch("external_api.requests.get")  # Мокаем requests.get
    @patch("external_api.os.getenv")  # Мокаем os.getenv
    def test_convert_usd_to_rub(self, mock_getenv, mock_get):
        """
        Тестируем конвертацию из USD в RUB.
        """
        # Мокаем переменные окружения
        mock_getenv.return_value = "kxsl9Rogo3ZzpoEbZaNC4frMXI7soEcl"

        # Мокаем ответ от API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"rates": {"RUB": 75.0}}  # Предположим, что 1 USD = 75 RUB
        mock_get.return_value = mock_response

        # Вызываем функцию
        result = convert_to_rub(100, "USD")

        # Проверяем результат
        self.assertEqual(result, 7500.0)  # 100 USD * 75 RUB/USD = 7500 RUB

        # Проверяем, что requests.get был вызван с правильными аргументами
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/latest?base=USD",
            headers={"apikey": "kxsl9Rogo3ZzpoEbZaNC4frMXI7soEcl"},
        )

    @patch("external_api.requests.get")
    @patch("external_api.os.getenv")
    def test_convert_eur_to_rub(self, mock_getenv, mock_get):
        """
        Тестируем конвертацию из EUR в RUB.
        """
        # Мокаем переменные окружения
        mock_getenv.return_value = "kxsl9Rogo3ZzpoEbZaNC4frMXI7soEcl"

        # Мокаем ответ от API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"rates": {"RUB": 90.0}}  # Предположим, что 1 EUR = 90 RUB
        mock_get.return_value = mock_response

        # Вызываем функцию
        result = convert_to_rub(50, "EUR")

        # Проверяем результат
        self.assertEqual(result, 4500.0)  # 50 EUR * 90 RUB/EUR = 4500 RUB

        # Проверяем, что requests.get был вызван с правильными аргументами
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/latest?base=EUR",
            headers={"apikey": "kxsl9Rogo3ZzpoEbZaNC4frMXI7soEcl"},
        )

    @patch("external_api.requests.get")
    def test_convert_rub_to_rub(self, mock_get):
        """
        Тестируем конвертацию из RUB в RUB (без вызова API).
        """
        # Вызываем функцию для RUB
        result = convert_to_rub(100, "RUB")

        # Проверяем результат
        self.assertEqual(result, 100.0)  # 100 RUB остается 100 RUB
        mock_get.assert_not_called()  # Запрос к API не должен быть выполнен


if __name__ == "__main__":
    unittest.main()
