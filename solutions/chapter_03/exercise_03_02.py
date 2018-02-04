class Polynomial:
    def __init__(self, coeff):
        self.coeff = coeff
    
    # convert polynomial to string for printing
    def __str__(self):
        s = ""
        first = True # checks if other terms have already been printed
        # go from highest coeff to lowest
        for i in range(len(self.coeff)-1, -1, -1):
            c = self.coeff[i] # current coefficient
            # dont print zero coefficient
            if c == 0:
                continue
            prefix = ""
            power = ""
            # check for sign of next coefficent
            if c < 0:
                if first:
                    prefix = "-"
                else:
                    prefix = " - "
            else:
                if not first:
                    prefix = " + "
            # check for power
            if i >= 2:
                power = "x^{}".format(i)
            elif(i == 1):
                power = "x"
            # add new term to output string
            s += prefix + str(abs(c)) + power
            first = False
        # check for zero polynomial
        if s == "":
            s = "0"
        return s
    
    # to get string representation in terminal without printing command
    def __repr__(self):
        return str(s)
    
    # evaluate polynomia at a point
    def __call__(self, x):
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s
    
    # coefficienttwise addition of polynomials
    def __add__(self, other):
        l = []
        if len(self.coeff) > len(other.coeff):
            l += self.coeff  # append to list
            for i in range(len(other.coeff)):
                l[i] += other.coeff[i]
        else:
            l += other.coeff # append to list
            for i in range(len(self.coeff)):
                l[i] += self.coeff[i]
        return Polynomial(l)
    
    # check for equality coefficientwise
    def __eq__(self, other):
        return self.coeff == other.coeff
    
    # calculates the derivative
    def derivative(self):
        coeff = []
        for i in range(1,len(self.coeff)):
            coeff.append(i * self.coeff[i])
        return Polynomial(coeff)
    
    # calculates the antiderivative with zero constant term
    def antiderivative(self):
        coeff = [0]
        for i in range(len(self.coeff)):
            coeff.append(self.coeff[i]/(i+1))
        return Polynomial(coeff)



# Testing the class and its methods:

p = Polynomial([1,2,3])
print("The given polynmial p:")
print(p)

#   OUTPUT:
#   The given polynmial p:
#   3x^2 + 2x + 1

print("The derivative of p:")
print( p.derivative() )

#   OUTPUT:
#   The derivative of p:
#   6x + 2

print("The antiderivative of p:")
print( p.antiderivative() )

#   OUTPUT:
#   The antiderivative of p:
#   1.0x^3 + 1.0x^2 + 1.0x

print("Taking antiderivative and then derivative:")
print( p.antiderivative().derivative() )

#   OUTPUT:
#   Taking antiderivative and then derivative:
#   3.0x^2 + 2.0x + 1.0
