def exp_approx(x):
    y = 1           # current approx
    eps = 10**6     # 1/precision
    n = 1
    fac = 1         # n!
    if x >= 0:
        while fac < (3**x) * (x**(n+1)) * eps:
            print(n)
            y += x**n / fac
            n += 1  
            fac *= n
    if x < 0:
        while fac < ((-x)**(n+1)) * eps:
            y += x**n / fac
            n += 1  
            fac *= n
    return y

# problems for x >= 23, x <= -26
