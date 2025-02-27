import logging

# Создаем логгер для модуля masks
logger_masks = logging.getLogger('masks')
logger_masks.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования

# Создаем логгер для модуля utils
logger_utils = logging.getLogger('utils')
logger_utils.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования

# Создаем обработчик для вывода логов в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Создаем форматтер для логов
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Привязываем форматтер к обработчику
console_handler.setFormatter(formatter)

# Добавляем обработчик к логгерам
logger_masks.addHandler(console_handler)
logger_utils.addHandler(console_handler)