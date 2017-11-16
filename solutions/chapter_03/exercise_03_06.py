### CLASSES

class Rational():
    def __init__(self, num, denum = 1): # default denumerator is 1
        if type(num) != int:
            raise TypeError("numerator is no integer")
        if type(denum) != int:
            raise TypeError("denumerater is no integer")
        if denum == 0:
            raise ZeroDivisionError("denumerator is zero")
        self.num = num        
        self.denum = denum
    
    def __str__(self):  # allows print(A) for a matrix A
        return "{}/{}".format(self.num, self.denum)
    
    def __add__(self, other):
        return Rational( self.num * other.denum + self.denum * other.num, self.denum * other.denum )
    
    def __sub__(self, other):
        Rational( self.num * other.denum - self.denum * other.num, self.denum * other.num )
    
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
        if type(other) == int:  # allowing comparison to int, useful for x == 0
            return (self == Rational(other))
        return (self.num * other.denum == self.denum * other.num)
    
    def __float__(self):
        return self.num / self.denum



class matrix():
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
                s = self[i][0] * other[0][j]    # starting sum, makes sure s has the right type
                for k in range(1, self.width):
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
    
    def map(self, f):   # applies a function to all entries
        for i in range(self.height):
            for j in range(self.width):
                self[i][j] = f(self[i][j])
    
    def swaprows(self, i, j):   # swap rows i and j
        if i > self.height or j > self.height:
            raise ValueError("swap nonexistent rows")
        l = self[i]
        self[i] = self[j]
        self[j] = l
    
    def addrow(self, i, j, c=1): # add c times row j to row i
        for k in range(self.width):
            self[i][k] = self[i][k] + self[j][k] * c
    
    def addcolumn(self, i, j, c=1): # add c times column j from colunm i
        for k in range(self.height):
            self[k][i] = self[k][i] + self[k][j] * c
    
    def multrow(self, i, c):    # multiply row i with c
        for j in range(self.width):
            self[i][j] *= c



### AUXILIARY MATRIX FUNCTIONS

def zeromatrix(height, width):  # creates a zero matrix
    entries = []
    for i in range(height):
        entries.append([0]*width)
    return matrix(entries)

def identitymatrix(size):   # creates an identiy matrix
    E = zeromatrix(size, size)
    for i in range(size):
        E[i][i] = 1
    return E

def copymatrix(A):  # copies a matrix
    B = zeromatrix(A.height, A.width)
    for i in range(A.height):
        for j in range(A.width):
            B[i][j] = A[i][j]
    return B



### PRIMARY FUNCTION

# allowed input are integer matrices
def invert(A):
    if A.height != A.width:
        raise ValueError("matrix is not square")
    B = copymatrix(A)   # circumvent pass by reference
    n = B.height
    Inv = identitymatrix(n)
    B.map(Rational)     # make all
    Inv.map(Rational)   # entries rational
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
        Inv.multrow(i, B[i][i].inverse())
        B.multrow(i, B[i][i].inverse())
    # bring B into identity form
    for j in range(n):
        for i in range(j):
            Inv.addrow(i, j, -B[i][j])
            B.addrow(i, j, -B[i][j])
    return Inv

A = matrix([[3,-1,2],[-3,4,-1],[-6,5,-2]])
B = invert(A)
