from sympy import *

u = Function('u')
x = symbols('x')

ode = Eq(u(x).diff(x) + u(x), x)
gen_sol = dsolve(ode, u(x))
expr = simplify(gen_sol.rhs)

C1 = symbols('C1')
b = solve( Eq(expr.subs(x,0),1) )
expr.subs(C1, b)
