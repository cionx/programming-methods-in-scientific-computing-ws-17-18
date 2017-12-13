from sympy import symbols, Eq, Matrix, solveset, linsolve, det

alpha, beta, x, y, z = symbols('alpha beta x y z')

A = Matrix([[1,1,1],[1,0,-1],[alpha,-1,1]])
b = Matrix([3,beta,-3])
print( "The kernel is nonzero for the following values of alpha:" )
print( solveset(det(A)) )

v,w = A.subs(alpha,-3).columnspace()    # column space is 2-dimensional
B = v.col_insert(1, w).col_insert(2, b)
print("For alpha = -3 there exists a solution for the following values of beta:") 
print( solveset(det(B)) )

print("For alpha = -3, beta = 0 the solutions are given as follows:")
print( linsolve( [Eq(x+y+z,3), Eq(x-z,0), Eq(-3*x-y+z,-3) ], [x,y,z] ) )
