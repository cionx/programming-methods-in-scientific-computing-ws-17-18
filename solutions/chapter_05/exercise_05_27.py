from sympy import symbols, exp, cosh, lambdify

class TimeOutError(Exception):
    pass

def newton(f, var, x0): # var = variable name
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
x0 = 1
print("The root of e^x + 2x is {}.".format(newton(f, x, 1)))
x1 = 0.5
x2 = 2
print("The functions cosh(x) and 2x intersect at {} and {}.".format(newton(g, x, x1), newton(g, x, x2)))
