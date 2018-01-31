from scipy import *
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def fun(x,y): return [y[1], -abs(y[0])] # differential equation
def bc(yl, yr): return [yl[0], yr[0]+2]   # boundary condition

x = linspace(0,4,2);

y_1 = zeros((2, len(x))) # first inital guess u'(0) = 1
y_1[1][0] = 1
y_2 = zeros((2, len(x))) # second initial guess u'(0) = -1
y_2[1][0] = -1

res_1 = solve_bvp(fun, bc, x, y_1)  # solve with first guess
res_2 = solve_bvp(fun, bc, x, y_2)  # solve with second guess

x = linspace(0, 4, 100)
u_1 = res_1.sol(x)[0]
u_2 = res_2.sol(x)[0]

plt.plot(x, u_1, label='u_1')
plt.plot(x, u_2, label='u_2')
plt.legend()
plt.show()
