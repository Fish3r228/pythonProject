import json
import csv
import openpyxl
from datetime import datetime


def load_json(file_path):
    """
    Загружает данные из JSON-файла.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def load_csv(file_path):
    """
    Загружает данные из CSV-файла.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


def load_xlsx(file_path):
    """
    Загружает данные из XLSX-файла.
    """
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    rows = sheet.iter_rows(values_only=True)
    headers = next(rows)
    return [dict(zip(headers, row)) for row in rows]


def main():
    # Приветствие пользователя
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    # Получаем выбор пользователя
    choice = input("Ваш выбор: ")

    # Обработка выбора пользователя
    if choice == '1':
        file_path = 'data/transactions.json'
        transactions = load_json(file_path)
        print("Для обработки выбран JSON-файл.")
    elif choice == '2':
        file_path = 'data/transactions.csv'
        transactions = load_csv(file_path)
        print("Для обработки выбран CSV-файл.")
    elif choice == '3':
        file_path = 'data/transactions.xlsx'
        transactions = load_xlsx(file_path)
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор. Программа завершена.")
        return

    # Фильтрация по статусу
    available_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию.\n"
                       f"Доступные для фильтрации статусы: {', '.join(available_statuses)}\n").upper()
        if status in available_statuses:
            print(f"Операции отфильтрованы по статусу '{status}'")
            break
        else:
            print(f"Статус операции '{status}' недоступен.")

    # Фильтрация транзакций по статусу
    filtered_transactions = [t for t in transactions if t.get('status', '').upper() == status]

    # Сортировка по дате
    sort_by_date = input("Отсортировать операции по дате? (Да/Нет): ").lower()
    if sort_by_date == 'да':
        order = input("Отсортировать по возрастанию или по убыванию? (по возрастанию/по убыванию): ").lower()
        reverse = order == 'по убыванию'
        filtered_transactions.sort(key=lambda x: datetime.strptime(x.get('date', ''), '%Y-%m-%d'), reverse=reverse)

    # Фильтрация по рублевым транзакциям
    rub_only = input("Выводить только рублевые транзакции? (Да/Нет): ").lower()
    if rub_only == 'да':
        filtered_transactions = [t for t in filtered_transactions if t.get('currency', '').upper() == 'RUB']

    # Фильтрация по описанию
    filter_by_description = input("Отфильтровать список транзакций по определенному слову в описании? (Да/Нет): ").lower()
    if filter_by_description == 'да':
        search_word = input("Введите слово для поиска в описании: ").lower()
        filtered_transactions = [t for t in filtered_transactions if search_word in t.get('description', '').lower()]

    # Вывод итогового списка транзакций
    print("Распечатываю итоговый список транзакций...")
    if filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}\n")
        for transaction in filtered_transactions:
            date = transaction.get('date', '')
            description = transaction.get('description', '')
            from_account = transaction.get('from', '')
            to_account = transaction.get('to', '')
            amount = transaction.get('amount', '')
            currency = transaction.get('currency', '')

            print(f"{date} {description}")
            if from_account:
                print(f"{from_account} -> {to_account}")
            else:
                print(f"{to_account}")
            print(f"Сумма: {amount} {currency}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

# Запуск программы
if __name__ == "__main__":
    main()