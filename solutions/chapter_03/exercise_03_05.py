### CLASSES

class Matrix():
    def __init__(self, entries):
        m = len(entries)
        if m == 0:
            raise ValueError("height must be positive")
        n = len(entries[0])
        if n == 0:
            raise ValueError("width must be positive")
        for i in range(1, m):
            if len(entries[i]) != n:
                raise ValueError("rows must have the same width")
        self.height = m
        self.width = n
        self.entries = entries
    
    def __getitem__(self, i):       # allows to get the rows via A[i]
        return self.entries[i]
    
    def __setitem__(self, i, k):    # allows to set rows via A[i]
        self.entries[i] = k
    
    def __str__(self):              # allows print(A) for a Matrix A
        rows = ["["]*self.height
        for j in range(self.width): # construct output columnwise, align left
            numbers = []            # numbers to appear in column j
            maxlen = 0              # maximal length of a number in column j
            for i in range(self.height):
                s = str(self[i][j])
                numbers.append(s)
                if len(s) > maxlen:
                    maxlen = len(s)
            for i in range(self.height):
                # pad the entries if they are too short
                rows[i] += numbers[i] + " "*(maxlen-len(numbers[i])) + " "
        s = ""
        for r in rows:
            s += r[:-1] + "]\n" # remove white space at the end of ech line
        s = s[:-1]              # remove empty line at the end
        return s
    
    def __mul__(self, other):
        if self.width != other.height:
            raise TypeError('matrix dimensions do not match')
        newentries = []
        for i in range(self.height):
            row = []
            for j in range(other.width):
                s = self[i][0] * other[0][j]    # makes s have the right type
                for k in range(1, self.width):
                    s += self[i][k] * other[k][j]
                row.append(s)
            newentries.append(row)
        return Matrix(newentries)
    
    def __eq__(self, other):
        if self.height != other.height or self.width != other.width:
                return False
        for i in range(self.height):
            for j in range(self.width):
                if self[i][j] != other[i][j]:
                    return False
        return True
    
    def transpose(self):
        T = zeromatrix(self.width, self.height)
        for i in range(self.height):
            for j in range(self.width):
                T[j][i] = self[i][j]
        return T



### AUXILIARY MATRIX FUNCTIONS

def zeromatrix(height, width):  # creates a zero matrix
    entries = []
    for i in range(height):
        entries.append([0]*width)
    return Matrix(entries)

def copymatrix(A):  # copies a matrix
    B = zeromatrix(A.height, A.width)
    for i in range(A.height):
        for j in range(A.width):
            B[i][j] = A[i][j]
    return B



### PRIMARY FUNCTION

def cholesky(A):
    from math import sqrt
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

### EXAMPLES
#
#   >>> A = Matrix([[1,2,1],[2,5,2],[1,2,10]])
#   >>> L = cholesky(A)
#   >>> print(L)
#   [1.0 0   0  ]
#   [2.0 1.0 0  ]
#   [1.0 0.0 3.0]
#   >>> print(L * L.transpose())
#   [1.0 2.0 1.0 ]
#   [2.0 5.0 2.0 ]
#   [1.0 2.0 10.0]
#
#   >>> B = Matrix([[1.01E-2, 0.705, 1.42E-2],[0.705,49.5,1],[1.42E-2,1,1]])
#   >>> L = cholesky(B)
#   >>> print(L)
#   [0.1004987562112089  0                    0                 ]
#   [7.015012190980423   0.5381486415443629   0                 ]
#   [0.14129528100981847 0.016374437298272527 0.9898320672556135]
#   >>> print(L * L.transpose())
#   [0.010100000000000001 0.705 0.014200000000000003]
#   [0.705                49.5  1.0                 ]
#   [0.014200000000000003 1.0   1.0                 ]
#
###
