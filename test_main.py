import pytest
from main import add_numbers, subtract_numbers, multiply_numbers, divide_numbers


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(1000000, 2000000) == 3000000
    assert add_numbers(-5, -7) == -12
    assert add_numbers(0.1, 0.2) == pytest.approx(0.3)


def test_subtract_numbers():
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(10, 15) == -5
    assert subtract_numbers(0, 0) == 0
    assert subtract_numbers(100, 1) == 99
    assert subtract_numbers(-10, -5) == -5
    assert subtract_numbers(3.14, 1.14) == pytest.approx(2)


def test_multiply_numbers():
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(-4, 5) == -20
    assert multiply_numbers(0, 100) == 0
    assert multiply_numbers(1.5, 2) == pytest.approx(3)
    assert multiply_numbers(-2, -2) == 4
    assert multiply_numbers(0.1, 0.1) == pytest.approx(0.01)


def test_divide_numbers():
    assert divide_numbers(6, 2) == 3
    assert divide_numbers(10, 5) == 2
    assert divide_numbers(-15, 3) == -5
    assert divide_numbers(1, 3) == pytest.approx(0.3333333333)
    assert divide_numbers(0, 5) == 0
    assert divide_numbers(2.5, 0.5) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide_numbers(10, 0)
    with pytest.raises(ValueError):
        divide_numbers(-5, 0)
    with pytest.raises(ValueError):
        divide_numbers(0, 0)


def test_large_numbers():
    assert add_numbers(1e15, 1e15) == 2e15
    assert subtract_numbers(1e15, 1e14) == 9e14
    assert multiply_numbers(1e5, 1e5) == 1e10
    assert divide_numbers(1e10, 1e5) == 1e5


def test_small_numbers():
    assert add_numbers(1e-10, 2e-10) == pytest.approx(3e-10)
    assert subtract_numbers(5e-7, 3e-7) == pytest.approx(2e-7)
    assert multiply_numbers(2e-5, 3e-5) == pytest.approx(6e-10)
    assert divide_numbers(1e-5, 1e-2) == pytest.approx(1e-3)


def test_type_errors():
    with pytest.raises(TypeError):
        add_numbers("2", 3)
    with pytest.raises(TypeError):
        subtract_numbers(5, "3")
    with pytest.raises(TypeError):
        multiply_numbers([], 3)
    with pytest.raises(TypeError):
        divide_numbers(10, {})
