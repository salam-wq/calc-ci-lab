"""Модульные тесты для calc.operations (pytest)."""

import pytest

from calc import add, divide, multiply, power, subtract
from calc.cli import main


@pytest.mark.parametrize(
    "a, b, expected",
    [(2, 3, 5), (-1, 1, 0), (0.5, 0.25, 0.75)],
)
def test_add(a, b, expected):
    assert add(a, b) == pytest.approx(expected)


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 7) == 21


def test_divide():
    assert divide(9, 3) == 3


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError, match="Деление на ноль"):
        divide(1, 0)


@pytest.mark.parametrize(
    "base, exponent, expected",
    [(2, 10, 1024), (5, 0, 1), (2, -2, 0.25)],
)
def test_power(base, exponent, expected):
    assert power(base, exponent) == pytest.approx(expected)


def test_power_rejects_non_integer_exponent():
    with pytest.raises(TypeError):
        power(2, 0.5)


def test_cli_add(capsys):
    assert main(["add", "2", "3"]) == 0
    assert capsys.readouterr().out.strip() == "5.0"


def test_cli_division_by_zero_returns_error_code(capsys):
    assert main(["div", "1", "0"]) == 1
    assert "Ошибка" in capsys.readouterr().err

def test_is_palindrome():
    from calc import is_palindrome

    assert is_palindrome("А роза упала на лапу Азора")
    assert not is_palindrome("Привет")


def test_is_palindrome_invalid_input():
    from calc import is_palindrome

    with pytest.raises(TypeError):
        is_palindrome(123)
