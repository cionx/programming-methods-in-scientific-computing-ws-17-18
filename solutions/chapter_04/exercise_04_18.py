from scipy import *
from scipy.linalg import *

def ldu(A):
    (n, m) = A.shape
    if n != m:
        return ValueError("matrix is not square")
    L = zeros((n,n))
    D = zeros((n,n))
    U = zeros((n,n))
    for i in range(n):
        # splitting up the i-th row
        L[i,:i] = A[i,:i]
        D[i,i] = A[i,i]
        U[i, i+1:] = A[i, i+1:]
    return(L,D,U)

A = array([[4,3,0],[3,4,-1],[0,-1,4]])
print("A:")
print(A)
b = array([24,30,-24])
print("b:")
print(b)

### OUTPUT:
#   A:
#   [[ 4  3  0]
#    [ 3  4 -1]
#    [ 0 -1  4]]
#   b:
#   [ 24  30 -24]

exact = solve(A, b)
print("The solution to Ax = b is:")
print(exact)

### OUTPUT:
#   The solution to Ax = b is:
#   [ 3.  4. -5.]

L,D,U = ldu(A)
n = 3  # iterations steps
x = array([3,3,3])  # starting point
for i in range(n+1):
    x = inv(D + L) @ (b - U @ x)

print("An approximate solution to Ax = b is:")
print(x)
print("The difference is:")
print(exact - x)

### OUTPUT:
#   An approximate solution to Ax = b is:
#   [ 2.57885742  4.35095215 -4.91226196]
#   The difference is:
#   [ 0.42114258 -0.35095215 -0.08773804]
