from scipy import *
from scipy.misc import factorial
from scipy.interpolate import KroghInterpolator

# the interpolation itself

xarr = linspace(0,3,7)
f = [1,1,0,0,3,1,2]
p = KroghInterpolator(xarr, f)

# getting the coefficients

deriv = p.derivatives(0)
coeff = []
for n in range(len(deriv)):
    coeff.append(deriv[n]/factorial(n))

print("The coefficients (via interpolation):")
print(coeff)

### OUTPUT:
#   The coefficients (via interpolation):
#   [1.0, -13.66666666666666, 65.46666666666664, -110.66666666666664, 81.33333333333331, -26.66666666666666, 3.1999999999999993]

# comparing to a different approach

from scipy.linalg import solve
A = zeros((7,7))
for i in range(len(xarr)):
    for j in range(len(f)):
        A[i,j] = xarr[i]**j

print("The coefficients (via linear equations) are:")
print(solve(A, f))

### OUTPUT:
#   The coefficients (via linear equations) are:
#   [   1.          -13.66666667   65.46666667 -110.66666667   81.33333333
#   -26.66666667    3.2       ]


