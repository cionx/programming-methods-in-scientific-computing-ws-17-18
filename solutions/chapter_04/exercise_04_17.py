from scipy import sin, exp, pi, linspace
from scipy.integrate import quad, romberg, trapz, simps

# defining the functions
f = sin
def g(x): return 3**(3*x-1)
def h(x): return exp(x**2)

# defining the intervals
x1 = linspace(0, pi, 1000)
x2 = linspace(0, 2, 1000)
x3 = linspace(0, 1, 1000)

# creating the output
print( "         {:19} {:21} {:20}".format( "sin(x) from 0 to pi ", "3^(3x-1) from 0 to 2", "e^(x^2) from 0 to 1" ) )
print( "quad:    {:19.17f} {:21.17f} {:20.17f}".format( quad(f,0,pi)[0], quad(g,0,2)[0], quad(h,0,1)[0] ) )
print( "romberg: {:19.17f} {:21.17f} {:20.17f}".format( romberg(f,0,pi), romberg(g,0,2), romberg(h,0,1) ) )
print( "trapz:   {:19.17f} {:21.17f} {:20.17f}".format( trapz(f(x1), x1), trapz(g(x2), x2), trapz(h(x3), x3)  ) )
print( "simps:   {:19.17f} {:21.17f} {:20.17f}".format( simps(f(x1), x1), simps(g(x2), x2), simps(h(x3), x3)  ) )

### OUTPUT:
#            sin(x) from 0 to pi  3^(3x-1) from 0 to 2  e^(x^2) from 0 to 1 
#   quad:    2.00000000000000000  73.62823966492641148  1.46265174590718150
#   romberg: 2.00000000000132117  73.62823966494875094  1.46265174591010316
#   trapz:   1.99999835177085195  73.62850679530863829  1.46265219986153205
#   simps:   1.99999999999701172  73.62824054651866845  1.46265174667154541
