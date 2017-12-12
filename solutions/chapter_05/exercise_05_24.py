from sympy import *

alpha, beta, x, y, z = symbols('alpha beta x y z')

A = Matrix([[1,1,1],[1,0,-1],[alpha,-1,1]])
b = Matrix([3,beta,-3])

print( solveset(det(A)) )

v,w = A.subs(alpha,-3).columnspace()
B = v.col_insert(1, w).col_insert(2, b)

print( solveset(det(B)) )

print( linsolve( [Eq(x+y+z,3), Eq(x-z,0), Eq(-3*x-y+z,-3) ], [x,y,z] ) )
