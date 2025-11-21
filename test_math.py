from math_func import add, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(6, 2) == 3
    import pytest
    with pytest.raises(ValueError):
        divide(5, 0)