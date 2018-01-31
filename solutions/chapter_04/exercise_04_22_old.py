from scipy import *
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def f(x,y): return -abs(y)
def bc(yl, yr): return abs(yl) + abs(yr+2)

I = linspace(0, 4)

y = zeros((1, len(I)))
y[0][0] = 1

res = solve_bvp(f, bc, I, y)

x = linspace(0, 4, 100)
u = res.sol(x)[0]

plt.clf()
plt.plot(x, u)
plt.grid()
plt.show()

plt.clf()
plt.plot(x, u, "b-", label="u") 
plt.plot(x, -2*exp(x-4), "r--", label="-2 e^{x-4}")
plt.grid()
plt.legend()
plt.show()
