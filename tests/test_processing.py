import pytest

from src.processing import filter_by_state, sort_by_date

# Пример данных для тестирования
TEST_DATA = [
    {"name": "Alice", "state": "active"},
    {"name": "Bob", "state": "inactive"},
    {"name": "Charlie", "state": "active"},
    {"name": "David", "state": "pending"},
]


# Тесты для функции filter_by_state
def test_filter_by_state_active():
    # Ожидаемый результат после фильтрации по статусу 'active'
    expected_result = [
        {"name": "Alice", "state": "active"},
        {"name": "Charlie", "state": "active"},
    ]

    # Вызов функции и проверка результата
    result = filter_by_state(TEST_DATA, "active")
    assert result == expected_result


def test_filter_by_state_empty_input():
    # Пустой список на входе
    date = []
    # Ожидаемый результат - пустой список
    expected_result = []
    # Вызов функции и проверка результата
    result = filter_by_state(date, "active")
    assert result == expected_result

    @pytest.mark.parametrize(
        "state, next_result",
        [
            (
                "active",
                [
                    {"name": "Alice", "state": "active"},
                    {"name": "Charlie", "state": "active"},
                ],
            ),
        ],
    )
    def test_filter_by_state(state, next_result):
        """
        Тестирование функции filter_by_state с различными значениями state.
        """
        _result = filter_by_state(TEST_DATA, state)
        assert _result == next_result


TEST_DATA_1 = [
    {"name": "Event 1", "date": "2023-10-01"},
    {"name": "Event 2", "date": "2023-09-15"},
    {"name": "Event 3", "date": "2023-12-25"},
    {"name": "Event 4", "date": "2023-01-01"},
]

# Результаты
EXPECTED_ASCENDING_1 = [
    {"name": "Event 4", "date": "2023-01-01"},
    {"name": "Event 2", "date": "2023-09-15"},
    {"name": "Event 1", "date": "2023-10-01"},
    {"name": "Event 3", "date": "2023-12-25"},
]

EXPECTED_DESCENDING_1 = [
    {"name": "Event 3", "date": "2023-12-25"},
    {"name": "Event 1", "date": "2023-10-01"},
    {"name": "Event 2", "date": "2023-09-15"},
    {"name": "Event 4", "date": "2023-01-01"},
]


# Тесты
def test_sort_by_date_ascending_1() -> None:
    """
    Тестирование сортировки по дате в порядке возрастания.
    """
    result = sort_by_date(TEST_DATA_1, reverse=False)
    assert result == EXPECTED_ASCENDING_1


def test_sort_by_date_descending_2() -> None:
    """
    Тестирование сортировки по дате в порядке убывания.
    """
    result = sort_by_date(TEST_DATA_1, reverse=True)
    assert result == EXPECTED_DESCENDING_1


# Тест для корректных данных
def test_sort_by_date_ascending_3() -> None:
    result = sort_by_date(TEST_DATA_1, reverse=False)
    assert result == EXPECTED_ASCENDING_1


# Тест для некорректных данных
def test_sort_by_date_invalid_format() -> None:
    """
    Тестирование обработки неверного формата даты.
    """
    data = [
        {"name": "Event 1", "date": "2023-10-01"},
        {"name": "Event 2", "date": "2023/09/15"},  # Неверный формат даты
    ]
    with pytest.raises(ValueError, match="Invalid date format: 2023/09/15. Expected format: YYYY-MM-DD"):
        sort_by_date(data)
