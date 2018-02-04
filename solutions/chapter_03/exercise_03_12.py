# Exercise 3.12 (1)

class TimeOutError(Exception):
    pass

def newton(f, f_prime, x):
    eps = 1.E-7 # when to stop
    xold = x    # current position
    n = 1       # current iteration
    while n <= 100:
        d = f_prime(xold)
        if d == 0:
            raise ZeroDivisionError("derivative vanishes at {}".format(xold))
        xnew = xold - f(xold)/d
        if abs(xnew - xold) < eps:
            return xnew
        xold = xnew
        n += 1
    raise TimeOutError("the calculation takes too long")



f = (lambda x: x**2 - 2)
fprime = (lambda x: 2*x)
print("Calculating an approximation of sqrt(2):")
print( newton(f, fprime, 1) )

### OUTPUT:
#   Calculating an approximation of sqrt(2):
#   1.4142135623730951
