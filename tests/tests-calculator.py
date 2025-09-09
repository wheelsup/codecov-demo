# tests/test_calculator.py
import calculator  # this imports your calculator.py file

def test_add():
    assert calculator.add(2, 3) == 5

def test_subtract():
    assert calculator.subtract(5, 3) == 2

def test_multiply():
    assert calculator.multiply(4, 3) == 12

def test_divide():
    assert calculator.divide(10, 2) == 5

def test_divide_by_zero():
    try:
        calculator.divide(5, 0)
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        assert True
