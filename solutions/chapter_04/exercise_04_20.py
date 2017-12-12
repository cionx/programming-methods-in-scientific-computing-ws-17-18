from scipy import *
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def du(u, x): return x - u
xs = linspace(0,4,100)
u0 = 1.0
ys = odeint(du, u0, xs)

plt.clf()
plt.plot(xs, ys, "r", label="aprroximation")
plt.plot(xs, xs - 1 + 2*exp(-xs), "b--", label="exact")
plt.legend()
plt.show()
