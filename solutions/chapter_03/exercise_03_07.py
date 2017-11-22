from matrices import *
from math import sqrt

# assumes the matrix to have integer or float values
# and to be nonsingular
def qrdecomp(A):
    if A.height != A.width:
        return ValueError("only square matrices are supported")
    n = A.height
    Q = copymatrix(A)
    R = identitymatrix(n)
    for j in range(n):
        # make the j-th column of Q orthogonal to the next columns
        for k in range(j):
            s = 0   # inner product of j-th and k-th columns
            for i in range(n):
                s += Q[i][j] * Q[i][k]
            Q.addcolumn(j, k, -s)
            R.addrow(k, j, s)
        sn = 0   # squared norm of the j-th column
        for i in range(n):
            sn += Q[i][j]**2
        Q.multcolumn(j, sqrt(sn)**(-1))
        R.multrow(j, sqrt(sn))
    return (Q,R)


A = Matrix([[12,-51,4],[6,167,-68],[-4,24,-41]])
print("A:")
print(A)

#   A:
#   [12 -51 4  ]
#   [6  167 -68]
#   [-4 24  -41]

(Q,R) = qrdecomp(A)
print("Q:")
print(Q)

#   Q:
#   [0.8571428571428571  -0.3942857142857143 -0.33142857142857124]
#   [0.42857142857142855 0.9028571428571428  0.03428571428571376 ]
#   [-0.2857142857142857 0.17142857142857143 -0.9428571428571428 ]


print("Q * Q^T:")
print(Q * Q.transpose())

#   Q * Q^T:
#   [0.9999999999999998      1.474514954580286e-16 -1.6653345369377348e-16]
#   [1.474514954580286e-16   0.9999999999999998    4.996003610813204e-16  ]
#   [-1.6653345369377348e-16 4.996003610813204e-16 1.0

print("R:")
print(R)

#   R:
#   [14.0 20.999999999999996 -14.000000000000002]
#   [0.0  175.0              -69.99999999999999 ]
#   [0.0  0.0                35.0               ]

print("Q*R:")
print(Q*R)

#   Q*R:
#   [12.0 -51.0 4.000000000000002]
#   [6.0  167.0 -68.0            ]
#   [-4.0 24.0  -41.0            ]
