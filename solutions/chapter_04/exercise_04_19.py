from scipy import *
from scipy.misc import factorial
from scipy.interpolate import KroghInterpolator

xarr = linspace(0,3,7)
f = [1,1,0,0,3,1,2]
p = KroghInterpolator(xarr, f)

# getting the coefficients

deriv = p.derivatives(0)
coeff = []
for n in range(len(deriv)):
    coeff.append(deriv[n]/factorial(n))

print("The coefficients (via interpolation) are {}:")
print(coeff)

# checking the results

from scipy.linalg import solve
A = zeros((7,7))
for i in range(len(xarr)):
    for j in range(len(f)):
        A[i,j] = xarr[i]**j

print("The coefficients (via linear equations) are {}:")
print(solve(A, f))
