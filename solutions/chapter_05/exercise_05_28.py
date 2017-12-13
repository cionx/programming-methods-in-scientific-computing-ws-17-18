from sympy import symbols, Matrix

class TimeOutError(Exception):
    pass

# expect f to be a matrix
def newton(f, var, x0):
    n = len(var)
    if n != len(f):
        raise ValueError("wrong function type")
    Df = Matrix(n, n, (lambda i,j: f[i].diff(var[j])))
    def g(x):
        sublist = list(zip(var, x))
        substitutor = (lambda e: e.subs( sublist ))
        return f.applyfunc( substitutor )
    def Dg(x):
        sublist = list(zip(var, x))
        substitutor = (lambda e: e.subs( sublist ))
        return Df.applyfunc( substitutor )
    n = 1
    xold = x0
    xnew = x0
    while n <= 100:
        D = Dg(xold)
        xnew = xold - D**(-1) @ g(xold)
        if (xnew - xold).norm() < 1e-6:
            return xnew
        xold = xnew
        n += 1
    raise TimeOutError("the calculation takes too long")



x, y, z = symbols('x y z')

f = Matrix([9*x**2 + 36*y**2 + 4*z**2 - 36, x**2 - 2*y**2 - 20*z, x**2 - y**2 + z**2])
x0 = [ Matrix([1,1,0]), Matrix([1,-1,0]), Matrix([-1,1,0]), Matrix([-1,-1,0]) ]
print("initial value \t\t\troot")
for i in range(4):
    print( "{} \t{}". format(x0[i], newton(f, [x,y,z], x0[i]).applyfunc(float)) )
