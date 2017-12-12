from sympy import symbols, Matrix, simplify, limit, cos, sin

eps = symbols('eps')
A = Matrix([[1 + eps*cos(2/eps), -eps*sin(2/eps)],[-eps*sin(2/eps), 1 + eps*cos(2/eps)]])

e = A.eigenvects()
lambda1 = simplify(e[0][0])
lambda2 = simplify(e[1][0])
phi1 = simplify(e[0][2][0])
phi2 = simplify(e[1][2][0])

print("The eigenvalues are:")
print(lambda1)
print(lambda2)
print("The corresponding eigenvectors are:")
print(phi1)
print(phi2)

print("For eps -> 0 the matrix A becomes:")
print( A.applyfunc( (lambda x: limit(x, eps, 0) ) ) )
print("For eps -> 0 the eigenvalues become:")
print( limit(lambda1, eps, 0) )
print( limit(lambda2, eps, 0) )
