from scipy import *
from scipy.interpolate import InterpolatedUnivariateSpline
#import scipy.interpolate.InterpolatedUnivariateSpline as Spline
import matplotlib.pyplot as plt

f = (lambda z: 1/(1 + 25*z**2))

def rungespline(n):
    xvals = linspace(-1,1,n+1)
    yvals = f(xvals)
    
    spline = InterpolatedUnivariateSpline(xvals, yvals, k=3)
    
    lin = linspace(-1,1,100)
    plt.clf()
    plt.plot(lin, f(lin))
    plt.plot(lin, spline(lin))
    plt.show()

for n in range(3,10):
    rungespline(n)
