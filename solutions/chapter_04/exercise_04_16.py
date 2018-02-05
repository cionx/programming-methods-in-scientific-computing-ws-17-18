from scipy import *
from scipy.linalg import *

class TimeOutError(Exception):
    pass

def newton(f, Df, x):
    eps = 1.E-6 # when to stop
    xold = x    # current value
    n = 1       # current iteration
    while n <= 100:
        D = Df(xold)
        xnew = xold - inv(D) @ f(xold)
        if norm(xnew - xold) < eps:
            return xnew
        xold = xnew
        n += 1
    raise TimeOutError("the calculation takes too long")



def f(p):
  (x,y,z) = p
  xnew = 9*x**2 + 36*y**2 + 4*z**2 - 36
  ynew = x**2 - 2*y**2 - 20*z
  znew = x**2 - y**2 + z**2
  return (xnew, ynew, znew)

def J(p):
  (x,y,z) = p
  D = array([[18*x, 72*y, 8*z], [2*x,-4*y,-20],[2*x,-2*y,2*z]])
  return D

x0 = [(1,1,0), (1,-1,0), (-1,1,0), (-1,-1,0)]
print("initial value\troot")
for i in range(4):
    print( "{}\t{}.".format(x0[i], newton(f, J, x0[i])) )

### OUTPUT:
#   initial value   root
#   (1, 1, 0)       [ 0.89362823  0.89452701 -0.04008929].
#   (1, -1, 0)      [ 0.89362823 -0.89452701 -0.04008929].
#   (-1, 1, 0)      [-0.89362823  0.89452701 -0.04008929].
#   (-1, -1, 0)     [-0.89362823 -0.89452701 -0.04008929].
