from sympy import *

x = symbols('x')
f_expr = 1/(1 + 25*x**2)

def rungepolate(n):
    f = (lambda z: f_expr.subs('x',z))
    
    xval = [ -1 + i*sympify(2)/n for i in range(n+1) ]
    yval = [f(z) for z in xval]
    points = list(zip(xval,yval))
    poly = interpolate(points, x)  # sympy interpolate
    
    return poly



#   (a)
for n in [5, 11, 17]:
    p = rungepolate(n)
    plot(p, (x, -1, 1))



#   (b)
for n in [5, 11, 17]:
    p = rungepolate(n)
    plot(f_expr - p, (x, -1, 1))
