from scipy import *
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def f(y, x):  # the ode
    (u, uprim) = y
    dy = (uprim, (3*x+2)/(3*x-1)*uprim + (6*x-8)/(3*x-1)*u)
    return dy
u0 = (2, 3) # initial values

# solving the ode on the interval [0,2]
xval = linspace(0, 2, 100)
sol = odeint(f, u0, xval)
yval = sol[:,0]

# plotting the solution
plt.clf()
plt.plot(xval, yval, color='b', label="u(x)")
plt.grid()
plt.legend()
plt.show()
