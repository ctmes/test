import pytest
from main import add_numbers, subtract_numbers, multiply_numbers, divide_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_subtract_numbers():
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(10, 15) == -5
    assert subtract_numbers(0, 0) == 0

def test_multiply_numbers():
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(-4, 5) == -20
    assert multiply_numbers(0, 100) == 0

def test_divide_numbers():
    assert divide_numbers(6, 2) == 3
    assert divide_numbers(10, 5) == 2
    assert divide_numbers(-15, 3) == -5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide_numbers(10, 0)
