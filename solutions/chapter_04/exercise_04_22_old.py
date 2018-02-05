from scipy import *
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def f(x,y): return -abs(y)  # the differential equation
def bc(yl, yr): return abs(yl) + abs(yr+2) # boundary conditions

I = linspace(0, 4)  # interval for solving

y = zeros((1, len(I)))  # initial guess
y[0][0] = 1             # u(0) = 0

res = solve_bvp(f, bc, I, y)  #soling the ode

x = linspace(0, 4, 100)  # interval for plotting
u = res.sol(x)[0]        # yval of solution

# plotting solution
plt.clf()
plt.plot(x, u)
plt.grid()
plt.show()

# plotting solution with calculated function
plt.clf()
plt.plot(x, u, "b-", label="u") 
plt.plot(x, -2*exp(x-4), "r--", label="-2 e^{x-4}")
plt.grid()
plt.legend()
plt.show()
