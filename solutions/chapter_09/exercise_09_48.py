from sympy import *

x = symbols('x')
f_expr = 1/(1 + 25*x**2)

def rungepolate(n):
    f = (lambda z: f_expr.subs('x',z))
    
    xval = [ -cos(i*pi/n).evalf() for i in range(n+1) ] # use float for speed
    yval = [f(z) for z in xval]
    pts = list(zip(xval,yval))
    poly = interpolate(pts, x)  # sympy interpolate
    
    return poly



#   (a)
for n in [5, 11, 17]:
    p = rungepolate(n)
    plot(p, (x, -1, 1))



#   (b)
for n in [5, 11, 17]:
    p = rungepolate(n)
    plot(f_expr - p, (x, -1, 1))
