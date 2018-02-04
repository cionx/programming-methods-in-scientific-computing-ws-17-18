class Rational():
    def __init__(self, num, denum = 1):   # default denumerator is 1
        if type(num) == Rational:
            p = num/Rational(denum)
            self.num = p.num
            self.denum = p.denum
        elif type(num) != int:
            raise TypeError("numerator is no integer")
        elif type(denum) != int:
            raise TypeError("denumerater is no integer")
        elif denum == 0:
            raise ZeroDivisionError("denumerator is zero")
        else:
            self.num = num
            self.denum = denum
    
    # allows printing of rational numbers
    def __str__(self):
        return "{}/{}".format(self.num, self.denum)
    
    def __repr__(self):
        return str(self)
    
    # adding to a rational number
    def __add__(self, other):
        if type(other) == int:
            return self + Rational(other)
        elif type(other) == Rational:
            return Rational( self.num * other.denum + self.denum * other.num, self.denum * other.denum )
        raise TypeError("unsupported operand type(s) for + or add(): 'Rational' and '{}'".format(type(other).__name__))
    
    # subtracting from a rational number
    def __sub__(self, other):
        if type(other) == int:
            return self - Rational(other)
        elif type(other) == Rational:
            return Rational( self.num * other.denum - self.denum * other.num, self.denum * other.num )
        raise TypeError("unsupported operand type(s) for - or sub(): 'Rational' and '{}'".format(type(other).__name__))
    
    # multipliy to a rational number
    def __mul__(self, other):
        if type(other) == int:
            return self * Rational(other)
        elif type(other) == Rational:
            return Rational( self.num * other.num, self.denum * other.denum )
        raise TypeError("unsupported operand type(s) for * or mul(): 'Rational' and '{}'".format(type(other).__name__))
    
    # divide a rational number
    def __truediv__(self, other):
        if type(other) == int:
            return self / Rational(other)
        elif type(other) == Rational:
            if other.num == 0:
                raise ZeroDivisionError("division by zero")
            return Rational( self.num * other.denum, self.denum * other.num)
        raise TypeError("unsupported operand type(s) for / or truediv(): 'Rational' and '{}'".format(type(other).__name__))
    
    # powers of rational number
    def __pow__(self, n):   # supports only integer powers
        if not type(n) == int:
            raise TypeError("unsupported operand type(s) for ** or pow(): 'Rational' and '{}'".format(type(n).__name__))
        if n >= 0:
            return Rational(self.num**n, self.denum**n)
        return Rational(self.denum, self.num)**(-n)
    
    # +x for rational x
    def __pos__(self):
        return Rational( self.num, self.denum )
    
    # -x for rational x
    def __neg__(self):
        return Rational( -self.num, self.denum )
    
    # absolute value
    def __abs__(self):
        return Rational(abs(self.num), abs(self.denum))
    
    # equality of rational numbers
    def __eq__(self, other):
        if type(other) == int:  # allows comparison to int, used for x == 0
            return (self == Rational(other))
        elif type(other) == Rational:
            return (self.num * other.denum == self.denum * other.num)
        raise TypeError("unsupported operand type(s) for == or eq(): 'Rational' and '{}'".format(type(other).__name__))
    
    # casts to float
    def __float__(self):
        return self.num / self.denum
