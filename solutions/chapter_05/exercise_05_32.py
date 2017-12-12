from sympy import symbols, Matrix, integrate

x = symbols('x')

def innerL2(f,g, var):
    return integrate( f*g, (var, -1, 1) )

def legendre(n):
    p = [x**i for i in range(n+1)]
    normsq = []
    for i in range(n+1):
        s = 0
        for j in range(i):
            s += innerL2(p[i], p[j], x)/normsq[j] * p[j]
        p[i] -= s
        normsq.append( innerL2(p[i], p[i], x) )
    return p

p = legendre(6)
print( Matrix(6, 6, (lambda i,j: innerL2(p[i], p[j], x))) )
