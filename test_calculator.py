from calculator import *
from math import pi
import pytest

def test_add():
    assert add(1,2) == 3
    assert abs(add(0.1,0.2) - 0.3) < 1e-14

def test_divide():
    assert divide(16,2) == 8

def test_factorial():
    assert factorial(5) == 120
    assert factorial(1) == 1

def test_sin():
    assert sin(0) == 0
    assert abs(sin(pi/4) - 1/sqrt(2)) < 1e-14

def test_sqrt():
    assert sqrt(9) == 3

def test_is_float_raises_ValueError_for_string_arguments():
    with pytest.raises(ValueError): # for factorial(-1) raise a ValueError 
        factorial(-1)

def test_is_decimal_raises_TypeError_for_string_arguments():
    with pytest.raises(ZeroDivisionError): 
        divide(5, 0)
# Not needed to modify code for this test to pass


@pytest.mark.parametrize("x, y, output", [(1,2,3), (1,3,4), (2,3,5)])
def test_add_parametrized(x,y, output):
    assert abs(add(x,y) - output) < 1e-14

@pytest.mark.parametrize("x, y, output", [(10,5,2), (3,1,3), (4,4,1)])
def test_divide_parameterized(x, y, output):
    assert divide(x,y) == output
    

@pytest.mark.parametrize("arg, output", [(5,120), (3,6), (1,1)])
def test_factorial_parameterized(arg, output):
    assert factorial(arg) == output

@pytest.mark.parametrize("arg, output", [(0,0), (pi/4,1/sqrt(2)), (pi/2,1)])
def test_sin_parameterized(arg, output):
    assert abs(sin(arg) - output) < 1e-14  

@pytest.mark.parametrize("arg, output", [(1,1), (4,2), (16,4)])
def test_sqrt_parameterized(arg, output):
    assert abs(sqrt(arg) - output) < 1e-11  

