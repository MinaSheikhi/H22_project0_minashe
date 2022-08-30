from calculator import *
from math import pi

def test_add():
    assert add(1,2) == 3
    assert abs(add(0.1,0.2) - 0.3) < 1e-14

def test_divide():
    assert divide(16,2) == 8

def test_factorial():
    assert factorial(5) == 20
    assert factorial(1) == 1

def test_sin():
    assert sin(0) == 0
    assert abs(sin(pi/4) - 1/sqrt(2)) < 1e-14

def test_sqrt():
    assert sqrt(9) == 3

    
