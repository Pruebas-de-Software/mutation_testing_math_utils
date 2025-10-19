import pytest
from src.math_utils import is_prime, safe_div

def test_is_prime_basic():
    # Casos básicos y algunos típicos
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(9) is False
    assert is_prime(11) is True
    assert is_prime(25) is False
    assert is_prime(29) is True

def test_safe_div_ok():
    assert safe_div(10, 2) == 5
    assert safe_div(9, 2) == 4  # división entera
    assert safe_div(-9, 2) == -5

def test_safe_div_raises_on_zero():
    with pytest.raises(ValueError):
        safe_div(1, 0)
