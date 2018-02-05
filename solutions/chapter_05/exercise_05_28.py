from sympy import *

class TimeOutError(Exception):
    pass

# f   : a matrix of expressions
# var : list of appearing variables
def newton(f, var, x0):
    n = len(var)
    if n != len(f):
        raise ValueError("wrong function type")
    Df = Matrix(n, n, (lambda i,j: f[i].diff(var[j])))
    def g(x):   # make f into a function
        sublist = list(zip(var, x))
        substitutor = (lambda e: e.subs( sublist ))
        return f.applyfunc( substitutor )
    def Dg(x):  # make Df into a function
        sublist = list(zip(var, x))
        substitutor = (lambda e: e.subs( sublist ))
        return Df.applyfunc( substitutor )
    eps = 1.E-7 # when to stop
    xold = x0   # current value
    n = 1       # current iteration
    while n <= 100:
        D = Dg(xold)
        xnew = xold - D**(-1) @ g(xold)
        if (xnew - xold).norm() < eps:
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

### OUTPUT
#   initial value                   root
#   Matrix([[1], [1], [0]])         Matrix([[0.893628234476483], [0.894527010390578], [-0.0400892861591528]])
#   Matrix([[1], [-1], [0]])        Matrix([[0.893628234476483], [-0.894527010390578], [-0.0400892861591528]])
#   Matrix([[-1], [1], [0]])        Matrix([[-0.893628234476483], [0.894527010390578], [-0.0400892861591528]])
#   Matrix([[-1], [-1], [0]])       Matrix([[-0.893628234476483], [-0.894527010390578], [-0.0400892861591528]])

