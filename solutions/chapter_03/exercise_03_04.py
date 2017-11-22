### CLASSES

from rationals import *
from matrices import *
from copy import deepcopy

# expects the matrix entries to be comparable to 0 in a sensible way
def naive_lu(A): 
    if A.height != A.width:
        raise ValueError("matrix is not square")
    U = deepcopy(A)   # circumvent pass by reference
    n = U.height
    L = identitymatrix(n)
    # bring U in upper triangular form, change L such that always LU = A
    for j in range(n):
        if U[j][j] == 0:
            raise ValueError("algorithm does not work for this matrix")
        for i in range(j+1,n):
            L.addcolumn(j, i,  U[i][j]/U[j][j]) # important: change L first
            U.addrow(i, j, -U[i][j]/U[j][j])
    return (L,U)

A = Matrix([[3,2,1],[6,6,3],[9,10,6]])
print("A:")
print(A)

#   A:
#   [3 2  1]
#   [6 6  3]
#   [9 10 6]

(L,U) = naive_lu(A.mapentries(Rational))
print("L:")
print(L)

#   L:
#   [9/9  0/18  0]
#   [18/9 18/18 0]
#   [27/9 36/18 1]

print("U:")
print(U)

#   U:
#   [3/1   2/1   1/1    ]
#   [0/3   6/3   3/3    ]
#   [0/162 0/162 162/162]

print("Check if L*U == A:")
print(L.mapentries(Rational) * U.mapentries(Rational) == A)

#   Check if L*U == A:
#   True

B = Matrix([[0,1],[1,0]])
print("B:")
print(B)

#   B:
#   [0 1]
#   [1 0]

print("Trying to calculate the LU decomposition of B:")
(L,U) == naive_lu(B)

#   Trying to calculate the LU decomposition of B:
#   Traceback (most recent call last):
#     File "exercise_03_04.py", line 57, in <module>
#       (L,U) == naive_lu(B)
#     File "exercise_03_04.py", line 17, in naive_lu
#       raise ValueError("algorithm does not work for this matrix")
#   ValueError: algorithm does not work for this matrix
