from Matrix import *
from math import sqrt

def cholesky(A):    # expects int or float as matrix entries
    if A.height != A.width:
        raise ValueError("matrix is not square")
    B = copymatrix(A)
    n = B.height
    L = zeromatrix(n,n)
    for i in range(n):
        rowsum = 0
        for j in range(i):
            s = 0
            for k in range(j):
                s += L[i][k] * L[j][k]
            L[i][j] = (B[i][j] - s)/L[j][j]
            rowsum += L[i][j]**2
        L[i][i] = sqrt( B[i][i] - rowsum )
    return L

A = Matrix([[1,2,1],[2,5,2],[1,2,10]])
print("A:")
print(A)

#   A:
#   [1 2 1 ]
#   [2 5 2 ]
#   [1 2 10]

L = cholesky(A)
print("L:")
print(L)

#   L:
#   [1.0 0   0  ]
#   [2.0 1.0 0  ]
#   [1.0 0.0 3.0]

print("L * L^T:")
print(L * L.transpose())

#   L * L^T:
#   [1.0 2.0 1.0 ]
#   [2.0 5.0 2.0 ]
#   [1.0 2.0 10.0]

B = Matrix([[1.01E-2, 0.705, 1.42E-2],[0.705,49.5,1],[1.42E-2,1,1]])
print("B:")
print(B)

#   B:
#   [0.0101 0.705 0.0142]
#   [0.705  49.5  1     ]
#   [0.0142 1     1     ]

L = cholesky(B)
print("L:")
print(L)

#   L:
#   [0.1004987562112089  0                    0                 ]
#   [7.015012190980423   0.5381486415443629   0                 ]
#   [0.14129528100981847 0.016374437298272527 0.9898320672556135]

print("L * L^T:")
print(L * L.transpose())

#   L * L^T:
#   [0.010100000000000001 0.705 0.014200000000000003]
#   [0.705                49.5  1.0                 ]
#   [0.014200000000000003 1.0   1.0                 ]
