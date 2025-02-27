# masks.py
from src.logger import setup_logger

# Настраиваем логгер для модуля masks
logger = setup_logger(__name__, "masks.log")


def mask_card_number(card_number):
    """
    Маскирует номер карты.
    """
    logger.info(f"Masking card number: {card_number}")
    try:
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.info(f"Card number masked successfully: {masked_number}")
        return masked_number
    except Exception as e:
        logger.error(f"Error masking card number: {e}")
        raise
