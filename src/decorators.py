import datetime
import functools


def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Формируем строку с информацией о начале выполнения функции
            start_time = datetime.datetime.now()
            log_message = f"{start_time}: Function '{func.__name__}' started with args: {args}, kwargs: {kwargs}\n"

            # Логируем начало выполнения функции
            if filename:
                with open(filename, "a") as f:
                    f.write(log_message)
            else:
                print(log_message, end="")

            try:
                # Выполняем функцию и логируем результат
                result = func(*args, **kwargs)
                end_time = datetime.datetime.now()
                success_message = (
                    f"{end_time}: Function '{func.__name__}' finished successfully with result: {result}\n"
                )

                if filename:
                    with open(filename, "a") as f:
                        f.write(success_message)
                else:
                    print(success_message, end="")

                return result

            except Exception as e:
                # Логируем ошибку, если она возникла
                error_time = datetime.datetime.now()
                error_message = (
                    f"{error_time}: Function '{func.__name__}' raised an error: {type(e).__name__} "
                    f"with args: {args}, kwargs: {kwargs}. Error message: {str(e)}\n"
                )

                if filename:
                    with open(filename, "a") as f:
                        f.write(error_message)
                else:
                    print(error_message, end="")

                # Пробрасываем исключение дальше
                raise

        return wrapper

    return decorator


# Пример использования декоратора
@log(filename="function_log.txt")
def add(a, b):
    return a + b


@log()
def divide(a, b):
    return a / b


if __name__ == "__main__":
    # Тестируем функции
    add(2, 3)
    divide(10, 2)
    divide(10, 0)  # Это вызовет ошибку
