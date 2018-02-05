from sympy import *

eps = symbols('eps')
A = Matrix([[1 + eps*cos(2/eps), -eps*sin(2/eps)],[-eps*sin(2/eps), 1 + eps*cos(2/eps)]])

eig = A.eigenvects()
lambda1 = simplify(eig[0][0])  # first eigenvector
lambda2 = simplify(eig[1][0])  # second eigenvalue
phi1 = simplify(eig[0][2][0])  # first eigenvector
phi2 = simplify(eig[1][2][0])  # second eigenvector

print("The eigenvalues are:")
print(lambda1)
print(lambda2)
print("The corresponding eigenvectors are:")
print(phi1)
print(phi2)

print("For eps -> 0 the matrix A becomes:")
B = A.applyfunc( (lambda x: limit(x, eps, 0)) ) # apply limit entrywise
print( B ) 
print("For eps -> 0 the eigenvalues become:")
print( limit(lambda1, eps, 0) )
print( limit(lambda2, eps, 0) )
