### CLASSES

class Rational():
    def __init__(self, num, denum = 1):   # default denumerator is 1
        if type(num) != int:
            raise TypeError("numerator is no integer")
        if type(denum) != int:
            raise TypeError("denumerater is no integer")
        if denum == 0:
            raise ZeroDivisionError("denumerator is zero")
        self.num = num        
        self.denum = denum
    
    def __str__(self):    # allows print(x) for Rational x
        return "{}/{}".format(self.num, self.denum)
    
    def __add__(self, other):
        return Rational( self.num * other.denum + self.denum * other.num, self.denum * other.denum )
    
    def __sub__(self, other):
        return Rational( self.num * other.denum - self.denum * other.num, self.denum * other.num )
    
    def __neg__(self):
        return Rational( -self.num, self.denum )
    
    def __mul__(self, other):
        return Rational( self.num * other.num, self.denum * other.denum )
    
    def __truediv__(self, other):
        if other.num == 0:
            raise ZeroDivisionError("division by zero")
        return Rational( self.num * other.denum, self.denum * other.num)
    
    def inverse(self):  # short hand notation
        return Rational(1)/self
    
    def __eq__(self, other):
        if type(other) == int:  # allows comparison to int, used for x == 0
            return (self == Rational(other))
        return (self.num * other.denum == self.denum * other.num)
    
    def __float__(self):
        return self.num / self.denum



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
    
    def __str__(self):
        rows = ["["]*self.height
        for j in range(self.width): # build the output columnwise
            numbers = []            # the numbers to appear in column j
            maxlen = 0              # the maximal length of a number column j
            for i in range(self.height):
                s = str(self[i][j])
                numbers.append(s)
                if len(s) > maxlen:
                    maxlen = len(s)
            for i in range(self.height):
                # pad the entries if they are too short
                rows[i] += numbers[i] + " "*(maxlen - len(numbers[i])) + " " 
        s = ""
        for r in rows:
            s += r[:-1] + "]\n" # remove white space at the end of each line
        s = s[:-1]              # remove an empty line
        return s
    
    def __mul__(self, other):
        if self.width != other.height:
            raise TypeError('matrix dimensions do not match')
        entries = []    # entries of the new matrix
        for i in range(self.height):
            row = []
            for j in range(other.width):
                s = self[i][0] * other[0][j]  # s has the right type
                for k in range(1, self.width):
                    s += self[i][k] * other[k][j]
                row.append(s)
            entries.append(row)
        return Matrix(entries)
    
    def __eq__(self, other):
        if self.height != other.height or self.width != other.width:
                return False2
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
    
    def addrow(self, i, j, c=1):    # add c times row j to row i
        for k in range(self.width):
            self[i][k] = self[i][k] + self[j][k] * c
    
    def addcolumn(self, i, j, c=1): # add c times column j from colunm i
        for k in range(self.height):
            self[k][i] = self[k][i] + self[k][j] * c



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



### PRIMARY FUNCTION

def naive_lu(A):  # expects integer valued matrix as input
    if A.height != A.width:
        raise ValueError("matrix is not square")
    U = copymatrix(A)   # circumvent pass by reference
    n = U.height
    L = identitymatrix(n)
    U = U.mapentries(Rational)   # make all
    L = L.mapentries(Rational)   # entries rational
    # bring U in upper triangular form, change L such that always LU = A
    for j in range(n):
        if U[j][j] == 0:
            raise ValueError("algorithm does not work for this matrix")
        for i in range(j+1,n):
            L.addcolumn(j, i,  U[i][j]/U[j][j]) # important: change L first
            U.addrow(i, j, -U[i][j]/U[j][j])
    return (L,U)


### EXAMPLES
#
#   >>> A = Matrix([[3,2,1],[6,6,3],[9,10,6]])
#   >>> (L,U) = naive_lu(A)
#   >>> print(L)
#   [9/9  0/18  0/1]
#   [18/9 18/18 0/1]
#   [27/9 36/18 1/1]
#   >>> print(U)
#   [3/1   2/1   1/1    ]
#   [0/3   6/3   3/3    ]
#   [0/162 0/162 162/162]
#   >>> print( (L*U).mapentries(float) )
#   [3.0 2.0  1.0]
#   [6.0 6.0  3.0]
#   [9.0 10.0 6.0]
#
#   >>> B = Matrix([[0,1],[1,0]])
#   >>> (L,U) == naive_lu(B)
#   Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 12, in naive_lu
#   ValueError: algorithm does not work for this matrix
#
###
