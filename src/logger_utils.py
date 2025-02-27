# utils.py
from src.logger import setup_logger

# Настраиваем логгер для модуля utils
logger = setup_logger(__name__, "utils.log")


def validate_input(data):
    """
    Проверяет входные данные.
    :param data: Входные данные.
    :return: True, если данные валидны, иначе False.
    """
    logger.info(f"Validating input: {data}")
    try:
        if not data:
            logger.warning("Input data is empty")
            return False
        logger.info("Input data is valid")
        return True
    except Exception as e:
        logger.error(f"Error validating input: {e}")
        raise
