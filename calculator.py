from json import tool
from re import I


def add(x: float, y:float) -> float:
    return x+y

def divide(x: float, y:float) -> float:
    return x/y

def factorial(n):
    s = 1
    for i in range(1,n+1):
        s = s * i
    return s


def sin(x, N=20):
    s = 0
    for n in range(N+1):
       s += (-1)**n * x**(2*n+1)/factorial(2*n +1)

    return s

def sqrt(y: float, x0: float = 1, tol: float = 1e-12) -> float:
    
    while True:
        if abs(x0**2 - y) <= tol:
            break
        x0 = 1/2*(y/x0 + x0)
    return x0




