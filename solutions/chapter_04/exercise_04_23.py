# the given code

from scipy import *
n = 51
x = linspace(0,1,n)
y = linspace(0,1,n)
L = zeros((n,n))
L[0,:] = y*(y-1)

iter = 70
for _ in range(iter):
    for i in range(1,n-1):
        for j in range(1,n-1):
            Lt = L
            L[i,j] = (Lt[i+1,j] + Lt[i-1,j] + Lt[i,j+1] + Lt[i,j-1]) / 4



# own code

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')
x, y = meshgrid(x, y)
surf = ax.plot_surface(x, y, L, rstride=1, cstride=1, cmap=cm.jet, linewidth=0)
plt.show()

# exact solution

from poissonsolver import *
f = (lambda x,y: 0)
def g(x,y):
    if x == 0:
        return y*(y-1)
    return 0
poisson_solver(f, g, 51)
