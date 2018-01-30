from sympy import *

x = symbols('x');

xval = [1,2,3];
yval = [1,4,3];
deg = 3

A = Matrix(3, deg+1, (lambda i,j : xval[i]**j))
result = Matrix(yval);
coeff_all = A.gauss_jordan_solve(result)
coeff = coeff_all[0]
for var in list(coeff_all[1]):
    coeff = coeff.subs(var, 0)

p = 0
for i in range(deg+1):
    p += coeff[i]*x**i

print(p)

#   tries to interpolate the given points by a polynomial of degree d
#   only works because we have less pants then the degree
