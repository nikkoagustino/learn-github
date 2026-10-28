import pytest

from math_utils import add, divide, multiply, subtract


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-4, -6) == -10


def test_add_with_zero():
    assert add(0, 7) == 7


def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2


def test_subtract_negative_result():
    assert subtract(3, 5) == -2


def test_subtract_with_zero():
    assert subtract(10, 0) == 10


def test_multiply_positive_numbers():
    assert multiply(4, 5) == 20


def test_multiply_by_zero():
    assert multiply(9, 0) == 0


def test_multiply_negative_numbers():
    assert multiply(-3, 4) == -12


def test_divide_exact_result():
    assert divide(10, 2) == 5


def test_divide_fractional_result():
    assert divide(7, 2) == 3.5


def test_divide_negative_numbers():
    assert divide(-9, 3) == -3


def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError):
        divide(5, 0)
