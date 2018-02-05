from scipy import *
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def du(u, x): return x - u  # the ode
x = linspace(0,4,100)       # interval [0,4]
u0 = 1.0                    # left boundary condition
y = odeint(du, u0, x)       # solve ode

# plotting the graphs
plt.clf()
plt.plot(x, y, "r", label="aprroximation")
plt.plot(x, x - 1 + 2*exp(-x), "b--", label="exact")
plt.grid()
plt.legend()
plt.show()
