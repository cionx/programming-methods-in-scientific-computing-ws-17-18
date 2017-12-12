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

xct = solve(A, b)
print("The solution to Ax = b is:")
print(xct)

L,D,U = ldu(A)
n = 3
x = array([3,3,3])
for i in range(n+1):
    x = inv(D + L) @ (b - U @ x)

print("An approximate solution to Ax = b is:")
print(x)
print("The difference is:")
print(xct - x)
