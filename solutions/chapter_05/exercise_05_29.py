from sympy import symbols, Function, Eq, dsolve, solve, simplify

u = Function('u')
x = symbols('x')

ode = Eq(u(x).diff(x) + u(x), x)
gen_sol = dsolve(ode, u(x))
expr = simplify(gen_sol.rhs)

print("The general solution is: {}".format(expr))

C1 = symbols('C1')
b = solve( Eq(expr.subs(x,0),1) )
expr2 = expr.subs(C1, b[0])

print("The initial value results in the solution: {}".format(expr2))
