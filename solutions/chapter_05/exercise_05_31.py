from sympy import *

x = symbols('x')

def inner(f, g):
    return integrate( f*g, (x, 0, 1) )

p = [ 1, x-sympify(1)/2, x**2 - x + sympify(1)/6 ]
B = Matrix( len(p), len(p), (lambda i,j: inner(p[i], p[j])) )
print(B)
