# logger.py
import logging
import os

# Создаем папку logs, если её нет
if not os.path.exists("logs"):
    os.makedirs("logs")


def setup_logger(name, log_file, level=logging.INFO):
    """
    Настраивает логгер для модуля.
    """
    # Создаем логгер
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Формат записи логов
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Обработчик для записи в файл (перезаписывает файл при каждом запуске)
    file_handler = logging.FileHandler(f"logs/{log_file}", mode="w")
    file_handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)
    return logger
