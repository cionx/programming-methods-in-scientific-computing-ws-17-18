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
        l = []
        for i in range(1,len(self.coeff)):
            l.append(i * self.coeff[i])
        return Polynomial(l)
    
    def antiderivative(self):
        l = [0]
        for i in range(len(self.coeff)):
            l.append(self.coeff[i]/(i+1))
        return Polynomial(l)
        

class PolyRing(Polynomial):
    def __mul__(self, other):
        deg1, deg2 = len(self.coeff), len(other.coeff)
        l = [0 for i in range(deg1 + deg2 - 1)]
        for i in range(deg1):
            for j in range(deg2):
                l[i+j] += self.coeff[i] * other.coeff[j]
        return PolyRing(l)

p = PolyRing([1,2,3])
p.antiderivative().derivative() == p    # dangerous: compares int to float
