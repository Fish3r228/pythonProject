import logging

# Настройка логгера
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def get_mask_account(acc_num: int) -> str:
    """Функция которая преобразует номер счета в строку"""
    logger.info(f"Вызов функции get_mask_account с аргументом: {acc_num}")
    account_str = str(acc_num)

    # Проверка что длина номера счета достаточна для маскировки
    if len(account_str) < 4:
        error_msg = "Номер счета должен содержать как минимум 4 цифры"
        logger.error(error_msg)
        raise ValueError(error_msg)

    # Маскировка номера счета
    masked_card_number = f"**{account_str[-4:]}"
    logger.info(f"Номер счета успешно замаскирован: {masked_card_number}")
    return masked_card_number


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая преобразует номер карты, маскируя часть цифр."""
    logger.info(f"Вызов функции get_mask_card_number с номером карты: {card_number}")

    if len(card_number) < 10:
        logger.warning(f"Номер карты слишком короткий: {card_number}")
        return card_number  # или можно выбросить исключение

    masked_number = f"{card_number[:6]}** **** {card_number[-4:]}"
    logger.info(f"Номер карты после маскировки: {masked_number}")

    return masked_number


# Пример использования
card_number = "1234567890123456"
masked_card_number = get_mask_card_number(card_number)
print(masked_card_number)