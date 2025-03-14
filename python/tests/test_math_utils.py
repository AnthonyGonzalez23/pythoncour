import pytest
from games.math_utils import addition, soustraction, multiplication, division, puissance

def test_addition():
    assert addition(1, 2) == 3
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0

def test_soustraction():
    assert soustraction(5, 3) == 2
    assert soustraction(3, 5) == -2
    assert soustraction(0, 0) == 0

def test_multiplication():
    assert multiplication(2, 3) == 6
    assert multiplication(-2, 3) == -6
    assert multiplication(0, 5) == 0

def test_division():
    assert division(6, 3) == 2
    assert division(5, 2) == 2.5
    assert division(-6, 3) == -2

    # Test division by zero
    with pytest.raises(ValueError):
        division(5, 0)

def test_puissance():
    assert puissance(2, 3) == 8
    assert puissance(2, 0) == 1
    assert puissance(0, 5) == 0
    assert puissance(5, 1) == 5