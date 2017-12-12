from scipy import *
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def f(y, x):
    (u, uprim) = y
    dy = (uprim, (3*x+2)/(3*x-1)*uprim + (6*x-8)/(3*x-1)*u)
    return dy

# initial value
u0 = (2, 3)
I = linspace(0,2, 100)

# solving and ploting
sol = odeint(f, u0, I)
plt.clf()
plt.plot(I, sol[:,0], color='b', label="u(x)")
plt.legend()
plt.xlabel('x')
plt.show()
