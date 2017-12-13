from scipy import *
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def du(u, x): return x - u
x = linspace(0,4,100)
u0 = 1.0
y = odeint(du, u0, x)

plt.clf()
plt.plot(x, y, "r", label="aprroximation")
plt.plot(x, x - 1 + 2*exp(-x), "b--", label="exact")
plt.legend()
plt.show()
