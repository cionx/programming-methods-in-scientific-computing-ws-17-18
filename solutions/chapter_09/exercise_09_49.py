from sympy import *

x = symbols('x')
f = sympify("1/(1 + 25*x**2)")

def inner(f,g):
    return integrate(f*g,(x,-1,1))

# copied from chapter 5, exercise 32
# calculates the first n legendre polynomials of even degree
def legendre(n):
    p = [x**(2*i) for i in range(n)] # to be orthogonalized
    normsq = [] # list of squares of norms
    for i in range(n):
        s = 0   # projection onto previous polynomials
        for j in range(i):
            s += inner(p[i], p[j])/normsq[j] * p[j]
        p[i] -= s
        normsq.append( inner(p[i], p[i]) )
    return p

# returns the first n approximations
def approx(n):
    L = legendre(n)
    approxlist = []
    p = 0   #current approximation
    for q in L:
        p += inner(f,q)/inner(q,q) * q
        approxlist.append(p)
    return approxlist



n = 20 # number of approximations
approxlist = approx(n)

# (a)
for i in [5, 11, 17]:
    plot(approxlist[i], (x, -1, 1))

# (b)
for p in [5, 11, 17]:
    plot(approxlist[i] - f, (x, -1, 1))
