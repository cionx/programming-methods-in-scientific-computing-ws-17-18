from scipy import *
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def f(x,y): return -abs(y)
def bc(yl, yr): return abs(yl) + abs(yr+2)

I = linspace(0, 4)

y_1 = zeros((1, len(I)))
y_1[0][0] = 1
#y_2 = zeros((1, len(I)))
#y_2[0][1] = -1

res_1 = solve_bvp(f, bc, I, y_1)
#res_2 = solve_bvp(f, bc, I, y_2)

x = linspace(0, 4, 100)
u_1 = res_1.sol(x)[0]
#u_2 = res_2.sol(x)[0]

plt.clf()
plt.plot(x, u_1, label="u_1")
#plt.plot(x, u_2, label="u_2")
plt.plot(x, -0.037*exp(x), label="exp")
plt.legend()
plt.show()
