from scipy import cosh, linspace
import matplotlib.pyplot as plt

# (a)

# plot the graphs of cosh(x) and 2x
x = linspace(-1, 3, 100)
plt.clf()
plt.plot(x, cosh(x), color="k", label="cosh(x)")
plt.plot(x, 2*x, color="b", label="2x")
plt.grid()
plt.legend()
plt.show()

from exercise_04_14 import prime, newton_ext

def f(x): return cosh(x) - 2*x
x1 = 0.5 # starting value for left intersection
x2 = 2   # starting value for right intersection
print( "The intersections are at {} and {}.".format(newton_ext(f, x1), newton_ext(f, x2)) )

# (b)

fprime = prime(f)
print("The newton method cannot start at {}.".format(newton_ext(fprime, 1)))
