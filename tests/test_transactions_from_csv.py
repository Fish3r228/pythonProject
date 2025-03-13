import unittest
from unittest.mock import patch

import pandas as pd

from transactions.finance_utils import read_transactions_from_csv  # Замените `your_module` на имя вашего модуля


class TestReadTransactionsFromCSV(unittest.TestCase):
    @patch("pandas.read_csv")
    def test_read_transactions_from_csv(self, mock_read_csv):
        # Подготавливаем тестовые данные
        test_data = pd.DataFrame({
            "ID": [1, 2],
            "Date": ["2023-10-01", "2023-10-02"],
            "Amount": [500, 1500],
            "Description": ["Groceries", "Electronics"]
        })
        mock_read_csv.return_value = test_data

        # Вызываем тестируемую функцию
        result = read_transactions_from_csv("dummy_path.csv")

        # Проверяем, что функция вернула ожидаемый результат
        expected_result = [
            {"ID": 1, "Date": "2023-10-01", "Amount": 500, "Description": "Groceries"},
            {"ID": 2, "Date": "2023-10-02", "Amount": 1500, "Description": "Electronics"}
        ]
        self.assertEqual(result, expected_result)

        # Проверяем, что `pandas.read_csv` был вызван с правильным аргументом
        mock_read_csv.assert_called_once_with("dummy_path.csv")


if __name__ == "__main__":
    unittest.main()