from sympy import *

x = symbols('x')

def innerL2(f,g, var):
    return integrate( f*g, (var, 0, 1) )

p = [ 1, x-S(1)/2, x**2 - x + S(1)/6 ]
B = Matrix( len(p), len(p), (lambda i,j: innerL2(p[i], p[j], x) ) )
print(B == eye(len(p)))
