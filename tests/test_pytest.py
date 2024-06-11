import pytest

from function1.func1 import sum_numbers


def sum_elements_of_list(*args):
    result = sum(*args)
    return result


#
@pytest.fixture
def numbers():
    list1 = [i for i in range(8) if i % 2 == 0]
    return list1


def test_sum_elements_of_list():
    assert sum_elements_of_list(numbers) == 12


def test_sum_numbers():
    assert sum_numbers(1, 2, 3) == 6


def test_sum_numbers_not_string():
    assert sum_numbers(-6, 5, 0.2) == -0.8
