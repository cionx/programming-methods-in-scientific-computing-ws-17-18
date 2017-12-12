from sympy import *

u = Function('u')
x = symbols('x')

ode = Eq(u(x).diff(x,x), u(x))
gen_sol = dsolve(ode, u(x))
expr = simplify(gen_sol.rhs)

C1, C2 = symbols('C1 C2')
b = solve( [Eq(expr.subs(x,0),0), Eq(expr.diff(x).subs(x,1),-1)], [C1, C2] )
sol = sumplify(simplify(expr.subs(b))) # simplify not idempotent?
