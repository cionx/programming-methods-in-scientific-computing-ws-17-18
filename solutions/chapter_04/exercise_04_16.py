from scipy import *
from scipy.linalg import *

class TimeOutError(Exception):
    pass

def newton(f, Df, x):
    n = 1
    xold = x
    xnew = x
    while n <= 100:
        D = Df(xold)
        xnew = xold - inv(D) @ f(xold)
        if norm(xnew - xold) <= 1e-6:
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
  A = zeros((3,3))
  A[0,0] = 18*x
  A[0,1] = 72*y
  A[0,2] = 8*z
  A[1,0] = 2*x
  A[1,1] = -2*y
  A[1,2] = -20
  A[2,0] = 2*x
  A[2,1] = -2*y
  A[2,2] = 2*z
  return A

x0 = (1,1,1)
print( "One root is {}.".format(newton(f, J, x0)) )
