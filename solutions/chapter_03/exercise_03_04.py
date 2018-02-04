### CLASSES

from matrices import *
from rationals import *
from copy import deepcopy

# expects the matrix entries to be comparable to 0 in a sensible way
def naive_lu(A):
    if A.height() != A.width():
        raise ValueError("matrix is not square")
    U = deepcopy(A)   # circumvent pass by reference
    n = U.height()
    L = identitymatrix(n)
    # bring U in upper triangular form, change L such that always LU = A
    for j in range(n):
        if U[j][j] == 0:
            raise ValueError("algorithm does not work for this matrix")
        for i in range(j+1,n):
            L.addcolumntofrom(j, i,  U[i][j]/U[j][j]) # important: change L first
            U.addrowtofrom(i, j, -U[i][j]/U[j][j])
    return (L,U)

A = Matrix(3, 3, [[3,2,1],[6,6,3],[9,10,6]])
print("A:")
print(A)

### OUTPUT:
#   A:
#   [3 2  1]
#   [6 6  3]
#   [9 10 6]

(L,U) = naive_lu(mapentries(A, Rational))
print("L:")
print(L)
print("U:")
print(U)
print("Check if L*U == A:")
print(mapentries(L, Rational) * mapentries(U, Rational) == A)

### OUTPUT:
#   L:
#   [9/9  0/18  0]
#   [18/9 18/18 0]
#   [27/9 36/18 1]
#   U:
#   [3/1   2/1   1/1    ]
#   [0/3   6/3   3/3    ]
#   [0/162 0/162 162/162]
#   Check if L*U == A:
#   True

B = Matrix(2, 2, [[0,1],[1,0]])
print("B:")
print(B)

### OUTPUT:
#   B:
#   [0 1]
#   [1 0]

print("Trying to calculate the LU decomposition of B:")
(L,U) == naive_lu(B)

### OUTPUT:
#   Trying to calculate the LU decomposition of B:
#   Traceback (most recent call last):
#     File "exercise_03_04.py", line 57, in <module>
#       (L,U) == naive_lu(B)
#     File "exercise_03_04.py", line 17, in naive_lu
#       raise ValueError("algorithm does not work for this matrix")
#   ValueError: algorithm does not work for this matrix
