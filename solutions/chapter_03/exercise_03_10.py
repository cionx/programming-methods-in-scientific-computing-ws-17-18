def trapeze(f, a, b, mmax):
    integrals = []              # list of the approximations
    values = [f(a), f(b)]       # list of the calculated values
    for m in range(1,mmax+1):
        n = 2**m
        for k in range(1,n,2):
            values.insert(k, f(a + (k/n)*(b-a)))    # add new values
        integral = 0
        for i in range(len(values)-1):
            integral += values[i] + values[i+1]
        integral = (b-a)*integral/n/2
        integrals.append(integral)                  # add new approx.
    return integrals

### Use m = 11
#
#   from math import exp
#   f = (lambda x: exp(x**2))
#   m = 11
#   results = trapeze(f, 0, 1, m)
#   for i in range(m):
#   print("m={:2d}\t{:24.20f}".format(i+1, results[i]))
#
###
