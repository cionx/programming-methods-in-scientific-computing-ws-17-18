from rationals import *
from matrices import *
from copy import deepcopy

# expects the matrix entries to be int or Rational
def invert(A):
    if A.height() != A.width():
        raise ValueError("matrix is not square")
    B = deepcopy(A)   # circumvent pass by reference
    n = B.height()
    Inv = identitymatrix(n)
    B = mapentries(B,Rational)      # make all the
    Inv = mapentries(Inv,Rational)  # entries rational
    # bring B in lower triangular form
    for j in range(n):
        p = -1
        for i in range(j,n):
            if B[i][j] != 0:
                p = i
                break
        if p == -1:
            raise ZeroDivisionError("matrix is not invertible")
        for i in range(p+1,n):
            Inv.addrowtofrom(i, p, -B[i][j]/B[p][j])  # import: change inverse first
            B.addrowtofrom(i, p, -B[i][j]/B[p][j])
    # norm the diagonal entries
    for i in range(n):
        Inv.multrow(i, B[i][i]**(-1))   # **(-1) also works for Rational
        B.multrow(i, B[i][i]**(-1))
    # bring B into identity form
    for j in range(n):
        for i in range(j):
            Inv.addrowtofrom(i, j, -B[i][j])
            B.addrowtofrom(i, j, -B[i][j])
    return Inv



A = Matrix(3, 3, [[3,-1,2],[-3,4,-1],[-6,5,-2]])
print("A:")
print(A)

### OUTPUT:
#   A:
#   [3  -1 2 ]
#   [-3 4  -1]
#   [-6 5  -2]

B = invert(A)
print("A^(-1) with rationals:")
print(B)
print("A^(-1) with floats:")
print(mapentries(B,float))

### OUTPUT:
#   A^(-1) with rationals:
#   [-1162261467/3486784401 3099363912/3486784401 -2711943423/3486784401]
#   [0/43046721             28697814/43046721     -14348907/43046721    ]
#   [59049/59049            -59049/59049          59049/59049           ]
#   A^(-1) with floats:
#   [-0.3333333333333333 0.8888888888888888 -0.7777777777777778]
#   [0.0                 0.6666666666666666 -0.3333333333333333]
#   [1.0                 -1.0               1.0                ]

print("Checking if A*B == I (using rationals):")
print(mapentries(A,Rational) * B == identitymatrix(3))

### OUTPUT:
#   Check if A*B = I (using rationals):
#   True
