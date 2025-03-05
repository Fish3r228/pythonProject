import pandas as pd


def read_transactions_from_csv(file_path):
    """
    Считывает финансовые операции из CSV-файла.

    :param file_path: Путь к CSV-файлу.
    :return: Список словарей с транзакциями.
    """
    try:
        # Считываем данные из CSV-файла
        df = pd.read_csv(file_path)
        # Преобразуем DataFrame в список словарей
        transactions = df.to_dict(orient='records')
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        return []


def read_transactions_from_excel(file_path):
    """
    Считывает финансовые операции из Excel-файла.
    """
    try:
        # Считываем данные из Excel-файла
        df = pd.read_excel(file_path)
        # Преобразуем DataFrame в список словарей
        transactions = df.to_dict(orient='records')
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении Excel-файла: {e}")
        return []


# Пример CSV-файла
csv_file_path = "/Users/anastasianasedkina/PycharmProjects/PythonProject2/data/transactions.csv"
csv_transactions = read_transactions_from_csv(csv_file_path)
print("Транзакции из CSV:", csv_transactions)

# Пример Excel-файла
excel_file_path = "/Users/anastasianasedkina/PycharmProjects/PythonProject2/data/transactions_excel.xlsx"
excel_transactions = read_transactions_from_excel(excel_file_path)
print("Транзакции из Excel:", excel_transactions)