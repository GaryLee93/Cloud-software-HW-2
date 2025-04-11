from calculator import add, substract

def test_add():
    assert add(1, 3) == 4
    assert add(-1, 2) == 1

def test_substract():
    assert substract(2, 1) == 1
    assert substract(3, 2) == 1