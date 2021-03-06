### newton method from exercise 3.12

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

### new Newton method

def prime(f, h=1e-6):
    return (lambda x: (f(x+h)-f(x))/h)

def newton_ext(f, x):
    fprime = prime(f)
    return newton(f, fprime, x)

# the following code does not execute when this file is imported
if __name__ == "__main__":

    from scipy import exp, linspace
    import matplotlib.pyplot as plt

    def f(x): return exp(x) + 2*x

    # plotting the function
    x = linspace(-1, 1, 100)
    plt.clf()
    plt.plot(x, f(x), color="b")
    plt.grid()
    plt.show()

    x0 = -0.25
    def fprime(x): return exp(x) + 2
    print("With the exact derivative we get a root at      {}.".format(newton(f, fprime, x0)))
    print("With an approximate derivative we get a root at {}.".format(newton_ext(f, x0)))
    
    ### OUTPUT:
    #   With the exact derivative we get a root at      -0.35173371124919584.
    #   With an approximate derivative we get a root at -0.35173371124919584.
