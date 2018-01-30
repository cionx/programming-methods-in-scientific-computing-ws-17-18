from sympy import *

x = symbols('x')
f = sympify("1/(1 + 25*x**2)")

def inner(f,g):
    return integrate(f*g,(x,-1,1))

# copied from chapter 5, exercise 32
# calculates the first n legendre polynomials of even degree
def legendre(n):
    p = [x**(2*i) for i in range(n)]
    normsq = []
    for i in range(n):
        s = 0
        for j in range(i):
            s += inner(p[i], p[j])/normsq[j] * p[j]
        p[i] -= s
        normsq.append( inner(p[i], p[i]) )
    return p

# returns the first n approximations
def approx(n):
    L = legendre(n)
    aps = []
    s = 0
    for p in L:
        s += inner(f,p)/inner(p,p) * p
        aps.append(s)
    return aps



n = 10 # number of approximations
approxlist = approx(n)

# (a)
for p in approxlist:
    plot(p, (x, -1, 1))

# (b)
for p in approxlist:
    plot(p - f, (x, -1, 1))
