### MAIN CLASS

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
    
    def __repr__(self):
        return str(self)
    
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
    
    def mapentries(self, f):        # applies a function to all entries
        A = zeromatrix(self.height, self.width) # zeromatrix is defined below
        for i in range(self.height):
            for j in range(self.width):
                A[i][j] = f(self[i][j])
        return A
    
    def addrow(self, i, j, c):      # add c times row j to row i
        for k in range(self.width):
            self[i][k] =  c * self[j][k] + self[i][k]
            # makes c responsible for implementing the operations
    
    def addcolumn(self, i, j, c):   # add c times column j from colunm i
        for k in range(self.height):
            self[k][i] = c * self[k][j] + self[k][i]
    
    def multrow(self, i, c):        # multiply row i with c
        for j in range(self.width):
            self[i][j] = c * self[i][j]
    
    def swaprows(self, i, j):       # swap rows i and j
        if i > self.height or j > self.height:
            raise ValueError("swap nonexistent rows")
        l = self[i]
        self[i] = self[j]
        self[j] = l
    
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

def identitymatrix(size):       # creates an identiy matrix
    E = zeromatrix(size, size)
    for i in range(size):
        E[i][i] = 1
    return E

def copymatrix(A):              # forcefully copies a matrix
    B = zeromatrix(A.height, A.width)
    for i in range(A.height):
        for j in range(A.width):
            B[i][j] = A[i][j]
    return B
