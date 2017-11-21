class Polynomial:
    def __init__(self, coeff):
        self.coeff = coeff
    
    def __str__(self):
        s = ""
        if self.coeff == []:
            s = "0"
        else:
            s += "{} x^0".format(self.coeff[0])
        for i in range(1,len(self.coeff)):
            s += " + {} x^{}".format(self.coeff[i], i)
        return s
    
    def __repr__(self):
        return str(s)
    
    def __call__(self, x):
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s
    
    def __add__(self, other):
        l = []
        if len(self.coeff) > len(other.coeff):
            l += self.coeff
            for i in range(len(other.coeff)):
                l[i] += other.coeff[i]
        else:
            l += other.coeff
            for i in range(len(self.coeff)):
                l[i] += self.coeff[i]
        return Polynomial(l)
    
    def __eq__(self, other):
        return self.coeff == other.coeff
    
    def derivative(self):
        coeff = []
        for i in range(1,len(self.coeff)):
            coeff.append(i * self.coeff[i])
        return Polynomial(coeff)
    
    def antiderivative(self):
        coeff = [0]
        for i in range(len(self.coeff)):
            coeff.append(self.coeff[i]/(i+1))
        return Polynomial(coeff)

p = Polynomial([1,2,3])
print("The given polynmial p:")
print(p)

#   The given polynmial p:
#   1 x^0 + 2 x^1 + 3 x^2

print("The derivative of p:")
print( p.derivative() )

#   The derivative of p:
#   2 x^0 + 6 x^1

print("The antiderivative of p:")
print( p.antiderivative() )

#   The antiderivative of p:
#   0 x^0 + 1.0 x^1 + 1.0 x^2 + 1.0 x^3

print("Taking antiderivative and then derivative:")
print( p.antiderivative().derivative() )

#   Taking antiderivative and then derivative:
#   1.0 x^0 + 2.0 x^1 + 3.0 x^2
