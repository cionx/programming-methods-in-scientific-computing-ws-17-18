from sympy import *

x = symbols('x')
f = sympify("1/(1 + 25*x**2)")

def inner(f,g):
    return integrate(f*g,(x,-1,1))

# copied from chapter 5, exercise 32
# calculates the even legendre polynomials of degree <= n
def legendreeven(n):
    m = n//2 + 1  # number of polynomials to be computed
    p = [x**(2*i) for i in range(m)]  # to be orthogonalized
    normsq = []  # list of squares of norms
    for i in range(n//2 + 1):
        s = 0  # projection onto previous polynomials
        for j in range(i):
            s += inner(p[i], p[j])/normsq[j] * p[j]
        p[i] -= s
        normsq.append( inner(p[i], p[i]) )
    return p

# returns the first approximations of even degree <= n
def approx(n):
    L = legendreeven(n)
    approxlist = []
    p = 0   #current approximation
    for q in L:
        p += inner(f,q)/inner(q,q) * q
        approxlist.append(p)
    return approxlist



nlist = [5, 11, 17]
approxlist = approx(max(nlist))

# (a)
for n in nlist:
    plot(approxlist[n//2], (x, -1, 1))

# (b)
for n in nlist:
    plot(approxlist[n//2] - f, (x, -1, 1))
