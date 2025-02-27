import os

import pytest

from src import decorators


# Функции для тестирования
@decorators.log()
def add(a, b):
    return a + b


@decorators.log(filename="test_log.txt")
def divide(a, b):
    return a / b


# Тесты
def test_log_to_console(capsys):
    # Проверяем вывод в консоль
    result = add(2, 3)
    captured = capsys.readouterr()

    assert result == 5
    assert "Function 'add' started" in captured.out
    assert "Function 'add' finished successfully" in captured.out
    assert "result: 5" in captured.out


def test_log_to_file():
    # Удаляем старый файл, если он существует
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    # Проверяем запись в файл
    result = divide(10, 2)
    assert result == 5.0

    # Читаем файл и проверяем логи
    with open("test_log.txt", "r") as f:
        log_content = f.read()

    assert "Function 'divide' started" in log_content
    assert "Function 'divide' finished successfully" in log_content
    assert "result: 5.0" in log_content


def test_log_exception(capsys):
    # Проверяем, что исключение логируется в консоль
    with pytest.raises(ZeroDivisionError):
        decorators.divide(10, 0)

    captured = capsys.readouterr()

    assert "Function 'divide' raised an error" in captured.out
    assert "ZeroDivisionError" in captured.out
    assert "division by zero" in captured.out


def test_log_exception_to_file():
    # Удаляем старый файл, если он существует
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    # Проверяем, что исключение логируется в файл
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    # Читаем файл и проверяем логи
    with open("test_log.txt", "r") as f:
        log_content = f.read()

    assert "Function 'divide' raised an error" in log_content
    assert "ZeroDivisionError" in log_content
    assert "division by zero" in log_content
