from matrices import *

A = Matrix(3, 2, [[0,1],[1,0],[1,1]])
print("A:")
print(A)

#   OUTPUT:
#   A:
#   [0 1]
#   [1 0]
#   [1 1]

B = Matrix(2, 4, [[1,2,3,4],[5,6,7,8]])
print("B:")
print(B)

#   OUTPUT:
#   B:
#   [1 2 3 4]
#   [5 6 7 8]

C = Matrix(4, 2, [[1,0],[0,1],[1,0],[0,1]])
print("C:")
print(C)

#   OUTPUT:
#   C:
#   [1 0]
#   [0 1]
#   [1 0]
#   [0 1]

print("Checking if A(BC) == (AB)C:")
print(A * (B * C) == (A * B) * C)

#   OUTPUT:
#   Checking if A(BC) == (AB)C:
#   True
