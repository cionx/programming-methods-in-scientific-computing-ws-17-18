class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients
        
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

### Example:
#
#   >>> p = Polynomial([1,2,3])
#   >>> p.derivative().coeff
#   [2, 6]
#   >>> p.antiderivative().coeff
#   [0, 1.0, 1.0, 1.0]
#   >>> p.antiderivative().derivative().coeff
#   [1.0, 2.0, 3.0]
#
###
