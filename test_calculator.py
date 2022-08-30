from calculator import *

def test_add():
    assert add(1,2) == 3
    assert abs(add(0.1,0.2) - 0.3) < 1e-14
