from matrices import *

A = Matrix([[0,1],[1,0],[1,1]])
print("A:")
print(A)

#   A:
#   [0 1]
#   [1 0]
#   [1 1]

B = Matrix([[1,2,3,4],[5,6,7,8]])
print("B:")
print(B)

#   B:
#   [1 2 3 4]
#   [5 6 7 8]

C = Matrix([[1,0],[0,1],[1,0],[0,1]])
print("C:")
print(C)

#   C:
#   [1 0]
#   [0 1]
#   [1 0]
#   [0 1]

print("Checking if A(BC) == (AB)C:")
print(A * (B * C) == (A * B) * C)

#   Checking if A(BC) == (AB)C:
#   True
