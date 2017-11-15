from math import sqrt

class matrix():
    def __init__(self, entries):
        m = len(entries)
        if m == 0:
            raise ValueError("The height needs to be positive.")
        n = len(entries[0])
        if n == 0:
            raise ValueError("The width needs to be positive.")
        for i in range(1, m):
            if len(entries[i]) != n:
                raise ValueError("Rows need to have the same width.")
        self.height = m
        self.width = n
        self.entries = entries
    
    def __getitem__(self, i):   # allows to get the rows via A[i]
        return self.entries[i]
    
    def __setitem__(self, i, k):    # allows to set rows via A[i]
        self.entries[i] = k
    
    def __str__(self):
        rows = ["["]*self.height
        for j in range(self.width): # build the output columnwise
            numbers = []            # the numbers to appear in the j-th column
            maxlen = 0              # the maximal length of a number in the j-th column
            for i in range(self.height):
                s = str(self[i][j])
                numbers.append(s)
                if len(s) > maxlen:
                    maxlen = len(s)
            for i in range(self.height):
                rows[i] += numbers[i] + " " * (maxlen - len(numbers[i])) + " "  # pad the entries if they are too short
        s = ""
        for r in rows:
            s += r[:-1] + "]\n" # remove the unnecessary white space at the end of ech line
        s = s[:-1]              # remove an empty line at the end
        return s
    
    def __mul__(self, other):
        if self.width != other.height:
            raise TypeError('matrix dimensions do not match')
        entries = []    # entries of the new matrix
        for i in range(self.height):
            row = []
            for j in range(other.width):
                s = 0   # current sum of the i-j-th entry
                for k in range(self.width):
                    s += self[i][k] * other[k][j]
                row.append(s)
            entries.append(row)
        return matrix(entries)
    
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



def zeromatrix(height, width):  # creates a zero matrix
    entries = []
    for i in range(height):
        entries.append([0]*width)
    return matrix(entries)

def copymatrix(A):  # copies a matrix
    B = zeromatrix(A.height, A.width)
    for i in range(A.height):
        for j in range(A.width):
            B[i][j] = A[i][j]
    return B



def cholesky(A):
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

A = matrix([[1,2,1],[2,5,2],[1,2,10]])
print(A)
L = cholesky(A)
print(L * L.transpose())

B = matrix([[1.01E-2, 0.705, 1.42E-2],[0.705,49.5,1],[1.42E-2,1,1]])
print(B)
L = cholesky(B)
print(L * L.transpose())
