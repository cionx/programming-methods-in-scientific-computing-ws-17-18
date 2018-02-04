### MAIN CLASS

class Matrix():
    # constructor takes list of rows
    def __init__(self, m, n, entries):
        self.rows = m
        self.cols = n
        self.entries = entries

    # gets the rows via A[i]
    def __getitem__(self, i):       
        return self.entries[i]
    
    # sets the rows via A[i]
    def __setitem__(self, i, r):
        self.entries[i] = r

    def height(self):
        return self.rows;
    
    def width(self):
        return self.cols;

    # converts matrix to a string for printing
    # constructs the matrix columnwise, left aligned
    def __str__(self):
        rowstrings = [ "" ]*self.rows
        for j in range(self.cols): # going trough columns
            numbers = []            # numbers to appear in column j
            maxlen = 0              # maximal length of a number in column j
            for i in range(self.rows):
                s = str(self[i][j])
                numbers.append(s)
                maxlen = max(len(s), maxlen)
            for i in range(self.rows):
                # pad the entries if they are too short
                numbers[i] += " "*(maxlen-len(numbers[i]))
                # build up column in string
                rowstrings[i] += numbers[i] + " "
        # put the row strings together
        s = ""
        for r in rowstrings:
            s += "[" + r[:-1] + "]\n" # remove white space at the end of lines
        s = s[:-1]                    # remove at newline at the end
        return s
    
    def __repr__(self):
        return str(self)
    
    # addition of matrices of the same dimensions
    def __add__(self, other):
        if self.rows != other.rows:
            raise ValueError('cannot add matrices of different height')
        if self.cols != other.cols:
            raise ValueError('cannot add matrices of different width')
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                row.append(self[i][j] + other[i][j])
            result.append(row)
        return Matrix(self.rows, self.cols, result)
    
    # multiplication to matrices of compatible dimensions
    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError('cannot multipliy matrices of wrong dimensions')
        # special check for empty matrices
        if self.cols == 0 or self.rows == 0 or other.rows == 0 or other.cols == 0:
            return zeromatrix(self.rows, other.cols)
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                s = self[i][0] * other[0][j]  # makes sure s has right type
                for k in range(1, self.cols):
                    s += self[i][k] * other[k][j]
                row.append(s)
            result.append(row)
        return Matrix(self.rows, other.cols, result)
    
    # compares two matrices entrywise
    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
                return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self[i][j] != other[i][j]:
                    return False
        return True
    
    # add row i -> i + c*j
    def addrowtofrom(self, i, j, c):
        for k in range(self.cols):
            # make c responsible for implementing the multiplication
            self[i][k] =  c * self[j][k] +  self[i][k]
    
    # add column i -> i + c*j
    def addcolumntofrom(self, i, j, c):
        for k in range(self.rows):
            # make c responsible for implementing the multiplication
            self[k][i] = c * self[k][j] + self[k][i]
    
    # multiply row i -> c*i
    def multrow(self, i, c):
        for j in range(self.cols):
            self[i][j] = c * self[i][j]
    
    # multipliy column j -> c*j
    def multcolumn(self, j, c):
        for i in range(self.rows):
            self[i][j] = c * self[i][j]
    
    # swap rows i <-> j
    def swaprows(self, i, j):
        temp = self[i]
        self[i] = self[j]
        self[j] = temp
    
    # swap columns i <-> j
    def swapcolumns(self, i, j):
        for k in range(self.rows):
            temp = self[k][i]
            self[k][i] = self[k][j]
            self[k][j] = temp





### AUXILIARY MATRIX FUNCTIONS

# creates a zero matrix of given height and width
def zeromatrix(height, width):  
    entries = []
    for i in range(height):
        entries.append([0]*width)
    return Matrix(height, width, entries)

# creates an identiy matrix of given square size
def identitymatrix(size):
    E = zeromatrix(size, size)
    for i in range(size):
        E[i][i] = 1
    return E

# creates the transposed matrix
def transpose(A):
    m = A.height()
    n = A.width()
    result = []
    for i in range(m):
        row = []
        for j in range(n):
                row.append(A[j][i])
        result.append(row)
    return Matrix(n, m, result)

# creates a new matrix by applying a function entrywise to a given matrix
def mapentries(A, f):
    m = A.height()
    n = A.width()
    result = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(f(A[i][j]))
        result.append(row)
    return Matrix(m, n, result)
