from sympy import *

a, x = symbols('a x', real=True)

sol = solveset(x**3 + 3*x - a, x)
(u,v,w) = list(sol)
u = simplify(u)
v = simplify(v)
w = simplify(w)
