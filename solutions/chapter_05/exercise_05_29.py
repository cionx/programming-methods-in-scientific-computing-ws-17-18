from sympy import *

u = Function('u')
x = symbols('x')

ode = Eq(u(x).diff(x) + u(x), x)
gen_sol = dsolve(ode, u(x))
expr = simplify(gen_sol.rhs)
print("The general solution is: {}".format(expr))

### OUTPUT:
#   The general solution is: C1*exp(-x) + x - 1

C1 = symbols('C1')  # constant appearing the general solution
b = solve( Eq(expr.subs(x,0),1) )
expr2 = expr.subs(C1, b[0])
print("The initial value results in the solution: {}".format(expr2))

### OUTPUT:
#   The initial value results in the solution: x - 1 + 2*exp(-x)
