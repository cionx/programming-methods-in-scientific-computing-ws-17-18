from sympy import symbols, Matrix, integrate

x = symbols('x')

def inner(f,g):
    return integrate( f*g, (x, -1, 1) )

def legendre(n):
    p = [x**i for i in range(n+1)]
    normsq = [] # list of squared norms
    for i in range(n+1):
        s = 0
        for j in range(i):
            s += inner(p[i], p[j])/normsq[j] * p[j]
        p[i] -= s
        normsq.append( inner(p[i], p[i]) )
    return p

p = legendre(6)
print( Matrix(6, 6, (lambda i,j: inner(p[i], p[j]))) )
