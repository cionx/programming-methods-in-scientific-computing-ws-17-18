def bisect_it(f, a, b, err=1e-6):
    x = (a+b)/2
    while abs(f(x)) >= err:
        # f(a) < 0 < f(b) by assumption
        if f(x) > 0:
            b = x
        else:
            a = x
        x = (a+b)/2
    return x

def bisect_rec(f, a, b, err=1e-6):
    x = (a+b)/2
    if abs(f(x)) < err:
        return x
    if f(x) > 0:
        return bisect_rec(f, a, x, err)
    else:
        return bisect_rec(f, x, b, err)



from scipy import linspace, sin
import matplotlib.pyplot as plt

def f(x): return sin(4*x-1)+ x + x**20 - 1

x = linspace(-1.1, 1.1, 100)
plt.clf()
plt.plot(x, f(x))
plt.grid()
plt.show()

xit1, xit2 = bisect_it(f, 0, -1.5), bisect_it(f,0,1)
print("The roots with bisect_it are {} and {}.".format(xit1, xit2))

### OUTPUT:
#   The roots with bisect_it are -1.002246916294098 and 0.4082937240600586.

xrec1, xrec2 = bisect_rec(f, 0, -1.5), bisect_rec(f,0,1)
print("The roots with bisect_rec are {} and {}.".format(xrec1, xrec2))

### OUTPUT:
#   The roots with bisect_rec are -1.002246916294098 and 0.4082937240600586.
