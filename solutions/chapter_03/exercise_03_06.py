from Rational import *
from Matrix import *



# we assume that the input matrix is well-behaved
# i.e. entries allow a reasonable comparison to 0
def invert(A):
    if A.height != A.width:
        raise ValueError("matrix is not square")
    B = copymatrix(A)   # circumvent pass by reference
    n = B.height
    Inv = identitymatrix(n)
    B = B.mapentries(Rational)      # make all
    Inv = Inv.mapentries(Rational)  # entries rational
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
            Inv.addrow(i, p, -B[i][j]/B[p][j])  # import: change inverse first
            B.addrow(i, p, -B[i][j]/B[p][j])
    # norm the diagonal entries
    for i in range(n):
        Inv.multrow(i, B[i][i]**(-1))   # **(-1) also works for Rational
        B.multrow(i, B[i][i]**(-1))
    # bring B into identity form
    for j in range(n):
        for i in range(j):
            Inv.addrow(i, j, -B[i][j])
            B.addrow(i, j, -B[i][j])
    return Inv



A = Matrix([[3,-1,2],[-3,4,-1],[-6,5,-2]])
print("A:")
print(A)

#   A:
#   [3  -1 2 ]
#   [-3 4  -1]
#   [-6 5  -2]

B = invert(A)
print("A^(-1) with rationals:")
print(B)

#   A^(-1) with rationals:
#   [-1162261467/3486784401 3099363912/3486784401 -2711943423/3486784401]
#   [0/43046721             28697814/43046721     -14348907/43046721    ]
#   [59049/59049            -59049/59049          59049/59049           ]

print("A^(-1) with floats:")
print(B.mapentries(float))

#   A^(-1) with floats:
#   [-0.3333333333333333 0.8888888888888888 -0.7777777777777778]
#   [0.0                 0.6666666666666666 -0.3333333333333333]
#   [1.0                 -1.0               1.0                ]

print("Checking if A*B = I (using rationals):")
print(A.mapentries(Rational) * B == identitymatrix(3))

#   Check if A*B = I (using rationals):
#   True
