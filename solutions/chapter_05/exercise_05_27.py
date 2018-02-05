from sympy import *

class TimeOutError(Exception):
    pass

def newton(f, var, x0): # var = variable name
    fprime  = f.diff(var)
    g = lambdify(var, f)
    gprime = lambdify(var, fprime)
    eps = 1.E-7 # when to stop
    xold = x0   # current value
    n = 1       # current iteration
    while n <= 100:
        d = gprime(xold)
        if d == 0:
            raise ZeroDivisionError("derivative vanishes at {}".format(xold))
        xnew = xold - g(xold)/d
        if abs(xnew - xold) < eps:
            return xnew
        xold = xnew
        n += 1
    raise TimeOutError("the calculation takes too long")


x = symbols('x')
f = exp(x) + 2*x
g = cosh(x) - 2*x

x0 = 1
print("The root of e^x + 2x is {}.".format(newton(f, x, 1)))

### OUTPUT:
#   The root of e^x + 2x is -0.3517337112491958.


x1 = 0.5
x2 = 2
print("The functions cosh(x) and 2x intersect at {} and {}.".format(newton(g, x, x1), newton(g, x, x2)))

### OUTPUT
#   The functions cosh(x) and 2x intersect at 0.5893877634693505 and 2.1267998926782568.
