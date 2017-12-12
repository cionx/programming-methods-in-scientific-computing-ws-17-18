from sympy import *

class TimeOutError(Exception):
    pass

def newton(f, var, x0):
    fprime  = f.diff(var)
    g = lambdify(var, f)
    gprime = lambdify(var, fprime)
    n = 1
    xold = x0
    xnew = x0
    while n <= 100:
        d = gprime(xold)
        if d == 0:
            raise ZeroDivisionError("derivative vanishes at {}".format(xold))
        xnew = xold - g(xold)/d
        if abs(xnew - xold) < 1.E-7:
            return xnew
        xold = xnew
        n += 1
    raise TimeOutError("the calculation takes too long")



x = symbols('x')
f = exp(x) + 2*x
g = cosh(x) - 2*x
newton(f, x, 2)
