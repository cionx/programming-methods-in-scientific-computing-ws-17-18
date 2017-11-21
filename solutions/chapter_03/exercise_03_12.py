# Exercise 3.12 (1)

class TimeOutError(Exception):
    pass

def newton(f, f_prime, x):
    n = 1
    xold = x
    xnew = x
    while n <= 100:
        d = f_prime(xold)
        if d == 0:
            raise ZeroDivisionError("derivative vanishes at {}".format(xold))
        xnew = xold - f(xold)/d
        if 0 <= xnew - xold <= 1.E-7 or 0 <= xold - xnew <= 1.E-7:
            return xnew
        xold = xnew
        n += 1
    raise TimeOutError("the calculation takes too long")



### Exercise 3.12 (2)
#
#   >>> f = (lambda x: x**2 - 2)
#   >>> fprime = (lambda x: 2*x)
#   >>> print( newton(f, fprime, 1) )
#   1.4142135623730951
#
#   Die ersten 15 Nachkommastellen stimmen mit dem exakten Ergebnis überein.
#
###
