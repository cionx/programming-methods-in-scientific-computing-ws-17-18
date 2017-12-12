from sympy import *

a, x = symbols('a x', real=True)
sol = solveset(x**3 + 3*x - a, x)
print(sol)

f = list(sol)[0]
plot(f, (a, -500, 500))
