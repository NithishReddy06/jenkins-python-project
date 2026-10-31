import pytest
from app import add, multiply, subtract, divide

def test_add():
    assert add(10, 20) == 30

def test_multiply():
    assert multiply(5, 4) == 20

def test_subtract():
    assert subtract(20, 5) == 15

def test_divide():
    assert divide(20, 4) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
