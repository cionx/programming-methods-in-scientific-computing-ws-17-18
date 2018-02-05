from scipy import linspace
from scipy.interpolate import InterpolatedUnivariateSpline
import matplotlib.pyplot as plt

f = (lambda z: 1/(1 + 25*z**2))

# appoximation by splines with n equidistant points
def rungespline(n):
    xvals = linspace(-1,1,n)
    yvals = f(xvals)
    
    spline = InterpolatedUnivariateSpline(xvals, yvals, k=3) # degree 3
    
    lin = linspace(-1,1,100)
    plt.clf()
    plt.plot(lin, f(lin))
    plt.plot(lin, spline(lin))
    plt.show()

for n in [5,7,11]:
    rungespline(n)
