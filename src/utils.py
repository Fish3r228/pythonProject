import json
import logging
import os

# Настройка логгера
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def load_transactions(file_path: str) -> list:
    """
    Загружает данные о транзакциях из JSON-файла.
    """
    logger.info(f"Попытка загрузить данные из файла: {file_path}")

    # Проверка существования файла
    if not os.path.exists(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            logger.info(f"Данные успешно загружены из файла: {file_path}")

            # Проверка, что данные являются списком
            if isinstance(data, list):
                logger.info(f"Загружено {len(data)} транзакций")
                return data
            else:
                logger.warning(f"Данные в файле {file_path} не являются списком")
                return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {file_path}")
        return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Неизвестная ошибка при загрузке файла {file_path}: {e}")
        return []


# Пример использования
file_path = "transactions.json"
transactions = load_transactions(file_path)
print(transactions)